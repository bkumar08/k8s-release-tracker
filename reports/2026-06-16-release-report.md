# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated June 16, 2026 at 12:47 UTC)

## Weekly Release Summary by Vendor

> **7 breaking change(s) detected** across 12 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 4 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 5 | 0 | OK |
| Amazon EKS | 2 | 2 (Sensor: 1) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 2 | 2 | **Action needed** |
| Red Hat OpenShift | 3 | 3 (Sensor: 3) | **Action needed** |

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

#### 🔴 v1.22.2

- **Date:** 2026-06-15
- **Severity:** CRITICAL
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.22.2)
- **What to watch for:** CRI, DaemonSet, CNI, VPC CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

#### 🟠 Amazon EKS now supports local clusters on AWS Outposts with Amazon EC2 instance store

- **Date:** Thu, 11 Ju
- **Severity:** HIGH
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-aws-outposts-ec2-instance-store/)
- **What to watch for:** authentication, OIDC

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (2)

#### 🟠 June 10, 2026

- **Date:** 2026-06-10
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_10_2026)
- **What to watch for:** removed, deprecated, deprecation, will be removed

#### 🟡 June 12, 2026

- **Date:** 2026-06-12
- **Severity:** MEDIUM
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_12_2026)
- **What to watch for:** deprecated, no longer available

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (3)

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

#### 🔴 5.0.0-okd-scos.ec.2

- **Date:** 2026-06-16
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.2)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
