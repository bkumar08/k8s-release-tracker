# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated September 12, 2026 at 11:49 UTC)

## Weekly Release Summary by Vendor

> **5 breaking change(s) detected** across 6 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 3 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 3 | 2 (Sensor: 1) | **Action needed** |
| Azure AKS | 1 | 1 | **Action needed** |
| Google GKE | 0 | 0 | No updates |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (2)

#### 🔴 AWS Private CA EKS add-on and Connector for AD now available in AWS GovCloud (US)

- **Date:** Wed, 09 Se
- **Severity:** CRITICAL
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/09/private-ca-eks-addon-ad-govcloud/)
- **What to watch for:** authentication, TLS

#### 🟡 v1.23.1

- **Date:** 2026-09-11
- **Severity:** MEDIUM
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.23.1)
- **What to watch for:** CRI, DaemonSet, network policy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v0.26.2 | 2026-09-10 | — | [View](https://github.com/aws/eks-anywhere/releases/tag/v0.26.2) |

---

## Azure AKS

### Breaking Changes / Deprecations (1)

#### 🔴 Release 2026-09-04 (2026-09-04)

- **Date:** 2026-09-09
- **Severity:** CRITICAL
- **Component:** AKS
- **Details:** [View full release notes](https://github.com/Azure/AKS/releases/tag/2026-09-04)
- **What to watch for:** deprecated, authentication, network policy, CNI

---

## Google GKE

No releases or updates found in this period.

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

#### 🔴 5.0.0-okd-scos.ec.9

- **Date:** 2026-09-09
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.9)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.ec.10

- **Date:** 2026-09-11
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.10)
- **What to watch for:** authentication, 401, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
