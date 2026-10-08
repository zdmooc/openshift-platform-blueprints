# OpenShift Platform Blueprints

**Canonical role:** OpenShift Architecture / Knowledge / Standards Reference  
**Portfolio status:** KEEP / REFERENCE / STATIC_VALIDATED  
**Last governance review:** 2026-10-08 — D-098 + certification-track closure

This repository is the OpenShift architecture and standards reference of the MayaBank portfolio. It connects platform architecture, reusable reference blueprints and structured OpenShift learning material without pretending to own every runtime capability.

## D-098 — SQY mission reference overlay

For the IT-EXPLORER SQY Expert Kubernetes/OpenShift mission, this repository supplies the
**OpenShift architecture and standards layer**.

Mission-specific reference:
- `architecture/reference-architectures/d098-sqy-caas-onprem.md`.

The operational CaaS/lifecycle owner remains `k8s-openshift-cluster-factory`.
The Data Lakehouse remains a workload proof and is not reclassified as the CaaS core.

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

- **EX280** — primary OpenShift administration preparation; repository track complete;
- **EX380** — primary advanced administration/automation preparation; repository track complete;
- **EX288** — mature complementary application-development track;
- **EX370** — complementary OpenShift Data Foundation/storage track, runtime environment-dependent;
- **EX480** — lightweight multi-cluster/governance reference;
- **EX482** — lightweight event-driven/Kafka reference.

Certification material is explicitly a **learning/reference asset**. Repository preparation completion is not an official certification claim. The certification area is structurally validated in CI.

## Principles

1. One canonical owner per capability.
2. Architecture here; operational implementation in the owning repository.
3. Reuse links/contracts instead of copying whole platforms.
4. No real credentials or customer data.
5. Validation status must match evidence.
6. Small executable examples are kept only when they clarify a platform standard.

## O1 cleanup baseline

The 2026-10-01 O1 cleanup is **complete (I1→I7)**.

The active platform reference surface passed the `Reference Validation` workflow, including YAML parsing, yamllint, Kustomize rendering and kubeconform. First complete successful validation: run `36854282558`.

This proves `STATIC_VALIDATED` reference assets only. It does not claim CRC runtime, multi-node resilience or production deployment.

Completion record: `docs/governance/O1_CLEANUP_COMPLETION.md`.

The governing portfolio decision is documented in `zdmooc/cadrage_202682030`, decision D-075.

## Author

**Zidane Djamal**  
Architecture technique / plateforme / cloud-native  
OpenShift · Kubernetes · GitOps · Security · Observability · Platform Engineering
