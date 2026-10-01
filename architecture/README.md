# OpenShift Architecture Reference

**Status:** REFERENCE  
**Last review:** 2026-10-01

This directory contains the canonical architecture views for `openshift-platform-blueprints`.

## Entry point

Start with:

- `overview/platform-overview.md`

It defines the platform layering, repository ownership boundaries and the difference between architecture reference and runtime proof.

## Reference architectures

- `reference-architectures/platform-layers.md` — L0→L5 layering and portfolio ownership;
- `reference-architectures/gitops-platform.md` — GitOps architecture and Argo CD reference model;
- `reference-architectures/security-architecture.md` — RBAC, network, identity and policy architecture;
- `reference-architectures/observability-sre.md` — metrics/logs/traces/SRE reference;
- `reference-architectures/storage-architecture.md` — CSI/PVC/ODF/stateful/backup concepts;
- `reference-architectures/day2-lifecycle.md` — lifecycle, upgrades, capacity and operational readiness;
- `reference-architectures/multi-cluster.md` — management/workload cluster and governance patterns.

## Governance

Repository boundaries are defined in:

- `../docs/governance/REPOSITORY_SCOPE.md`;
- `../docs/governance/OWNERSHIP_MATRIX.md`;
- `../docs/governance/DEPENDENCY_CLASSIFICATION.md`;
- `../docs/governance/ASSET_STATUS_MODEL.md`.

Platform standards are summarized in:

- `../docs/standards/PLATFORM_STANDARDS.md`.

## Implementation boundary

Architecture documents explain **why and what**.

The small examples under `platform/` illustrate selected standards.

Operational implementations live in their canonical repositories:

- cluster lifecycle → `k8s-openshift-cluster-factory`;
- common platform services → `shared-platform-services-openshift`;
- Argo CD expertise → `argocd-expert-pack`;
- Keycloak expertise → `keycloak-enterprise-roadmap-v7`;
- migration → `openshift-migration-framework`.

## Truth rule

An architecture diagram or target-state description is `REFERENCE` until an implementation and evidence explicitly promote the claim.
