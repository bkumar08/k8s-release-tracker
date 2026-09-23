# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated September 23, 2026 at 13:09 UTC)

## Weekly Release Summary by Vendor

> **2 breaking change(s) detected** across 2 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 2 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 0 | 0 | No updates |
| Red Hat OpenShift | 1 | 1 (Sensor: 1) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

#### 🟠 EKS Distro v1-37-eks-3 Release (v1-37-eks-3)

- **Date:** 2026-09-23
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-37-eks-3)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

No releases or updates found in this period.

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (1)

#### 🔴 5.0.0-okd-scos.0

- **Date:** 2026-09-17
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.0)
- **What to watch for:** authentication, 401, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
