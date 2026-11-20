# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated November 20, 2026 at 16:31 UTC)

## Weekly Release Summary by Vendor

> **7 breaking change(s) detected** across 10 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 6 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 4 | 2 (Sensor: 1) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 1 | 0 | OK |
| Red Hat OpenShift | 5 | 5 (Sensor: 5) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (2)

#### 🔴 Amazon VPC Flow Logs now supports Amazon EKS metadata

- **Date:** Thu, 19 No
- **Severity:** CRITICAL
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-vpc-flow-logs-amazon-eks-metadata/)
- **What to watch for:** CNI, VPC CNI

#### 🔴 Amazon SageMaker HyperPod now supports higher pod density on EKS-orchestrated clusters

- **Date:** Wed, 18 No
- **Severity:** CRITICAL
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-higher-pod-density/)
- **What to watch for:** DaemonSet, CNI, VPC CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet

### Releases (2)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v0.26.5 | 2026-11-18 | — | [View](https://github.com/aws/eks-anywhere/releases/tag/v0.26.5) |
|  | Wed, 18 No | Amazon EKS Hybrid Nodes reduces price for large hosts | [View](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-hybrid-nodes-pricing-change/) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-11-18 | November 18, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#November_18_2026) |

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (5)

#### 🔴 5.1.0-okd-scos.ec.4

- **Date:** 2026-11-14
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.1.0-okd-scos.ec.4)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.7

- **Date:** 2026-11-14
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.7)
- **What to watch for:** authentication, 401, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.1.0-okd-scos.ec.5

- **Date:** 2026-11-16
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.1.0-okd-scos.ec.5)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.8

- **Date:** 2026-11-19
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.8)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🟠 5.1.0-okd-scos.ec.6

- **Date:** 2026-11-19
- **Severity:** HIGH
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.1.0-okd-scos.ec.6)
- **What to watch for:** authentication, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
