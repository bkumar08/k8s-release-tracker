# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated October 08, 2026 at 15:05 UTC)

## Weekly Release Summary by Vendor

> **11 breaking change(s) detected** across 13 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 7 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 1 | 0 | OK |
| Amazon EKS | 8 | 7 (Sensor: 6) | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 3 | 3 | **Action needed** |
| Red Hat OpenShift | 0 | 0 | No updates |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.38.0-alpha.2 | 2026-10-07 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.38.0-alpha.2) |

---

## Amazon EKS

### Breaking Changes / Deprecations (7)

#### 🟠 EKS Distro v1-31-eks-50 Release (v1-31-eks-50)

- **Date:** 2026-10-02
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-31-eks-50)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-32-eks-43 Release (v1-32-eks-43)

- **Date:** 2026-10-02
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-32-eks-43)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-33-eks-33 Release (v1-33-eks-33)

- **Date:** 2026-10-02
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-33-eks-33)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-34-eks-24 Release (v1-34-eks-24)

- **Date:** 2026-10-02
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-34-eks-24)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-35-eks-15 Release (v1-35-eks-15)

- **Date:** 2026-10-02
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-35-eks-15)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-36-eks-9 Release (v1-36-eks-9)

- **Date:** 2026-10-02
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-36-eks-9)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 AWS Batch now supports Amazon EKS access entry authentication

- **Date:** Mon, 05 Oc
- **Severity:** HIGH
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-batch-access-entries/)
- **What to watch for:** authentication

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Fri, 02 Oc | Amazon EKS and Amazon EKS Distro now support Kubernetes version 1.37 | [View](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-distro-kubernetes-version-1-37) |

---

## Azure AKS

### Breaking Changes / Deprecations (1)

#### 🔴 Release Notes 2026-09-25 (2026-09-25)

- **Date:** 2026-10-01
- **Severity:** CRITICAL
- **Component:** AKS
- **Details:** [View full release notes](https://github.com/Azure/AKS/releases/tag/2026-09-25)
- **What to watch for:** removed, deprecated, CRI, not supported, incompatible, CoreDNS, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI, not supported

---

## Google GKE

### Breaking Changes / Deprecations (3)

#### 🟠 October 02, 2026

- **Date:** 2026-10-02
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_02_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

#### 🟡 October 05, 2026

- **Date:** 2026-10-05
- **Severity:** MEDIUM
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_05_2026)
- **What to watch for:** deprecated, deprecation

#### ⚪ October 06, 2026

- **Date:** 2026-10-06
- **Severity:** INFO
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_06_2026)
- **What to watch for:** CoreDNS

---

## Red Hat OpenShift

No releases or updates found in this period.

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
