"""
K8s Release Tracker — Main entry point.

Fetches releases from Kubernetes, EKS, AKS, GKE, and OpenShift,
analyzes them for breaking changes, and generates a markdown report.
"""

import os
import sys
import logging
import yaml
from pathlib import Path

from src.fetchers import fetch_all_releases
from src.analyzer import BreakingChangeAnalyzer, get_summary_stats
from src.reporter import MarkdownReporter, generate_report_filename

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def load_config(config_path: str = None) -> dict:
    """Load configuration from YAML file."""
    if config_path is None:
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yaml")

    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def main():
    """Main entry point."""
    # Allow overriding config path via env var
    config_path = os.environ.get("CONFIG_PATH", None)
    config = load_config(config_path)

    # Override lookback days if set via env
    lookback_override = os.environ.get("LOOKBACK_DAYS")
    if lookback_override:
        config.setdefault("schedule", {})["lookback_days"] = int(lookback_override)

    lookback = config.get("schedule", {}).get("lookback_days", 7)
    logger.info(f"Starting K8s Release Tracker (lookback: {lookback} days)")

    # Step 1: Fetch releases from all sources
    logger.info("Fetching releases from all sources...")
    releases = fetch_all_releases(config)
    logger.info(f"Fetched {len(releases)} total releases")

    if not releases:
        logger.info("No releases found in the lookback period. Generating empty report.")

    # Step 2: Analyze for breaking changes
    logger.info("Analyzing releases for breaking changes...")
    analyzer = BreakingChangeAnalyzer(config)
    analyzed = analyzer.analyze(releases)

    # Step 3: Generate statistics
    stats = get_summary_stats(analyzed, lookback)
    breaking_count = stats["breaking_changes"]
    logger.info(f"Found {breaking_count} releases with breaking changes out of {len(analyzed)} total")

    # Step 4: Generate markdown report
    logger.info("Generating report...")
    reporter = MarkdownReporter()
    report = reporter.generate(analyzed, stats)

    # Step 5: Write report to file
    reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    filename = generate_report_filename()
    report_path = os.path.join(reports_dir, filename)

    with open(report_path, "w") as f:
        f.write(report)

    logger.info(f"Report written to {report_path}")

    # Step 6: Set GitHub Actions output if running in CI
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"report_path={report_path}\n")
            f.write(f"report_filename={filename}\n")
            f.write(f"breaking_count={breaking_count}\n")
            f.write(f"total_count={len(analyzed)}\n")
            has_breaking = "true" if breaking_count > 0 else "false"
            f.write(f"has_breaking_changes={has_breaking}\n")

    # Print summary to stdout
    print(f"\n{'='*60}")
    print(f"  K8s Release Tracker Report")
    print(f"{'='*60}")
    print(f"  Total releases found:    {len(analyzed)}")
    print(f"  Breaking changes:        {breaking_count}")
    print(f"  Report:                  {report_path}")
    print(f"{'='*60}\n")

    # Exit with code 1 if critical breaking changes found (useful for CI alerts)
    if stats["by_severity"].get("critical", 0) > 0:
        logger.warning("CRITICAL breaking changes detected!")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
