# Repository Scope — OpenShift Platform Blueprints

**Status:** REFERENCE / KNOWLEDGE / STANDARDS  
**Date:** 2026-10-01

## Mission

This repository is the canonical OpenShift architecture, knowledge and standards reference of the MayaBank portfolio.

It explains **what a well-structured OpenShift platform should look like**, the architectural principles behind it, the reusable standards expected from workloads and platform teams, and the learning material used to deepen OpenShift expertise.

It is not the canonical owner of cluster provisioning, shared platform runtime services, Argo CD expertise, Keycloak expertise or application migration execution.

## Owned here

- OpenShift architecture principles;
- projects/namespaces and tenancy patterns;
- ResourceQuota / LimitRange standards;
- RBAC and SCC / Pod Security concepts;
- NetworkPolicy baseline patterns;
- workload reliability patterns: probes, PDB, HPA, requests/limits;
- Routes/Ingress and service exposure architecture;
- Operators / OLM architecture;
- GitOps architecture and integration contracts;
- observability architecture and ServiceMonitor examples;
- storage/CSI/ODF reference concepts;
- multi-cluster / ACM reference concepts;
- platform governance, SRE and Day-2 architectural principles;
- OpenShift certification learning tracks.

## Not owned here

| Capability | Canonical repository |
|---|---|
| Cluster provisioning / lifecycle / upgrade / N2-N3 | `zdmooc/k8s-openshift-cluster-factory` |
| Shared GitOps/IAM/observability/quality runtime | `zdmooc/shared-platform-services-openshift` |
| Argo CD deep-dive labs and runtime evidence | `zdmooc/argocd-expert-pack` |
| Keycloak deep-dive / IAM labs and runtime evidence | `zdmooc/keycloak-enterprise-roadmap-v7` |
| Workload migration assessment and waves | `zdmooc/openshift-migration-framework` |
| Kubernetes internals / manual bootstrap | `zdmooc/kubernetes-the-hard-way-vagrant-architect-v29` |
| Provider portability / KTHW Terraform | `zdmooc/kubernetes-the-hard-way-multicloud` |
| WebSphere -> OpenShift assessment | `zdmooc/assessment-was-openshift` |

## Repository zones

```text
architecture/     architecture views and reference architectures
docs/             reference knowledge, governance and standards
platform/         small validated reference examples only
certifications/   learning tracks and certification labs
evidence/         claim/evidence registry for this repository
.github/          validation automation
```

## Rule

A platform asset is kept here only if it is a **small reference blueprint** supporting the architecture.

A complete operational implementation belongs in the repository that owns that capability.

## Dependency classification

Every dependency referenced by a blueprint should be interpreted using one of:

`CONSUME_SHARED | DEDICATED_FOR_TEST | SPECIALIZED_PLATFORM | PRODUCT_OWNED | REFERENCE_ONLY`.

## Truth boundary

The presence of an architecture document or manifest does not imply runtime validation. Claims must use the evidence levels defined in `ASSET_STATUS_MODEL.md`.
