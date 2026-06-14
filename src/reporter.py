"""
Reporter module for generating markdown reports from analyzed releases.
Organized by provider for easy reading by support teams.
"""

import logging
from datetime import datetime, timezone
from typing import List, Dict
from collections import defaultdict

logger = logging.getLogger(__name__)

# Map raw source names to clean provider categories
PROVIDER_MAP = {
    "Kubernetes": "Kubernetes (Upstream)",
    "EKS": "Amazon EKS",
    "EKS (amazon-vpc-cni-k8s)": "Amazon EKS",
    "EKS (aws-node-termination-handler)": "Amazon EKS",
    "EKS (eks-anywhere)": "Amazon EKS",
    "EKS (eks-distro)": "Amazon EKS",
    "AKS": "Azure AKS",
    "AKS (Changelog)": "Azure AKS",
    "GKE": "Google GKE",
    "OpenShift (okd)": "Red Hat OpenShift",
    "OpenShift (origin)": "Red Hat OpenShift",
    "OpenShift (Errata)": "Red Hat OpenShift",
}

PROVIDER_ORDER = [
    "Kubernetes (Upstream)",
    "Amazon EKS",
    "Azure AKS",
    "Google GKE",
    "Red Hat OpenShift",
]

SEVERITY_EMOJI = {
    "critical": "🔴",
    "high": "🟠",
    "medium": "🟡",
    "low": "🔵",
    "info": "⚪",
}


class MarkdownReporter:
    """Generates markdown reports organized by provider."""

    def generate(self, analyzed_releases: List[Dict], stats: Dict) -> str:
        """Generate a full markdown report grouped by provider."""
        now = datetime.now(timezone.utc).strftime("%B %d, %Y at %H:%M UTC")
        month_year = datetime.now(timezone.utc).strftime("%B %Y")
        lookback = stats.get("lookback_days", 7)

        lines = []
        lines.append(f"# Kubernetes Ecosystem — Weekly Releases by Vendor")
        lines.append(f"**Report Period:** Last {lookback} days (generated {now})")
        lines.append("")

        # Quick summary at the top
        lines.append(self._generate_quick_summary(analyzed_releases, stats))

        # Group releases by provider
        by_provider = self._group_by_provider(analyzed_releases)

        # Generate a section for each provider
        for provider in PROVIDER_ORDER:
            releases = by_provider.get(provider, [])
            lines.append(self._generate_provider_section(provider, releases))

        # Handle any releases that didn't match a known provider
        known = set(PROVIDER_ORDER)
        for provider, releases in by_provider.items():
            if provider not in known:
                lines.append(self._generate_provider_section(provider, releases))

        # Footer
        lines.append("---")
        lines.append("")
        lines.append("*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). "
                      "Breaking changes are detected via keyword matching in release notes.*")
        lines.append("")

        return "\n".join(lines)

    def _generate_quick_summary(self, releases: List[Dict], stats: Dict) -> str:
        """Generate a quick summary box at the top."""
        lines = []
        breaking = [r for r in releases if r.get("has_breaking_changes")]
        total = len(releases)

        lines.append("## Weekly Release Summary by Vendor")
        lines.append("")

        if breaking:
            lines.append(f"> **{len(breaking)} breaking change(s) detected** across {total} total releases. Review the sections below for details.")
        else:
            lines.append(f"> **No breaking changes detected.** {total} release(s) found in this period.")

        lines.append("")

        # Provider status table
        by_provider = self._group_by_provider(releases)
        lines.append("| Vendor | Releases This Week | Breaking Changes | Status |")
        lines.append("|--------|-------------------|-----------------|--------|")

        for provider in PROVIDER_ORDER:
            provider_releases = by_provider.get(provider, [])
            count = len(provider_releases)
            breaking_count = sum(1 for r in provider_releases if r.get("has_breaking_changes"))

            if count == 0:
                status = "No updates"
            elif breaking_count > 0:
                status = f"**Action needed**"
            else:
                status = "OK"

            lines.append(f"| {provider} | {count} | {breaking_count} | {status} |")

        lines.append("")
        return "\n".join(lines)

    def _group_by_provider(self, releases: List[Dict]) -> Dict[str, List[Dict]]:
        """Group releases by normalized provider name."""
        grouped = defaultdict(list)
        for release in releases:
            raw_source = release.get("source", "Unknown")
            provider = PROVIDER_MAP.get(raw_source, raw_source)
            grouped[provider].append(release)
        return dict(grouped)

    def _generate_provider_section(self, provider: str, releases: List[Dict]) -> str:
        """Generate a section for a single provider."""
        lines = []
        lines.append("---")
        lines.append("")
        lines.append(f"## {provider}")
        lines.append("")

        if not releases:
            lines.append("No releases or updates found in this period.")
            lines.append("")
            return "\n".join(lines)

        # Separate breaking and non-breaking
        breaking = [r for r in releases if r.get("has_breaking_changes")]
        normal = [r for r in releases if not r.get("has_breaking_changes")]

        # Breaking changes first
        if breaking:
            lines.append(f"### Breaking Changes / Deprecations ({len(breaking)})")
            lines.append("")
            for release in breaking:
                lines.append(self._format_breaking_release(release))
        else:
            lines.append("**No breaking changes in this period.**")
            lines.append("")

        # All releases
        if normal:
            lines.append(f"### Releases ({len(normal)})")
            lines.append("")
            lines.append("| Version | Release Date | Title | Link |")
            lines.append("|---------|-------------|-------|------|")
            for release in normal:
                version = release.get("version", "—")
                date = release.get("date", "")[:10]
                title = release.get("title", "—")
                url = release.get("url", "")
                link = f"[View]({url})" if url else "—"
                # Clean up title if it's same as version
                if title == version:
                    title = "—"
                lines.append(f"| {version} | {date} | {title} | {link} |")
            lines.append("")

        return "\n".join(lines)

    def _format_breaking_release(self, release: Dict) -> str:
        """Format a release with breaking changes in a clear way."""
        lines = []
        severity = release.get("severity", "info")
        emoji = SEVERITY_EMOJI.get(severity, "⚪")
        version = release.get("version", "")
        title = release.get("title", "Untitled")
        date = release.get("date", "")[:10]
        url = release.get("url", "")
        source = release.get("source", "")

        # Header
        display_title = title
        if version and version != title:
            display_title = f"{title} ({version})"
        elif version:
            display_title = version

        lines.append(f"#### {emoji} {display_title}")
        lines.append("")
        lines.append(f"- **Date:** {date}")
        lines.append(f"- **Severity:** {severity.upper()}")
        if source:
            lines.append(f"- **Component:** {source}")
        if url:
            lines.append(f"- **Details:** [View full release notes]({url})")

        # What changed
        keywords = release.get("matched_keywords", [])
        if keywords:
            lines.append(f"- **What to watch for:** {', '.join(keywords)}")

        # Breaking change details
        sections = release.get("breaking_sections", [])
        if sections:
            lines.append("")
            lines.append("<details>")
            lines.append("<summary>Click to see breaking change details</summary>")
            lines.append("")
            for section in sections:
                lines.append("```")
                lines.append(section[:800])
                lines.append("```")
            lines.append("")
            lines.append("</details>")

        lines.append("")
        return "\n".join(lines)


def generate_report_filename() -> str:
    """Generate a filename for today's report."""
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"{date_str}-release-report.md"
