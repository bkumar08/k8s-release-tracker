# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated November 13, 2026 at 15:48 UTC)

## Weekly Release Summary by Vendor

> **11 breaking change(s) detected** across 13 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 7 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 8 | 6 (Sensor: 4) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 3 | 3 (Sensor: 1) | **Action needed** |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (6)

#### 🔴 v1.23.3

- **Date:** 2026-11-10
- **Severity:** CRITICAL
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.23.3)
- **What to watch for:** CRI, DaemonSet, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

#### 🔴 v0.25.6

- **Date:** 2026-11-11
- **Severity:** CRITICAL
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.25.6)
- **What to watch for:** not supported
- **Qualys Sensor Impact:** This change may affect sensor connectivity — not supported

#### 🟠 v0.27.0

- **Date:** 2026-11-12
- **Severity:** HIGH
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.27.0)
- **What to watch for:** CRI, not supported
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI, not supported

#### 🟠 Amazon EKS Provisioned Control Plane now offers a 24 GB etcd database on 4XL and 8XL tiers

- **Date:** Wed, 11 No
- **Severity:** HIGH
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-provisioned-control-plane-larger-etcd-database/)
- **What to watch for:** action required, ACTION REQUIRED

<details>
<summary>Click to see breaking change details</summary>

```
Amazon Elastic Kubernetes Service (Amazon EKS) now offers a larger 24 GB etcd database, up from 16 GB, for 4XL and 8XL Provisioned Control Plane clusters. etcd is the key-value store in the Kubernetes control plane that holds your cluster state, so its size limits how many Kubernetes objects your cluster can store. With 50% more capacity, you can run bigger clusters with more pods, jobs, events, and custom resources. 
The larger database gives more headroom to workloads that create and update many Kubernetes objects, such as large-scale AI/ML training and inference, batch processing, and CI/CD pipelines. When the etcd database fills up, you can’t add or change objects in your cluster, so the extra headroom helps keep these workloads running as they scale. 
To get the larger database,&nbsp;
```

</details>

#### 🔵 Amazon EKS Auto Mode and Karpenter now support Dynamic Resource Allocation

- **Date:** Mon, 09 No
- **Severity:** LOW
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-auto-mode-karpenter-dra/)
- **What to watch for:** CRI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI

#### ⚪ Introducing AWS Nitro Sandboxes on Amazon EKS, ECS and EC2 for hardware isolated pods, tasks and VMs

- **Date:** Mon, 09 No
- **Severity:** INFO
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/11/nitro-sandboxes-eks-ecs-ec2/)
- **What to watch for:** CNI, VPC CNI

### Releases (2)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Wed, 11 No | Amazon EKS Auto Mode now supports security groups for Pods | [View](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-auto-mode-security-groups-for-pods/) |
|  | Thu, 12 No | AWS Backup now supports resource modifiers for Amazon EKS restores | [View](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-backup-resource-modifiers-eks/) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (3)

#### 🟠 November 10, 2026

- **Date:** 2026-11-10
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#November_10_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

#### ⚪ November 11, 2026

- **Date:** 2026-11-11
- **Severity:** INFO
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#November_11_2026)
- **What to watch for:** mount, fuse
- **Qualys Sensor Impact:** This change may affect sensor connectivity — mount, fuse

#### ⚪ November 12, 2026

- **Date:** 2026-11-12
- **Severity:** INFO
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#November_12_2026)
- **What to watch for:** CNI

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

#### 🔴 5.1.0-okd-scos.ec.3

- **Date:** 2026-11-09
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.1.0-okd-scos.ec.3)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.6

- **Date:** 2026-11-09
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.6)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
