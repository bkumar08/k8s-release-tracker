# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated October 26, 2026 at 14:42 UTC)

## Weekly Release Summary by Vendor

> **4 breaking change(s) detected** across 4 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 3 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 1 | 1 | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 1 | 1 (Sensor: 1) | **Action needed** |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

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

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (1)

#### 🔴 October 20, 2026

- **Date:** 2026-10-20
- **Severity:** CRITICAL
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_20_2026)
- **What to watch for:** Unauthorized, containerd, fuse
- **Qualys Sensor Impact:** This change may affect sensor connectivity — Unauthorized, containerd, fuse

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

#### 🔴 5.0.0-okd-scos.3

- **Date:** 2026-10-21
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.3)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

#### 🟠 5.1.0-okd-scos.ec.0

- **Date:** 2026-10-21
- **Severity:** HIGH
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.1.0-okd-scos.ec.0)
- **What to watch for:** authentication, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
