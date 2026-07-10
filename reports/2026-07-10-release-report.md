# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated July 10, 2026 at 10:45 UTC)

## Weekly Release Summary by Vendor

> **1 breaking change(s) detected** across 4 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 1 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 1 | 0 | OK |
| Amazon EKS | 2 | 1 (Sensor: 1) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 1 | 0 | OK |
| Red Hat OpenShift | 0 | 0 | No updates |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.37.0-alpha.3 | 2026-07-08 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-alpha.3) |

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

#### 🟡 v1.22.3

- **Date:** 2026-07-06
- **Severity:** MEDIUM
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.22.3)
- **What to watch for:** CRI, DaemonSet, CNI, VPC CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Tue, 07 Ju | Amazon EKS Auto Mode reduces GPU management fees by up to 60% | [View](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-auto-mode-gpu-price) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-07-07 | July 07, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_07_2026) |

---

## Red Hat OpenShift

No releases or updates found in this period.

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
