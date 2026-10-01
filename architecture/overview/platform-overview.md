# OpenShift Platform Overview

**Status:** REFERENCE  
**Date:** 2026-10-01

## Purpose

This document is the architectural entry point for `openshift-platform-blueprints`.

The repository describes OpenShift platform architecture and standards. It does not claim to be the runtime implementation of every platform capability.

## Target layering

```text
L0  Infrastructure
    compute / network / DNS / LB / firewall / storage / backup / PKI
          |
L1  OpenShift / Kubernetes execution platform
    cluster / nodes / CNI / CSI / ingress-route / operators / lifecycle
          |
L2  Shared platform services
    GitOps / identity integration / observability / quality / policy / secrets
          |
L3  Shared technical platforms
    Kafka / IBM MQ / databases / S3 / API management / MFT
          |
L4  Specialized platforms
    Data / AI / Decision / Integration
          |
L5  Business products
    Payments / Cards / Customer / Claims / other products
```

## Canonical repository ownership

- **Architecture / standards:** this repository.
- **Cluster lifecycle / CaaS / Day-2:** `k8s-openshift-cluster-factory`.
- **Shared platform runtime:** `shared-platform-services-openshift`.
- **Argo CD expertise:** `argocd-expert-pack`.
- **Keycloak expertise:** `keycloak-enterprise-roadmap-v7`.
- **Migration:** `openshift-migration-framework`.

## Architecture domains covered here

### Platform core
Projects/namespaces, workload primitives, scheduling concepts, operators/OLM, Routes/Ingress, cluster services and governance principles.

### Security
RBAC, SCC/Pod Security, NetworkPolicy, secrets integration patterns, OIDC boundaries, policy-as-code architecture and auditability.

### Reliability
Requests/limits, quotas, probes, PDB, HPA, rollout/rollback principles, failure domains and SLO-aware design.

### GitOps
Git as desired-state source, Argo CD architecture, App-of-Apps reference, separation between platform configuration and product repositories.

### Observability
Metrics, logs, traces, ServiceMonitor patterns, OpenTelemetry boundaries, SRE signals and integration with shared observability.

### Storage
PVC/StorageClass/CSI concepts, ODF/Ceph reference, stateful workload constraints, backup/restore architecture and storage failure domains.

### Multi-cluster
Management vs workload clusters, environment isolation, ACM governance concepts and GitOps projection.

### Day-2
Upgrade architecture, capacity, backup/restore, operational readiness, incident evidence, change control and platform lifecycle principles.

## Local and enterprise contexts

The repository distinguishes three contexts:

1. **Learning/lab** — CRC and certification exercises.
2. **Reference examples** — small manifests validated for syntax/rendering.
3. **Enterprise target architecture** — documented design principles whose runtime implementation belongs to dedicated repositories.

A lab result must never be presented as multi-node, production or client evidence.

## Reference implementation boundary

The `platform/` directory intentionally remains small. It demonstrates:

- lab namespaces;
- quotas/limits;
- RBAC;
- NetworkPolicy;
- a ServiceMonitor;
- a tiny instrumented workload;
- Argo CD Applications wiring these examples.

It does **not** become another common platform product.

## Evidence

See:
- `docs/governance/ASSET_STATUS_MODEL.md`
- `evidence/CLAIM_EVIDENCE_MATRIX.md`

## Related architecture

- `architecture/reference-architectures/platform-layers.md`
- `architecture/reference-architectures/gitops-platform.md`
- `architecture/reference-architectures/security-architecture.md`
- `architecture/reference-architectures/observability-sre.md`
- `architecture/reference-architectures/storage-architecture.md`
- `architecture/reference-architectures/day2-lifecycle.md`
- `architecture/reference-architectures/multi-cluster.md`
