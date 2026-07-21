# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated July 21, 2026 at 10:17 UTC)

## Weekly Release Summary by Vendor

> **1 breaking change(s) detected** across 2 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 1 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 1 | 0 | OK |
| Amazon EKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 0 | 0 | No updates |
| Red Hat OpenShift | 0 | 0 | No updates |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.37.0-beta.0 | 2026-07-20 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-beta.0) |

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

#### 🟠 v0.26.0

- **Date:** 2026-07-17
- **Severity:** HIGH
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.26.0)
- **What to watch for:** removed, containerd, CRI, DaemonSet
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, containerd, CRI

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

No releases or updates found in this period.

---

## Red Hat OpenShift

No releases or updates found in this period.

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
