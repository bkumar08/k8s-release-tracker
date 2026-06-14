"""
Analyzer module for detecting breaking changes, deprecations,
and security issues in release notes.
"""

import re
import logging
from typing import List, Dict, Tuple

logger = logging.getLogger(__name__)


class BreakingChangeAnalyzer:
    """Analyzes release notes to identify breaking changes and deprecations."""

    def __init__(self, config: dict):
        self.keywords = config.get("breaking_change_keywords", [])
        self.severity_keywords = config.get("severity_keywords", {})

    def analyze(self, releases: List[Dict]) -> List[Dict]:
        """
        Analyze releases and flag those containing breaking changes.
        Returns releases enriched with breaking_changes and severity fields.
        """
        analyzed = []
        for release in releases:
            result = self._analyze_single(release)
            analyzed.append(result)

        # Sort: breaking changes first, then by severity, then by date
        severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
        analyzed.sort(key=lambda r: (
            0 if r.get("has_breaking_changes") else 1,
            severity_order.get(r.get("severity", "info"), 4),
            r.get("date", ""),
        ))

        breaking_count = sum(1 for r in analyzed if r.get("has_breaking_changes"))
        logger.info(f"Analysis complete: {breaking_count}/{len(analyzed)} releases have breaking changes")
        return analyzed

    def _analyze_single(self, release: Dict) -> Dict:
        """Analyze a single release for breaking changes."""
        result = release.copy()
        body = release.get("body", "").lower()
        title = release.get("title", "").lower()
        combined = f"{title} {body}"

        # Find matching keywords
        matched_keywords = []
        for keyword in self.keywords:
            if keyword.lower() in combined:
                matched_keywords.append(keyword)

        # Extract breaking change sections
        breaking_sections = self._extract_breaking_sections(release.get("body", ""))

        # Determine severity
        severity = self._classify_severity(combined)

        result["has_breaking_changes"] = len(matched_keywords) > 0
        result["matched_keywords"] = matched_keywords
        result["breaking_sections"] = breaking_sections
        result["severity"] = severity

        return result

    def _extract_breaking_sections(self, body: str) -> List[str]:
        """Extract specific breaking change sections from release body."""
        sections = []
        if not body:
            return sections

        # Common patterns for breaking change sections in K8s changelogs
        patterns = [
            # ## Breaking Changes / ## Deprecations / ## Urgent Upgrade Notes
            r'(?:^|\n)#{1,3}\s*(?:Breaking Changes?|Deprecations?|Urgent Upgrade Notes|Action Required|API Removals?)[\s:]*\n(.*?)(?=\n#{1,3}\s|\Z)',
            # - **Breaking:** or - **Deprecated:**
            r'[-*]\s*\*\*(?:Breaking|Deprecated|Removed|Action Required)\*\*[:\s]*(.*?)(?=\n[-*]|\n\n|\Z)',
            # Lines containing ACTION REQUIRED
            r'(?:^|\n).*ACTION REQUIRED.*(?:\n|$)',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, body, re.IGNORECASE | re.DOTALL)
            for match in matches:
                cleaned = match.strip()
                if cleaned and len(cleaned) > 10:
                    sections.append(cleaned[:1000])

        return sections

    def _classify_severity(self, text: str) -> str:
        """Classify severity based on keywords."""
        for severity in ["critical", "high", "medium", "low"]:
            keywords = self.severity_keywords.get(severity, [])
            for keyword in keywords:
                if keyword.lower() in text:
                    return severity
        return "info"


def get_summary_stats(analyzed_releases: List[Dict], lookback_days: int = 7) -> Dict:
    """Generate summary statistics from analyzed releases."""
    stats = {
        "total_releases": len(analyzed_releases),
        "breaking_changes": 0,
        "lookback_days": lookback_days,
        "by_source": {},
        "by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0},
    }

    for release in analyzed_releases:
        source = release.get("source", "Unknown")
        severity = release.get("severity", "info")
        has_breaking = release.get("has_breaking_changes", False)

        if source not in stats["by_source"]:
            stats["by_source"][source] = {"total": 0, "breaking": 0}

        stats["by_source"][source]["total"] += 1
        stats["by_severity"][severity] += 1

        if has_breaking:
            stats["breaking_changes"] += 1
            stats["by_source"][source]["breaking"] += 1

    return stats
