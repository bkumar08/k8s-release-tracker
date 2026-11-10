# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated November 10, 2026 at 15:57 UTC)

## Weekly Release Summary by Vendor

> **7 breaking change(s) detected** across 8 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 6 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 1 | 0 | OK |
| Amazon EKS | 3 | 3 (Sensor: 2) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 0 | 0 | No updates |
| Red Hat OpenShift | 4 | 4 (Sensor: 4) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.38.0-beta.0 | 2026-11-06 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.38.0-beta.0) |

---

## Amazon EKS

### Breaking Changes / Deprecations (3)

#### 🔴  (v0.25.5)

- **Date:** 2026-11-06
- **Severity:** CRITICAL
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.25.5)
- **What to watch for:** removed, not supported
- **Qualys Sensor Impact:** This change may affect sensor connectivity — not supported

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

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

No releases or updates found in this period.

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (4)

#### 🔴 5.1.0-okd-scos.ec.2

- **Date:** 2026-11-05
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.1.0-okd-scos.ec.2)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.5

- **Date:** 2026-11-05
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.5)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

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
