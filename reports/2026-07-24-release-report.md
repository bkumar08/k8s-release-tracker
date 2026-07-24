# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated July 24, 2026 at 10:09 UTC)

## Weekly Release Summary by Vendor

> **5 breaking change(s) detected** across 9 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 4 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 4 | 0 | OK |
| Amazon EKS | 4 | 4 (Sensor: 4) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 1 | 1 | **Action needed** |
| Red Hat OpenShift | 0 | 0 | No updates |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (4)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.37.0-beta.0 | 2026-07-20 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-beta.0) |
| v1.34.10 | 2026-07-22 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.34.10) |
| v1.35.7 | 2026-07-22 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.7) |
| v1.36.3 | 2026-07-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.3) |

---

## Amazon EKS

### Breaking Changes / Deprecations (4)

#### 🔴 Amazon EKS now supports EFA and placement groups on Amazon EKS Auto Mode and Karpenter

- **Date:** Wed, 22 Ju
- **Severity:** CRITICAL
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-efa-placement-groups/)
- **What to watch for:** CRI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI

#### 🟠 v0.26.0

- **Date:** 2026-07-17
- **Severity:** HIGH
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.26.0)
- **What to watch for:** removed, containerd, CRI, DaemonSet
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, containerd, CRI

#### 🟠 v0.25.3

- **Date:** 2026-07-23
- **Severity:** HIGH
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.25.3)
- **What to watch for:** containerd, DaemonSet, not supported
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, containerd, not supported

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

### Breaking Changes / Deprecations (1)

#### 🔴 July 20, 2026

- **Date:** 2026-07-20
- **Severity:** CRITICAL
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_20_2026)
- **What to watch for:** deprecated

---

## Red Hat OpenShift

No releases or updates found in this period.

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
