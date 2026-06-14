# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 30 days (generated June 14, 2026 at 07:30 UTC)

## Weekly Release Summary by Vendor

> **13 breaking change(s) detected** across 21 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 8 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 5 | 0 | OK |
| Amazon EKS | 4 | 2 (Sensor: 2) | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 6 | 5 | **Action needed** |
| Red Hat OpenShift | 5 | 5 (Sensor: 5) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (5)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.37.0-alpha.1 | 2026-06-11 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-alpha.1) |
| v1.33.13 | 2026-06-12 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.33.13) |
| v1.34.9 | 2026-06-12 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.34.9) |
| v1.35.6 | 2026-06-12 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.6) |
| v1.36.2 | 2026-06-12 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.2) |

---

## Amazon EKS

### Breaking Changes / Deprecations (2)

#### 🔴 v1.21.2

- **Date:** 2026-05-21
- **Severity:** CRITICAL
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.21.2)
- **What to watch for:** CRI, DaemonSet, CNI, VPC CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

#### 🔴 v1.22.1

- **Date:** 2026-05-29
- **Severity:** CRITICAL
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.22.1)
- **What to watch for:** CRI, DaemonSet, CNI, VPC CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

### Releases (2)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| weekly.2026-05-21 | 2026-05-21 | Weekly Release 2026-05-21 | [View](https://github.com/aws/eks-anywhere/releases/tag/weekly.2026-05-21) |
| weekly.2026-06-04 | 2026-06-04 | Weekly Release 2026-06-04 | [View](https://github.com/aws/eks-anywhere/releases/tag/weekly.2026-06-04) |

---

## Azure AKS

### Breaking Changes / Deprecations (1)

#### 🔴 Release 2026-05-29 (2026-05-29)

- **Date:** 2026-06-04
- **Severity:** CRITICAL
- **Component:** AKS
- **Details:** [View full release notes](https://github.com/Azure/AKS/releases/tag/2026-05-29)
- **What to watch for:** removed, deprecated, deprecation, must migrate, TokenReview, Unauthorized, TLS, pod security, CRI, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — Unauthorized, CRI

---

## Google GKE

### Breaking Changes / Deprecations (5)

#### 🔴 May 21, 2026

- **Date:** 2026-05-21
- **Severity:** CRITICAL
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#May_21_2026)
- **What to watch for:** deprecated

#### 🟠 June 10, 2026

- **Date:** 2026-06-10
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_10_2026)
- **What to watch for:** removed, deprecated, deprecation, will be removed

#### 🟡 May 27, 2026

- **Date:** 2026-05-27
- **Severity:** MEDIUM
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#May_27_2026)
- **What to watch for:** deprecated, no longer available

#### 🟡 June 04, 2026

- **Date:** 2026-06-04
- **Severity:** MEDIUM
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_04_2026)
- **What to watch for:** deprecated, no longer available

#### 🟡 June 12, 2026

- **Date:** 2026-06-12
- **Severity:** MEDIUM
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_12_2026)
- **What to watch for:** deprecated, no longer available

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-05-29 | May 29, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#May_29_2026) |

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (5)

#### 🔴 5.0.0-okd-scos.ec.0

- **Date:** 2026-05-28
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.0)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver

#### 🔴 4.22.0-okd-scos.2

- **Date:** 2026-06-02
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.2)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver

#### 🔴 5.0.0-okd-scos.ec.1

- **Date:** 2026-06-11
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.1)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver

#### 🔴 4.22.0-okd-scos.3

- **Date:** 2026-06-11
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.3)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver

#### 🟠 4.22.0-okd-scos.1

- **Date:** 2026-05-28
- **Severity:** HIGH
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.1)
- **What to watch for:** authentication, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
