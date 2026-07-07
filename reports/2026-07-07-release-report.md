# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 30 days (generated July 07, 2026 at 01:14 UTC)

## Weekly Release Summary by Vendor

> **25 breaking change(s) detected** across 33 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 20 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 6 | 0 | OK |
| Amazon EKS | 13 | 11 (Sensor: 10) | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 5 | 5 (Sensor: 1) | **Action needed** |
| Red Hat OpenShift | 8 | 8 (Sensor: 8) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (6)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.37.0-alpha.1 | 2026-06-11 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-alpha.1) |
| v1.33.13 | 2026-06-12 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.33.13) |
| v1.34.9 | 2026-06-12 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.34.9) |
| v1.35.6 | 2026-06-12 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.6) |
| v1.36.2 | 2026-06-12 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.2) |
| v1.37.0-alpha.2 | 2026-06-25 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0-alpha.2) |

---

## Amazon EKS

### Breaking Changes / Deprecations (11)

#### 🔴 v1.22.2

- **Date:** 2026-06-15
- **Severity:** CRITICAL
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.22.2)
- **What to watch for:** CRI, DaemonSet, CNI, VPC CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

#### 🔴 AWS Network Firewall now supports container attribute-based inspection for Amazon EKS and Amazon ECS

- **Date:** Tue, 30 Ju
- **Severity:** CRITICAL
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-container-attributes-referencing)
- **What to watch for:** TLS

#### 🟠 EKS Distro v1-30-eks-56 Release (v1-30-eks-56)

- **Date:** 2026-06-22
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-30-eks-56)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-31-eks-45 Release (v1-31-eks-45)

- **Date:** 2026-06-22
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-31-eks-45)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-32-eks-38 Release (v1-32-eks-38)

- **Date:** 2026-06-22
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-32-eks-38)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-33-eks-28 Release (v1-33-eks-28)

- **Date:** 2026-06-22
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-33-eks-28)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-34-eks-19 Release (v1-34-eks-19)

- **Date:** 2026-06-22
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-34-eks-19)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-35-eks-10 Release (v1-35-eks-10)

- **Date:** 2026-06-22
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-35-eks-10)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-36-eks-3 Release (v1-36-eks-3)

- **Date:** 2026-06-22
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-36-eks-3)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-36-eks-4 Release (v1-36-eks-4)

- **Date:** 2026-06-24
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-36-eks-4)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟡 v1.22.3

- **Date:** 2026-07-06
- **Severity:** MEDIUM
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.22.3)
- **What to watch for:** CRI, DaemonSet, CNI, VPC CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

### Releases (2)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Tue, 23 Ju | Amazon CloudWatch launches OTel Container Insights for Amazon EKS | [View](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-otel-amazon-eks/) |
|  | Wed, 01 Ju | Amazon EKS now supports Kubernetes version rollback | [View](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-version-rollback) |

---

## Azure AKS

### Breaking Changes / Deprecations (1)

#### 🔴 Release - 2026-06-19 (2026-06-19)

- **Date:** 2026-06-25
- **Severity:** CRITICAL
- **Component:** AKS
- **Details:** [View full release notes](https://github.com/Azure/AKS/releases/tag/2026-06-19)
- **What to watch for:** DaemonSet, privileged, not supported, CoreDNS, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, privileged, not supported

---

## Google GKE

### Breaking Changes / Deprecations (5)

#### 🟠 June 10, 2026

- **Date:** 2026-06-10
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_10_2026)
- **What to watch for:** removed, deprecated, deprecation, will be removed

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

#### 🟡 June 12, 2026

- **Date:** 2026-06-12
- **Severity:** MEDIUM
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_12_2026)
- **What to watch for:** deprecated, no longer available

#### ⚪ June 23, 2026

- **Date:** 2026-06-23
- **Severity:** INFO
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#June_23_2026)
- **What to watch for:** mount, fuse, network policy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — mount, fuse

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (8)

#### 🔴 5.0.0-okd-scos.ec.1

- **Date:** 2026-06-11
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.1)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 4.22.0-okd-scos.3

- **Date:** 2026-06-11
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.3)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.ec.2

- **Date:** 2026-06-16
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.2)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 4.22.0-okd-scos.4

- **Date:** 2026-06-18
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.4)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.ec.3

- **Date:** 2026-06-23
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.3)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 4.22.0-okd-scos.5

- **Date:** 2026-06-23
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.5)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 4.22.0-okd-scos.6

- **Date:** 2026-06-29
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.6)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.ec.4

- **Date:** 2026-06-29
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.4)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
