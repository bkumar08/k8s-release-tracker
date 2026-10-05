# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated October 05, 2026 at 16:38 UTC)

## Weekly Release Summary by Vendor

> **10 breaking change(s) detected** across 12 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 9 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 1 | 0 | OK |
| Amazon EKS | 8 | 7 (Sensor: 7) | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 1 | 1 | **Action needed** |
| Red Hat OpenShift | 1 | 1 (Sensor: 1) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.38.0-alpha.1 | 2026-09-29 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.38.0-alpha.1) |

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

#### 🟡 v1.23.2

- **Date:** 2026-09-30
- **Severity:** MEDIUM
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.23.2)
- **What to watch for:** CRI, DaemonSet, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

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

### Breaking Changes / Deprecations (1)

#### 🟠 October 02, 2026

- **Date:** 2026-10-02
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_02_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

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
