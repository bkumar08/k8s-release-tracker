# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated June 14, 2026 at 10:45 UTC)

## Weekly Release Summary by Vendor

> **6 breaking change(s) detected** across 11 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 3 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 5 | 0 | OK |
| Amazon EKS | 2 | 2 (Sensor: 1) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 2 | 2 | **Action needed** |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

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

#### 🟠 Amazon EKS now supports local clusters on AWS Outposts with Amazon EC2 instance store

- **Date:** Thu, 11 Ju
- **Severity:** HIGH
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-aws-outposts-ec2-instance-store/)
- **What to watch for:** authentication, OIDC

#### ⚪ AWS Backup support for Amazon EKS is now available in the AWS European Sovereign Cloud (Germany) Region

- **Date:** Tue, 09 Ju
- **Severity:** INFO
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-backup-amazon-eks-aws-european-sovereign-cloud/)
- **What to watch for:** CRI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI

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

### Breaking Changes / Deprecations (2)

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

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
