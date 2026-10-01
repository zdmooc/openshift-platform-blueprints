# OpenShift Platform Blueprints

**Canonical role:** OpenShift Architecture / Knowledge / Standards Reference  
**Portfolio status:** KEEP / REFERENCE / ACTIVE CLEANUP  
**Last governance review:** 2026-10-01

This repository is the OpenShift architecture and standards reference of the MayaBank portfolio. It connects platform architecture, reusable reference blueprints and structured OpenShift learning material without pretending to own every runtime capability.

## What this repository owns

- OpenShift platform architecture and governance;
- namespace/project tenancy patterns;
- ResourceQuota / LimitRange standards;
- RBAC, SCC and Pod Security architecture;
- NetworkPolicy patterns;
- workload reliability patterns: probes, PDB, HPA, requests/limits;
- Routes/Ingress and service exposure;
- storage/CSI/ODF reference concepts;
- Operators / OLM;
- GitOps architecture and small validated Argo CD examples;
- observability/SRE architecture and ServiceMonitor examples;
- multi-cluster / ACM reference architecture;
- OpenShift certification learning tracks.

## What it does not own

| Capability | Canonical repository |
|---|---|
| Cluster provisioning, lifecycle, upgrades, N2/N3 | `zdmooc/k8s-openshift-cluster-factory` |
| Shared platform runtime services | `zdmooc/shared-platform-services-openshift` |
| Argo CD deep expertise and runtime labs | `zdmooc/argocd-expert-pack` |
| Keycloak deep expertise and runtime labs | `zdmooc/keycloak-enterprise-roadmap-v7` |
| Workload migration assessment and execution patterns | `zdmooc/openshift-migration-framework` |
| Kubernetes internals / manual bootstrap | `zdmooc/kubernetes-the-hard-way-vagrant-architect-v29` |
| Multi-cloud KTHW provider adapters | `zdmooc/kubernetes-the-hard-way-multicloud` |
| WebSphere -> OpenShift assessment | `zdmooc/assessment-was-openshift` |

## Repository structure

```text
architecture/       platform views and reference architectures
docs/
  governance/       scope, ownership and claim model
  reference/        OpenShift reference knowledge
platform/           small reference manifests and GitOps examples
certifications/     EX280 / EX288 / EX370 / EX380 / EX480 / EX482 tracks
evidence/           validation and claim/evidence information
.github/workflows/  repository validation
```

## Recommended reading path

1. `docs/governance/REPOSITORY_SCOPE.md`
2. `architecture/overview/platform-overview.md`
3. `architecture/reference-architectures/`
4. `docs/reference/openshift/`
5. `platform/` for validated examples
6. `certifications/` for learning tracks

## Portfolio layering

```text
openshift-platform-blueprints
        Architecture / standards
                 |
                 v
k8s-openshift-cluster-factory
        Cluster lifecycle / CaaS
                 |
                 v
shared-platform-services-openshift
        Shared platform capabilities
                 |
                 v
Specialized platforms
        Data / MQ / Kafka / AI
                 |
                 v
Business products
        Payments / Cards / etc.
```

## Evidence model

Every claim must use one of the following levels:

`REFERENCE | IMPLEMENTED | STATIC_VALIDATED | CI_RUNTIME_PROVEN | CRC_RUNTIME_PROVEN | MULTINODE_PROVEN | PRODUCTION_REFERENCE | STALE_REQUALIFICATION_REQUIRED`.

See `docs/governance/ASSET_STATUS_MODEL.md`.

A manifest committed to Git is not automatically a deployable or runtime-proven asset.

## Executable examples

The `platform/` directory contains **small reference examples**, not a competing common platform implementation. Repository CI validates their syntax/rendering where possible.

Operational implementations belong to their canonical repositories.

## Certification tracks

The learning area currently covers:

- EX280 — OpenShift Administration;
- EX288 — application development;
- EX370 — OpenShift Data Foundation / storage;
- EX380 — automation, identity, backup, monitoring and GitOps topics;
- EX480 — multi-cluster management/governance;
- EX482 — event-driven / Kafka-related learning.

Certification material is explicitly a **learning/reference asset**. It is not a certification claim.

## Principles

1. One canonical owner per capability.
2. Architecture here; operational implementation in the owning repository.
3. Reuse links/contracts instead of copying whole platforms.
4. No real credentials or customer data.
5. Validation status must match evidence.
6. Small executable examples are kept only when they clarify a platform standard.

## Current cleanup program

The 2026-10-01 O1 cleanup performs:

- repository scope and ownership clarification;
- YAML/GitOps repair;
- architecture/reference normalization;
- cross-repository boundaries;
- automated validation;
- certification-track normalization;
- final evidence/index baseline.

The governing portfolio decision is documented in `zdmooc/cadrage_202682030`, decision D-075.

## Author

**Zidane Djamal**  
Architecture technique / plateforme / cloud-native  
OpenShift · Kubernetes · GitOps · Security · Observability · Platform Engineering
