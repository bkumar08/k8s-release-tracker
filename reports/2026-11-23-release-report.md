# Kubernetes Ecosystem — Weekly Releases by Vendor
**Report Period:** Last 7 days (generated November 23, 2026 at 19:41 UTC)

## Weekly Release Summary by Vendor

> **4 breaking change(s) detected** across 8 total releases. Review the sections below for details.
>
> **Qualys Sensor Impact:** 4 release(s) contain changes that may affect sensor connectivity (token/auth, kubeapi, runtime, DaemonSet).

| Vendor | Releases This Week | Breaking Changes | Status |
|--------|-------------------|-----------------|--------|
| Kubernetes (Upstream) | 0 | 0 | No updates |
| Amazon EKS | 4 | 1 (Sensor: 1) | **Action needed** |
| Azure AKS | 0 | 0 | No updates |
| Google GKE | 2 | 1 (Sensor: 1) | **Action needed** |
| Red Hat OpenShift | 2 | 2 (Sensor: 2) | **Action needed** |

---

## Kubernetes (Upstream)

No releases or updates found in this period.

---

## Amazon EKS

### Breaking Changes / Deprecations (1)

#### ⚪ Amazon CloudWatch Observability EKS add-on now supports custom OpenTelemetry and Prometheus telemetry

- **Date:** Fri, 20 No
- **Severity:** INFO
- **Component:** EKS
- **Details:** [View full release notes](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-addon-custom-telemetry/)
- **What to watch for:** CRI
- **Qualys Sensor Impact:** This change may affect sensor connectivity — CRI

### Releases (3)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
| v0.26.5 | 2026-11-18 | — | [View](https://github.com/aws/eks-anywhere/releases/tag/v0.26.5) |
|  | Fri, 20 No | Amazon CloudWatch Observability EKS add-on now supports telemetry filtering | [View](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-otel-addon-filtering/) |
|  | Fri, 20 No | Amazon CloudWatch EKS Container Insights now offers built-in monitoring for open source Kubernetes tools | [View](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-kubernetes-tools/) |

---

## Azure AKS

No releases or updates found in this period.

---

## Google GKE

### Breaking Changes / Deprecations (1)

#### 🔴 November 23, 2026

- **Date:** 2026-11-23
- **Severity:** CRITICAL
- **Component:** GKE
- **Details:** [View full release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#November_23_2026)
- **What to watch for:** deprecated, pod security, pod security admission
- **Qualys Sensor Impact:** This change may affect sensor connectivity — pod security admission

### Releases (1)

| Version | Release Date | Title | Link |
|---------|-------------|-------|------|
|  | 2026-11-18 | November 18, 2026 | [View](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#November_18_2026) |

---

## Red Hat OpenShift

### Breaking Changes / Deprecations (2)

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
