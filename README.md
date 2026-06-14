# K8s Release Tracker

Automatically tracks breaking changes across the Kubernetes ecosystem and pushes reports to this repository.

## What It Monitors

| Source | What's Tracked |
|--------|---------------|
| **Kubernetes** | Upstream releases, deprecations, API removals |
| **Amazon EKS** | Version support, add-on updates, platform changes |
| **Azure AKS** | Release notes, version support, feature changes |
| **Google GKE** | Release channel updates, version support |
| **OpenShift** | OKD/OCP releases, errata, security advisories |

## How It Works

1. **GitHub Actions** runs daily (8:00 AM UTC) on a cron schedule
2. **Python script** fetches releases from GitHub APIs and RSS feeds
3. **Analyzer** scans release notes for breaking change keywords
4. **Reporter** generates a markdown report in `reports/`
5. **Auto-commit** pushes the report to this repo
6. **GitHub Issue** is created if breaking changes are detected

## Setup

### 1. Create a GitHub Repository

```bash
# Clone this project
git clone https://github.com/YOUR_USERNAME/k8s-release-tracker.git
cd k8s-release-tracker

# Or push this folder as a new repo
git init
git add .
git commit -m "Initial commit: K8s Release Tracker"
git remote add origin https://github.com/YOUR_USERNAME/k8s-release-tracker.git
git push -u origin main
```

### 2. Enable GitHub Actions

No additional setup needed — the workflow uses the built-in `GITHUB_TOKEN` which has read access to public repos and write access to your repository.

### 3. (Optional) Configure

Edit `config.yaml` to:
- Enable/disable specific sources
- Adjust the lookback window (default: 7 days)
- Add custom breaking change keywords

### 4. Run Manually (First Time)

Go to **Actions** → **K8s Release Tracker** → **Run workflow** to test it immediately.

## Run Locally

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run (optionally set LOOKBACK_DAYS for wider window)
LOOKBACK_DAYS=30 python -m src.main
```

Reports are saved to `reports/YYYY-MM-DD-release-report.md`.

## Report Structure

Each report includes:
- **Summary table** — total releases, breaking change count, severity breakdown
- **Breaking Changes section** — detailed view with matched keywords and expandable details
- **Other Releases section** — non-breaking updates for awareness

## Customization

### Change Schedule

Edit `.github/workflows/check-releases.yml`:
```yaml
schedule:
  - cron: '0 8 * * *'    # Daily at 8 AM UTC
  # - cron: '0 8 * * 1'  # Weekly on Mondays
  # - cron: '0 */6 * * *' # Every 6 hours
```

### Add Slack Notifications

Add this step to the workflow after the commit step:
```yaml
- name: Notify Slack
  if: steps.tracker.outputs.has_breaking_changes == 'true'
  uses: slackapi/slack-github-action@v1.24.0
  with:
    payload: |
      {"text": "⚠️ K8s Breaking Changes: ${{ steps.tracker.outputs.breaking_count }} found. See: https://github.com/${{ github.repository }}/tree/main/reports"}
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```

## Project Structure

```
k8s-release-tracker/
├── .github/workflows/
│   └── check-releases.yml    # GitHub Actions workflow (daily cron)
├── src/
│   ├── fetchers.py            # Fetches releases from all sources
│   ├── analyzer.py            # Detects breaking changes via keyword matching
│   ├── reporter.py            # Generates markdown reports
│   └── main.py                # Entry point
├── reports/                   # Auto-generated reports (git-tracked)
├── config.yaml                # Configuration file
├── requirements.txt
└── README.md
```
