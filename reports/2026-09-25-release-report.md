# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated September 25, 2026 at 13:07 UTC)

## Weekly Release Summary by Vendor

> **4 breaking change(s) detected** across 9 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 3 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 4 | 0 | OK |
| Amazon EKS | 4 | 3 (Sensor: 3) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 1 | 1 | **Action needed** |
| Red Hat OpenShift | 0 | 0 | No updates |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (4)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.36.5 | 2026-09-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.5) |
| v1.37.1 | 2026-09-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.1) |
| v1.35.9 | 2026-09-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.9) |
| v1.34.12 | 2026-09-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.34.12) |

---

## Amazon EKS

### Breaking Changes / Deprecations (3)

#### 🟠 EKS Distro v1-37-eks-3 Release (v1-37-eks-3)

- **Date:** 2026-09-23
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-37-eks-3)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 v0.25.4

- **Date:** 2026-09-24
- **Severity:** HIGH
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.25.4)
- **What to watch for:** not supported
- **Qualys Sensor Impact:** This change may affect sensor connectivity — not supported

#### ⚪ Run interactive workloads on Amazon EMR on EKS with Spark Connect

- **Date:** Thu, 24 Se
- **Severity:** INFO
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/09/emr-eks-spark-connect-interactive/)
- **What to watch for:** CRI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Wed, 23 Se | Amazon EMR on EKS now supports IPv6 Amazon EKS clusters | [View](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-emr-eks-ipv6-support) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (1)

#### 🟠 September 23, 2026

- **Date:** 2026-09-23
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#September_23_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

---

## Red Hat OpenShift

No releases or updates found in this period.

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
