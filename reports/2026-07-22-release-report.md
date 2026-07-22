# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated July 22, 2026 at 10:17 UTC)

## Weekly Release Summary by Vendor

> **4 breaking change(s) detected** across 5 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 2 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 1 | 0 | OK |
| Amazon EKS | 2 | 2 (Sensor: 2) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 2 | 2 | **Action needed** |
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

### Breaking Changes / Deprecations (2)

#### 🟠 v0.26.0

- **Date:** 2026-07-17
- **Severity:** HIGH
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.26.0)
- **What to watch for:** removed, containerd, CRI, DaemonSet
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, containerd, CRI

#### 🟡 v1.22.4

- **Date:** 2026-07-22
- **Severity:** MEDIUM
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.22.4)
- **What to watch for:** CRI, DaemonSet, network policy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (2)

#### 🔴 July 20, 2026

- **Date:** 2026-07-20
- **Severity:** CRITICAL
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_20_2026)
- **What to watch for:** deprecated

#### 🟠 July 16, 2026

- **Date:** 2026-07-16
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_16_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

---

## Red Hat OpenShift

No releases or updates found in this period.

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
