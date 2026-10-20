# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated October 20, 2026 at 13:09 UTC)

## Weekly Release Summary by Vendor

> **2 breaking change(s) detected** across 4 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 1 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 1 | 0 | OK |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 2 | 1 | **Action needed** |
| Red Hat OpenShift | 1 | 1 (Sensor: 1) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v0.26.3 | 2026-10-15 | — | [View](https://github.com/aws/eks-anywhere/releases/tag/v0.26.3) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (1)

#### 🟠 October 14, 2026

- **Date:** 2026-10-14
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_14_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-10-16 | October 16, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_16_2026) |

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (1)

#### 🔴 5.0.0-okd-scos.2

- **Date:** 2026-10-13
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.2)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
