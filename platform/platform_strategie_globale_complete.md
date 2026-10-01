# Legacy strategy note — superseded

**Status:** STALE_REQUALIFICATION_REQUIRED  
**Superseded on:** 2026-10-01

This document belonged to the former `rh-openshift-architect-lab` organization of the repository.

Its historical content remains available in Git history, but it must no longer be used as the current repository strategy because:

- the repository was renamed and repositioned as `openshift-platform-blueprints`;
- cluster lifecycle is now owned by `k8s-openshift-cluster-factory`;
- shared runtime services are owned by `shared-platform-services-openshift`;
- Argo CD expertise is owned by `argocd-expert-pack`;
- Keycloak expertise is owned by `keycloak-enterprise-roadmap-v7`;
- migration execution is owned by `openshift-migration-framework`;
- the old GitOps manifests required repair and revalidation.

Use these current documents instead:

1. `README.md`
2. `docs/governance/REPOSITORY_SCOPE.md`
3. `docs/governance/OWNERSHIP_MATRIX.md`
4. `docs/governance/ASSET_STATUS_MODEL.md`
5. `architecture/overview/platform-overview.md`

The `platform/` directory is now limited to **small validated reference examples** supporting the architecture.
