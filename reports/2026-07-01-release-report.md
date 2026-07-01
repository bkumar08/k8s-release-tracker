# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated July 01, 2026 at 11:18 UTC)

## Weekly Release Summary by Vendor

> **6 breaking change(s) detected** across 7 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 4 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 1 | 0 | OK |
| Amazon EKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 2 | 2 | **Action needed** |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.37.0-alpha.2 | 2026-06-25 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-alpha.2) |

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

#### 🟠 EKS Distro v1-36-eks-4 Release (v1-36-eks-4)

- **Date:** 2026-06-24
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-36-eks-4)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

---

## Azure AKS

### Breaking Changes / Deprecations (1)

#### 🔴 Release - 2026-06-19 (2026-06-19)

- **Date:** 2026-06-25
- **Severity:** CRITICAL
- **Component:** AKS
- **Details:** [View full release notes](https://github.com/Azure/AKS/releases/tag/2026-06-19)
- **What to watch for:** DaemonSet, privileged, CoreDNS, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, privileged

---

## Google GKE

### Breaking Changes / Deprecations (2)

#### 🟠 June 26, 2026

- **Date:** 2026-06-26
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_26_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

#### 🟠 June 29, 2026

- **Date:** 2026-06-29
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_29_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

#### 🔴 4.22.0-okd-scos.6

- **Date:** 2026-06-29
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.6)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver

#### 🔴 5.0.0-okd-scos.ec.4

- **Date:** 2026-06-29
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.4)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
