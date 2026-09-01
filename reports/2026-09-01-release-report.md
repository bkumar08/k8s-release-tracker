# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated September 01, 2026 at 12:54 UTC)

## Weekly Release Summary by Vendor

> **4 breaking change(s) detected** across 5 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 4 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 1 | 0 | OK |
| Amazon EKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 0 | 0 | No updates |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.37.0 | 2026-08-26 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0) |

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

#### 🔴 Amazon EMR on EKS now supports job run concurrency controls

- **Date:** Fri, 28 Au
- **Severity:** CRITICAL
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-emr-eks/)
- **What to watch for:** CRI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI

---

## Azure AKS

### Breaking Changes / Deprecations (1)

#### 🟠 AppNet 2026-08-19 (AppNet-2026-08-19)

- **Date:** 2026-08-31
- **Severity:** HIGH
- **Component:** AKS
- **Details:** [View full release notes](https://github.com/Azure/AKS/releases/tag/AppNet-2026-08-19)
- **What to watch for:** removed, no longer supported, authentication, certificate rotation, CRI, not supported
- **Qualys Sensor Impact:** This change may affect sensor connectivity — certificate rotation, CRI, not supported

---

## Google GKE

No releases or updates found in this period.

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

#### 🔴 4.22.0-okd-scos.9

- **Date:** 2026-09-01
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.9)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.ec.8

- **Date:** 2026-09-01
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.8)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
