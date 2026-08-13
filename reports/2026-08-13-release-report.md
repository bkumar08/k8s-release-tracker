# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated August 13, 2026 at 09:03 UTC)

## Weekly Release Summary by Vendor

> **3 breaking change(s) detected** across 5 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 2 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 1 | 0 | OK |
| Amazon EKS | 2 | 1 (Sensor: 1) | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 1 | 1 | **Action needed** |
| Red Hat OpenShift | 0 | 0 | No updates |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.37.0-rc.0 | 2026-08-06 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-rc.0) |

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

#### 🔴 v1.23.0

- **Date:** 2026-08-07
- **Severity:** CRITICAL
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.23.0)
- **What to watch for:** RBAC, containerd, CRI, DaemonSet, network policy, CNI, VPC CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, containerd, CRI

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Wed, 12 Au | Amazon EKS now supports advanced Kubernetes control plane configuration parameters | [View](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-control-plane-configuration-parameters) |

---

## Azure AKS

### Breaking Changes / Deprecations (1)

#### 🔴 Release 2026-08-07 (2026-08-07)

- **Date:** 2026-08-11
- **Severity:** CRITICAL
- **Component:** AKS
- **Details:** [View full release notes](https://github.com/Azure/AKS/releases/tag/2026-08-07)
- **What to watch for:** service account token, authentication, ServiceAccount, mount, incompatible
- **Qualys Sensor Impact:** This change may affect sensor connectivity — service account token, mount

---

## Google GKE

### Breaking Changes / Deprecations (1)

#### 🟠 August 12, 2026

- **Date:** 2026-08-12
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#August_12_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

---

## Red Hat OpenShift

No releases or updates found in this period.

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
