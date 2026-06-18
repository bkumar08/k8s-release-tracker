# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated June 18, 2026 at 11:45 UTC)

## Weekly Release Summary by Vendor

> **5 breaking change(s) detected** across 9 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 3 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 4 | 0 | OK |
| Amazon EKS | 2 | 2 (Sensor: 1) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 1 | 1 | **Action needed** |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (4)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
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

### Breaking Changes / Deprecations (1)

#### 🟡 June 12, 2026

- **Date:** 2026-06-12
- **Severity:** MEDIUM
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_12_2026)
- **What to watch for:** deprecated, no longer available

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

#### 🔴 5.0.0-okd-scos.ec.2

- **Date:** 2026-06-16
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.2)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver

#### 🔴 4.22.0-okd-scos.4

- **Date:** 2026-06-18
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.4)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
