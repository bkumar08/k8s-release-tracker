# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated August 01, 2026 at 09:51 UTC)

## Weekly Release Summary by Vendor

> **10 breaking change(s) detected** across 12 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 8 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 9 | 8 (Sensor: 7) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 2 | 1 | **Action needed** |
| Red Hat OpenShift | 1 | 1 (Sensor: 1) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (8)

#### 🟠 EKS Distro v1-31-eks-47 Release (v1-31-eks-47)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-31-eks-47)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-30-eks-58 Release (v1-30-eks-58)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-30-eks-58)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-32-eks-40 Release (v1-32-eks-40)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-32-eks-40)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-33-eks-30 Release (v1-33-eks-30)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-33-eks-30)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-34-eks-21 Release (v1-34-eks-21)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-34-eks-21)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-35-eks-12 Release (v1-35-eks-12)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-35-eks-12)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-36-eks-6 Release (v1-36-eks-6)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-36-eks-6)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### ⚪ Amazon EKS now supports AWS PrivateLink for the cluster OIDC endpoint

- **Date:** Mon, 27 Ju
- **Severity:** INFO
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-oidc-endpoint-privatelink)
- **What to watch for:** OIDC

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Tue, 28 Ju | Amazon EKS Provisioned Control Plane now delivers faster pod autoscaling | [View](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-provisioned-control/) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (1)

#### 🟠 July 30, 2026

- **Date:** 2026-07-30
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_30_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-07-27 | July 27, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_27_2026) |

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (1)

#### 🔴 5.0.0-okd-scos.ec.6

- **Date:** 2026-07-27
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.6)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
