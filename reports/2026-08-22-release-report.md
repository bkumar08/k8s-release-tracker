# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated August 22, 2026 at 08:18 UTC)

## Weekly Release Summary by Vendor

> **2 breaking change(s) detected** across 9 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 2 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 4 | 0 | OK |
| Amazon EKS | 2 | 0 | OK |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 1 | 0 | OK |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (4)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.37.0-rc.1 | 2026-08-20 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-rc.1) |
| v1.36.4 | 2026-08-20 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.4) |
| v1.34.11 | 2026-08-20 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.34.11) |
| v1.35.8 | 2026-08-20 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.8) |

---

## Amazon EKS

**No breaking changes in this period.**

### Releases (2)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Fri, 21 Au | Amazon EKS Capability for Argo CD now supports custom configuration | [View](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-argo-cd-configuration) |
|  | Thu, 20 Au | Amazon EKS now supports certificate authority (CA) rotation with automated lifecycle management | [View](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-certificate-authority-ca-rotation-automated-lifecycle-management) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-08-18 | August 18, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#August_18_2026) |

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

#### 🔴 5.0.0-okd-scos.ec.7

- **Date:** 2026-08-17
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.7)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 4.22.0-okd-scos.8

- **Date:** 2026-08-20
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.8)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
