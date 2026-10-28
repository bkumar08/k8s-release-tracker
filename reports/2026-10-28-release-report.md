# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated October 28, 2026 at 14:43 UTC)

## Weekly Release Summary by Vendor

> **5 breaking change(s) detected** across 10 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 1 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 5 | 0 | OK |
| Amazon EKS | 2 | 2 | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 2 | 2 | **Action needed** |
| Red Hat OpenShift | 0 | 0 | No updates |

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

### Breaking Changes / Deprecations (2)

#### 🔴 v0.26.4

- **Date:** 2026-10-28
- **Severity:** CRITICAL
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.26.4)
- **What to watch for:** removed

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

No releases or updates found in this period.

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
