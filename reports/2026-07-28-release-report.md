# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated July 28, 2026 at 10:26 UTC)

## Weekly Release Summary by Vendor

> **13 breaking change(s) detected** across 17 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 12 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 3 | 0 | OK |
| Amazon EKS | 10 | 10 (Sensor: 10) | **Action needed** |
| Azure AKS | 1 | 1 (Sensor: 1) | **Action needed** |
| Google GKE | 2 | 1 | **Action needed** |
| Red Hat OpenShift | 1 | 1 (Sensor: 1) | **Action needed** |

---

## Kubernetes (Upstream)

**No breaking changes in this period.**

### Releases (3)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v1.34.10 | 2026-07-22 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.34.10) |
| v1.35.7 | 2026-07-22 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.7) |
| v1.36.3 | 2026-07-23 | — | [View](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.3) |

---

## Amazon EKS

### Breaking Changes / Deprecations (10)

#### 🔴 Amazon EKS now supports EFA and placement groups on Amazon EKS Auto Mode and Karpenter

- **Date:** Wed, 22 Ju
- **Severity:** CRITICAL
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-efa-placement-groups/)
- **What to watch for:** CRI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI

#### 🟠 v0.25.3

- **Date:** 2026-07-23
- **Severity:** HIGH
- **Component:** EKS (eks-anywhere)
- **Details:** [View full release notes](https://github.com/aws/eks-anywhere/releases/tag/v0.25.3)
- **What to watch for:** containerd, DaemonSet, not supported
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, containerd, not supported

#### 🟠 EKS Distro v1-31-eks-47 Release (v1-31-eks-47)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-31-eks-47)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-30-eks-58 Release (v1-30-eks-58)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-30-eks-58)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-32-eks-40 Release (v1-32-eks-40)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-32-eks-40)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-33-eks-30 Release (v1-33-eks-30)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-33-eks-30)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-34-eks-21 Release (v1-34-eks-21)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-34-eks-21)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-35-eks-12 Release (v1-35-eks-12)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-35-eks-12)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟠 EKS Distro v1-36-eks-6 Release (v1-36-eks-6)

- **Date:** 2026-07-27
- **Severity:** HIGH
- **Component:** EKS (eks-distro)
- **Details:** [View full release notes](https://github.com/aws/eks-distro/releases/tag/v1-36-eks-6)
- **What to watch for:** kube-apiserver, CoreDNS, kube-proxy
- **Qualys Sensor Impact:** This change may affect sensor connectivity — kube-apiserver

#### 🟡 v1.22.4

- **Date:** 2026-07-22
- **Severity:** MEDIUM
- **Component:** EKS (amazon-vpc-cni-k8s)
- **Details:** [View full release notes](https://github.com/aws/amazon-vpc-cni-k8s/releases/tag/v1.22.4)
- **What to watch for:** CRI, DaemonSet, network policy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — DaemonSet, CRI

---

## Azure AKS

### Breaking Changes / Deprecations (1)

#### 🔴 Release 2026-07-17 (2026-07-17)

- **Date:** 2026-07-24
- **Severity:** CRITICAL
- **Component:** AKS
- **Details:** [View full release notes](https://github.com/Azure/AKS/releases/tag/2026-07-17)
- **What to watch for:** deprecated, action required, ACTION REQUIRED, TLS, containerd, overlay, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — containerd, overlay

<details>
<summary>Click to see breaking change details</summary>

```
## Release Notes - 2026-07-17

> Monitor the release status by regions at [AKS-Release-Tracker](https://releases.aks.azure.com/). This release is titled `v20260717`.

### Announcements of upcoming changes and retirements

* On September 14, 2026, [the preview property enableCustomCATrust will retire](https://github.com/Azure/AKS/issues/5826). After that date, the `enableCustomCATrust=true` node pool level field will no longer enable [Custom Certificate Authority (CA)](https://aka.ms/aks/custom-certificate-authority). To avoid failures during scaling and certificate updates, update the impacted clusters and node pools and remove the preview property (`--disable-custom-ca-trust`).
* AKS no longer supports creating node pools with Windows Server Annual Channel for Containers. Existing 
```

</details>

---

## Google GKE

### Breaking Changes / Deprecations (1)

#### 🟠 July 24, 2026

- **Date:** 2026-07-24
- **Severity:** HIGH
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_24_2026)
- **What to watch for:** removed, deprecated, removed in, will be removed, no longer available

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-07-27 | July 27, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#July_27_2026) |

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (1)

#### 🔴 5.0.0-okd-scos.ec.6

- **Date:** 2026-07-27
- **Severity:** CRITICAL
- **Component:** OpenShift (okd)
- **Details:** [View full release notes](https://github.com/okd-project/okd/releases/tag/5.0.0-okd-scos.ec.6)
- **What to watch for:** authentication, 401, 403, kube-apiserver, RBAC, snapshot, snapshotter, CoreDNS, kube-proxy, CNI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — 401, kube-apiserver, snapshotter

---

*This report is auto-generated daily by [k8s-release-tracker](https://github.com/bkumar08/k8s-release-tracker). Breaking changes are detected via keyword matching in release notes.*
