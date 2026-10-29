# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated October 29, 2026 at 14:49 UTC)

## Weekly Release Summary by Vendor

> **15 breaking change(s) detected** across 21 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 10 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 5 | 0 | OK |
| Amazon EKS | 11 | 10 (Sensor: 7) | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 2 | 2 | **Action needed** |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (5)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.35.10 | 2026-10-28 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.10) |
| v1.34.13 | 2026-10-28 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.34.13) |
| v1.37.2 | 2026-10-28 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.2) |
| v1.36.6 | 2026-10-28 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.6) |
| v1.38.0-alpha.3 | 2026-10-28 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.38.0-alpha.3) |

---

## Amazon EKS

### Breaking Changes / Deprecations (10)

#### 🔴 v0.26.4

- **Date:** 2026-10-28
- **Severity:** CRITICAL
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.26.4)
- **What to watch for:** removed

#### 🟠 EKS Distro v1-31-eks-51 Release (v1-31-eks-51)

- **Date:** 2026-10-28
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-31-eks-51)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-32-eks-44 Release (v1-32-eks-44)

- **Date:** 2026-10-28
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-32-eks-44)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-33-eks-34 Release (v1-33-eks-34)

- **Date:** 2026-10-28
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-33-eks-34)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-34-eks-25 Release (v1-34-eks-25)

- **Date:** 2026-10-28
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-34-eks-25)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-35-eks-16 Release (v1-35-eks-16)

- **Date:** 2026-10-28
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-35-eks-16)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-36-eks-10 Release (v1-36-eks-10)

- **Date:** 2026-10-28
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-36-eks-10)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-37-eks-4 Release (v1-37-eks-4)

- **Date:** 2026-10-28
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-37-eks-4)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 Amazon EMR on EKS reduces EMR charge by 30 percent

- **Date:** Fri, 23 Oc
- **Severity:** HIGH
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/10/emr-eks-reduces-emr-charge-30-percent/)
- **What to watch for:** action required, ACTION REQUIRED

<details>
<summary>Click to see breaking change details</summary>

```
Amazon EMR announces a reduction of 30 percent in the EMR charge added to EKS when running EMR on EKS. This price decrease applies to both the per-vCPU-hour charge and the per-GB-hour charge, while the underlying Amazon EKS charges remain unchanged. All EMR workloads running on the EKS deployment option benefit from this change. Now, you can run Apache Spark workloads on Amazon Elastic Kubernetes Service (EKS) at a lower cost, and the new price automatically applies to your EMR on EKS workloads with no additional action required on your end.
The 30% reduction in EMR on EKS pricing is available in all AWS Regions where Amazon EMR on EKS is available. To learn more about EMR on EKS, visit the Amazon EMR on EKS documentation and the Amazon EMR pricing page.
```

</details>

#### ⚪ Amazon EKS Auto Mode now supports Kubernetes Gateway API

- **Date:** Wed, 28 Oc
- **Severity:** INFO
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-auto-mode-kubernetes-gateway-api/)
- **What to watch for:** TLS

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | Wed, 28 Oc | Amazon EKS Dashboard now provides fleet-wide visibility into certificate authority (CA) rotation | [View](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-dashboard-fleet-wide-visibility-certificate-authority-ca-rotation/) |

---

## Azure AKS

### Breaking Changes / Deprecations (1)

#### 🔴 Release 2026-10-25 (2026-10-25)

- **Date:** 2026-10-27
- **Severity:** CRITICAL
- **Component:** AKS
- **Details:** [View full release notes](https://github.com/Azure/AKS/releases/tag/2026-10-25)
- **What to watch for:** kube-apiserver, seccomp, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver, seccomp

---

## Google GKE

### Breaking Changes / Deprecations (2)

#### 🟠 October 26, 2026

- **Date:** 2026-10-26
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_26_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

#### 🟠 October 27, 2026

- **Date:** 2026-10-27
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_27_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

#### 🔴 5.1.0-okd-scos.ec.1

- **Date:** 2026-10-28
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.1.0-okd-scos.ec.1)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🔴 5.0.0-okd-scos.4

- **Date:** 2026-10-28
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.4)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
