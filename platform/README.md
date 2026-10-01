# Platform Reference Examples

**Status:** IMPLEMENTED / STATIC_VALIDATION TARGET

This directory contains **small OpenShift reference examples** supporting the architecture described by this repository.

It is deliberately not a second implementation of the MayaBank common platform.

## Contents

- `gitops/cluster-config/` — namespaces, quotas/limits, RBAC and NetworkPolicy examples;
- `gitops/argocd-apps/` — Argo CD Applications referencing those examples;
- `gitops/bootstrap/platform-root.yaml` — root Application used to bootstrap the example set;
- `observability/servicemonitors/` — ServiceMonitor example;
- `examples/demo-metrics/` — tiny workload used to make the observability example coherent.

## Ownership boundary

Operational platform services belong to `zdmooc/shared-platform-services-openshift`.

Cluster provisioning and lifecycle belong to `zdmooc/k8s-openshift-cluster-factory`.

Deep Argo CD labs/evidence belong to `zdmooc/argocd-expert-pack`.

## Validation

`.github/workflows/reference-validation.yml` validates the active reference surface using:

- PyYAML parsing and repository hygiene checks;
- yamllint;
- Kustomize rendering;
- kubeconform for standard Kubernetes schemas.

Runtime deployment on CRC is not claimed by this directory unless explicit evidence is added.
