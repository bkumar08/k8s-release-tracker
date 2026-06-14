"""
Fetchers for Kubernetes, EKS, AKS, GKE, and OpenShift release data.
Uses GitHub API and RSS feeds to collect release notes and changelogs.
"""

import os
import re
import logging
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional

import requests
import feedparser
from dateutil import parser as dateparser

logger = logging.getLogger(__name__)

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


def _github_headers() -> Dict[str, str]:
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers


def _within_lookback(date_str: str, lookback_days: int) -> bool:
    """Check if a date string is within the lookback window."""
    try:
        dt = dateparser.parse(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        cutoff = datetime.now(timezone.utc) - timedelta(days=lookback_days)
        return dt >= cutoff
    except Exception:
        return True  # Include if we can't parse the date


class ReleaseFetcher:
    """Base class for fetching release information."""

    def __init__(self, config: dict, lookback_days: int = 7):
        self.config = config
        self.lookback_days = lookback_days

    def fetch(self) -> List[Dict]:
        raise NotImplementedError


class KubernetesFetcher(ReleaseFetcher):
    """Fetch Kubernetes upstream releases from GitHub."""

    def fetch(self) -> List[Dict]:
        if not self.config.get("enabled", True):
            return []

        repo = self.config.get("github_repo", "kubernetes/kubernetes")
        url = f"{GITHUB_API}/repos/{repo}/releases"
        params = {"per_page": 30}

        try:
            resp = requests.get(url, headers=_github_headers(), params=params, timeout=30)
            resp.raise_for_status()
            releases = resp.json()
        except Exception as e:
            logger.error(f"Failed to fetch Kubernetes releases: {e}")
            return []

        results = []
        for rel in releases:
            published = rel.get("published_at", "")
            if not _within_lookback(published, self.lookback_days):
                continue

            results.append({
                "source": "Kubernetes",
                "version": rel.get("tag_name", ""),
                "title": rel.get("name", ""),
                "date": published,
                "body": rel.get("body", ""),
                "url": rel.get("html_url", ""),
                "prerelease": rel.get("prerelease", False),
            })

        logger.info(f"Kubernetes: found {len(results)} releases in last {self.lookback_days} days")
        return results


class EKSFetcher(ReleaseFetcher):
    """Fetch EKS changes from AWS docs changelog."""

    def fetch(self) -> List[Dict]:
        if not self.config.get("enabled", True):
            return []

        results = []

        # Fetch from GitHub releases of EKS-related repos
        eks_repos = [
            "aws/amazon-vpc-cni-k8s",
            "aws/aws-node-termination-handler",
            "aws/eks-anywhere",
            "aws/eks-distro",
        ]

        # Primary: EKS doc history
        changelog_url = self.config.get("changelog_url", "")
        if changelog_url:
            try:
                resp = requests.get(changelog_url, timeout=30)
                resp.raise_for_status()
                results.extend(self._parse_doc_history(resp.text))
            except Exception as e:
                logger.error(f"Failed to fetch EKS doc history: {e}")

        # Secondary: EKS-related GitHub repos
        for repo in eks_repos:
            try:
                url = f"{GITHUB_API}/repos/{repo}/releases"
                resp = requests.get(url, headers=_github_headers(), params={"per_page": 10}, timeout=30)
                resp.raise_for_status()
                for rel in resp.json():
                    published = rel.get("published_at", "")
                    if not _within_lookback(published, self.lookback_days):
                        continue
                    results.append({
                        "source": f"EKS ({repo.split('/')[-1]})",
                        "version": rel.get("tag_name", ""),
                        "title": rel.get("name", ""),
                        "date": published,
                        "body": rel.get("body", ""),
                        "url": rel.get("html_url", ""),
                        "prerelease": rel.get("prerelease", False),
                    })
            except Exception as e:
                logger.error(f"Failed to fetch {repo} releases: {e}")

        # AWS What's New announcements (catches token, auth, platform changes)
        announcements_rss = self.config.get("announcements_rss", "")
        if announcements_rss:
            try:
                feed = feedparser.parse(announcements_rss)
                for entry in feed.entries:
                    title = entry.get("title", "")
                    # Only include EKS-related announcements
                    if not any(kw in title.lower() for kw in ["eks", "kubernetes", "amazon elastic kubernetes"]):
                        continue
                    published = entry.get("published", entry.get("updated", ""))
                    if not _within_lookback(published, self.lookback_days):
                        continue
                    summary = entry.get("summary", "")
                    summary = re.sub(r'<[^>]+>', '', summary)
                    results.append({
                        "source": "EKS",
                        "version": "",
                        "title": title,
                        "date": published,
                        "body": summary[:3000],
                        "url": entry.get("link", ""),
                        "prerelease": False,
                    })
            except Exception as e:
                logger.error(f"Failed to fetch AWS announcements RSS: {e}")

        logger.info(f"EKS: found {len(results)} changes in last {self.lookback_days} days")
        return results

    def _parse_doc_history(self, text: str) -> List[Dict]:
        """Parse the EKS doc-history.md for recent changes."""
        results = []
        # Pattern: | [Title](link) | Description | Date |
        pattern = r'\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+)\|\s*(\w+ \d+, \d{4})\s*\|'
        for match in re.finditer(pattern, text):
            title, url, description, date_str = match.groups()
            if _within_lookback(date_str.strip(), self.lookback_days):
                results.append({
                    "source": "EKS",
                    "version": "",
                    "title": title.strip(),
                    "date": date_str.strip(),
                    "body": description.strip(),
                    "url": url.strip() if url.startswith("http") else f"https://docs.aws.amazon.com/eks/latest/userguide/{url.strip()}",
                    "prerelease": False,
                })
        return results


class AKSFetcher(ReleaseFetcher):
    """Fetch AKS releases from Azure/AKS GitHub repo."""

    def fetch(self) -> List[Dict]:
        if not self.config.get("enabled", True):
            return []

        results = []
        repo = self.config.get("github_repo", "Azure/AKS")

        # GitHub releases
        try:
            url = f"{GITHUB_API}/repos/{repo}/releases"
            resp = requests.get(url, headers=_github_headers(), params={"per_page": 20}, timeout=30)
            resp.raise_for_status()
            for rel in resp.json():
                published = rel.get("published_at", "")
                if not _within_lookback(published, self.lookback_days):
                    continue
                results.append({
                    "source": "AKS",
                    "version": rel.get("tag_name", ""),
                    "title": rel.get("name", ""),
                    "date": published,
                    "body": rel.get("body", ""),
                    "url": rel.get("html_url", ""),
                    "prerelease": rel.get("prerelease", False),
                })
        except Exception as e:
            logger.error(f"Failed to fetch AKS releases: {e}")

        # Also check the CHANGELOG if available
        changelog_url = self.config.get("release_notes_url", "")
        if changelog_url:
            try:
                resp = requests.get(changelog_url, timeout=30)
                resp.raise_for_status()
                results.extend(self._parse_aks_changelog(resp.text))
            except Exception as e:
                logger.error(f"Failed to fetch AKS changelog: {e}")

        logger.info(f"AKS: found {len(results)} changes in last {self.lookback_days} days")
        return results

    def _parse_aks_changelog(self, text: str) -> List[Dict]:
        """Parse AKS CHANGELOG.md for recent entries."""
        results = []
        # AKS changelog sections typically start with ## YYYY-MM-DD
        sections = re.split(r'^## (\d{4}-\d{2}-\d{2})', text, flags=re.MULTILINE)
        for i in range(1, len(sections) - 1, 2):
            date_str = sections[i]
            content = sections[i + 1]
            if _within_lookback(date_str, self.lookback_days):
                results.append({
                    "source": "AKS (Changelog)",
                    "version": "",
                    "title": f"AKS Update {date_str}",
                    "date": date_str,
                    "body": content.strip()[:3000],
                    "url": "https://github.com/Azure/AKS/blob/master/CHANGELOG.md",
                    "prerelease": False,
                })
        return results


class GKEFetcher(ReleaseFetcher):
    """Fetch GKE release notes from Google Cloud RSS feed."""

    def fetch(self) -> List[Dict]:
        if not self.config.get("enabled", True):
            return []

        results = []
        feed_url = self.config.get(
            "release_notes_url",
            "https://cloud.google.com/feeds/kubernetes-engine-release-notes.xml"
        )

        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                published = entry.get("published", entry.get("updated", ""))
                if not _within_lookback(published, self.lookback_days):
                    continue

                # Clean HTML from summary
                summary = entry.get("summary", "")
                summary = re.sub(r'<[^>]+>', '', summary)

                results.append({
                    "source": "GKE",
                    "version": "",
                    "title": entry.get("title", "GKE Update"),
                    "date": published,
                    "body": summary[:3000],
                    "url": entry.get("link", ""),
                    "prerelease": False,
                })
        except Exception as e:
            logger.error(f"Failed to fetch GKE release notes: {e}")

        logger.info(f"GKE: found {len(results)} changes in last {self.lookback_days} days")
        return results


class OpenShiftFetcher(ReleaseFetcher):
    """Fetch OpenShift releases from GitHub."""

    def fetch(self) -> List[Dict]:
        if not self.config.get("enabled", True):
            return []

        results = []

        # OpenShift OKD releases
        okd_repos = [
            "openshift/okd",
            "openshift/origin",
        ]

        for repo in okd_repos:
            try:
                url = f"{GITHUB_API}/repos/{repo}/releases"
                resp = requests.get(url, headers=_github_headers(), params={"per_page": 15}, timeout=30)
                resp.raise_for_status()
                for rel in resp.json():
                    published = rel.get("published_at", "")
                    if not _within_lookback(published, self.lookback_days):
                        continue
                    results.append({
                        "source": f"OpenShift ({repo.split('/')[-1]})",
                        "version": rel.get("tag_name", ""),
                        "title": rel.get("name", ""),
                        "date": published,
                        "body": rel.get("body", ""),
                        "url": rel.get("html_url", ""),
                        "prerelease": rel.get("prerelease", False),
                    })
            except Exception as e:
                logger.error(f"Failed to fetch {repo} releases: {e}")

        # OpenShift Container Platform errata (public RSS)
        try:
            feed_url = "https://access.redhat.com/errata-search/api/errata.atom?product=OpenShift+Container+Platform&type=Security+Advisory,Bug+Fix,Enhancement"
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:20]:
                published = entry.get("published", entry.get("updated", ""))
                if not _within_lookback(published, self.lookback_days):
                    continue
                summary = entry.get("summary", "")
                summary = re.sub(r'<[^>]+>', '', summary)
                results.append({
                    "source": "OpenShift (Errata)",
                    "version": "",
                    "title": entry.get("title", ""),
                    "date": published,
                    "body": summary[:3000],
                    "url": entry.get("link", ""),
                    "prerelease": False,
                })
        except Exception as e:
            logger.error(f"Failed to fetch OpenShift errata: {e}")

        logger.info(f"OpenShift: found {len(results)} changes in last {self.lookback_days} days")
        return results


def fetch_all_releases(config: dict) -> List[Dict]:
    """Fetch releases from all configured sources."""
    lookback = config.get("schedule", {}).get("lookback_days", 7)
    sources = config.get("sources", {})

    fetchers = [
        KubernetesFetcher(sources.get("kubernetes", {}), lookback),
        EKSFetcher(sources.get("eks", {}), lookback),
        AKSFetcher(sources.get("aks", {}), lookback),
        GKEFetcher(sources.get("gke", {}), lookback),
        OpenShiftFetcher(sources.get("openshift", {}), lookback),
    ]

    all_releases = []
    for fetcher in fetchers:
        try:
            releases = fetcher.fetch()
            all_releases.extend(releases)
        except Exception as e:
            logger.error(f"Error in {fetcher.__class__.__name__}: {e}")

    # Sort by date (newest first)
    all_releases.sort(key=lambda r: r.get("date", ""), reverse=True)
    return all_releases
