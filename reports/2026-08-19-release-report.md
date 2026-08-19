# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated August 19, 2026 at 08:26 UTC)

## Weekly Release Summary by Vendor

> **3 breaking change(s) detected** across 5 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 2 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 2 | 1 (Sensor: 1) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 2 | 1 | **Action needed** |
| Red Hat OpenShift | 1 | 1 (Sensor: 1) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

#### ⚪ v0.26.1

- **Date:** 2026-08-13
- **Severity:** INFO
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.26.1)
- **What to watch for:** containerd
- **Qualys Sensor Impact:** This change may affect sensor connectivity — containerd

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Wed, 12 Au | Amazon EKS now supports advanced Kubernetes control plane configuration parameters | [View](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-control-plane-configuration-parameters) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (1)

#### 🟠 August 14, 2026

- **Date:** 2026-08-14
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#August_14_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-08-18 | August 18, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#August_18_2026) |

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (1)

#### 🔴 5.0.0-okd-scos.ec.7

- **Date:** 2026-08-17
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.7)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
