# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated July 02, 2026 at 10:30 UTC)

## Weekly Release Summary by Vendor

> **6 breaking change(s) detected** across 7 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 3 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 2 | 1 | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 2 | 2 | **Action needed** |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

#### 🔴 AWS Network Firewall now supports container attribute-based inspection for Amazon EKS and Amazon ECS

- **Date:** Tue, 30 Ju
- **Severity:** CRITICAL
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-container-attributes-referencing)
- **What to watch for:** TLS

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Wed, 01 Ju | Amazon EKS now supports Kubernetes version rollback | [View](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-version-rollback) |

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
