# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated September 30, 2026 at 14:27 UTC)

## Weekly Release Summary by Vendor

> **9 breaking change(s) detected** across 15 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 9 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 5 | 0 | OK |
| Amazon EKS | 9 | 8 (Sensor: 8) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 0 | 0 | No updates |
| Red Hat OpenShift | 1 | 1 (Sensor: 1) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (5)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.36.5 | 2026-09-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.5) |
| v1.37.1 | 2026-09-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.1) |
| v1.35.9 | 2026-09-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.9) |
| v1.34.12 | 2026-09-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.34.12) |
| v1.38.0-alpha.1 | 2026-09-29 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.38.0-alpha.1) |

---

## Amazon EKS

### Breaking Changes / Deprecations (8)

#### 🟠 v0.25.4

- **Date:** 2026-09-24
- **Severity:** HIGH
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.25.4)
- **What to watch for:** not supported
- **Qualys Sensor Impact:** This change may affect sensor connectivity — not supported

#### 🟠 EKS Distro v1-31-eks-49 Release (v1-31-eks-49)

- **Date:** 2026-09-25
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-31-eks-49)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-32-eks-42 Release (v1-32-eks-42)

- **Date:** 2026-09-25
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-32-eks-42)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-33-eks-32 Release (v1-33-eks-32)

- **Date:** 2026-09-25
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-33-eks-32)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-34-eks-23 Release (v1-34-eks-23)

- **Date:** 2026-09-25
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-34-eks-23)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-35-eks-14 Release (v1-35-eks-14)

- **Date:** 2026-09-25
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-35-eks-14)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-36-eks-8 Release (v1-36-eks-8)

- **Date:** 2026-09-25
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-36-eks-8)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

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

No releases or updates found in this period.

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (1)

#### 🔴 5.0.0-okd-scos.1

- **Date:** 2026-09-30
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.1)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
