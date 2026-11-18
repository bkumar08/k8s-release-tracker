# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated November 18, 2026 at 16:50 UTC)

## Weekly Release Summary by Vendor

> **7 breaking change(s) detected** across 8 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 5 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 3 | 2 (Sensor: 2) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 2 | 2 | **Action needed** |
| Red Hat OpenShift | 3 | 3 (Sensor: 3) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (2)

#### 🔴 AWS Batch on Amazon EKS adds Linux capabilities, seccomp, and pod-level settings

- **Date:** Fri, 13 No
- **Severity:** CRITICAL
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/)
- **What to watch for:** pod security, security context, seccomp
- **Qualys Sensor Impact:** This change may affect sensor connectivity — seccomp

#### 🟠 v0.27.0

- **Date:** 2026-11-12
- **Severity:** HIGH
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.27.0)
- **What to watch for:** CRI, not supported
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI, not supported

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Tue, 17 No | Amazon EKS Auto Mode now rightsizes Pods to reduce compute costs (Preview) | [View](https://aws.amazon.com/about-aws/whats-new/2026/11/eks-auto-mode-pod-rightsizing-preview/) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (2)

#### 🔴 November 13, 2026

- **Date:** 2026-11-13
- **Severity:** CRITICAL
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#November_13_2026)
- **What to watch for:** deprecated, no longer available

#### ⚪ November 12, 2026

- **Date:** 2026-11-12
- **Severity:** INFO
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#November_12_2026)
- **What to watch for:** CNI

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (3)

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

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
