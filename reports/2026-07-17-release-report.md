# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated July 17, 2026 at 09:49 UTC)

## Weekly Release Summary by Vendor

> **10 breaking change(s) detected** across 13 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 9 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 9 | 7 (Sensor: 7) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 2 | 1 | **Action needed** |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (7)

#### 🟠 EKS Distro v1-36-eks-5 Release (v1-36-eks-5)

- **Date:** 2026-07-10
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-36-eks-5)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-30-eks-57 Release (v1-30-eks-57)

- **Date:** 2026-07-10
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-30-eks-57)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-31-eks-46 Release (v1-31-eks-46)

- **Date:** 2026-07-10
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-31-eks-46)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-32-eks-39 Release (v1-32-eks-39)

- **Date:** 2026-07-10
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-32-eks-39)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-33-eks-29 Release (v1-33-eks-29)

- **Date:** 2026-07-10
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-33-eks-29)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-34-eks-20 Release (v1-34-eks-20)

- **Date:** 2026-07-10
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-34-eks-20)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-35-eks-11 Release (v1-35-eks-11)

- **Date:** 2026-07-10
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-35-eks-11)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

### Releases (2)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Fri, 10 Ju | Amazon EKS Auto Mode now supports Application Recovery Controller zonal shift | [View](https://aws.amazon.com/about-aws/whats-new/2026/07/eks-auto-mode-arc-zonal-shift) |
|  | Fri, 10 Ju | Amazon EMR on EKS now supports Apache Spark troubleshooting agent | [View](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-emr-eks-spark-troubleshooting/) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (1)

#### ⚪ July 14, 2026

- **Date:** 2026-07-14
- **Severity:** INFO
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_14_2026)
- **What to watch for:** incompatible, CNI

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-07-16 | July 16, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_16_2026) |

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

#### 🔴 4.22.0-okd-scos.7

- **Date:** 2026-07-13
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/4.22.0-okd-scos.7)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.ec.5

- **Date:** 2026-07-13
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.5)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
