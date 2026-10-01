# Changelog

## 2026-10-01 — O1 OpenShift Blueprints cleanup

### I1 — Governance
- redefined repository as canonical OpenShift Architecture / Knowledge / Standards reference;
- added ownership matrix and evidence vocabulary;
- retired legacy strategy documents.

### I2 — GitOps/YAML repair
- rebuilt namespace, quota/LimitRange, RBAC and NetworkPolicy examples;
- repaired ServiceMonitor;
- repaired Argo CD Applications and repository URLs;
- added Kustomize entry points;
- added separate root bootstrap;
- added coherent demo metrics workload.

### I3 — Architecture
- normalized platform overview;
- added layer model, storage and Day-2 references;
- added platform standards.

### I4 — Portfolio boundaries
- linked GitOps, security, observability and multi-cluster architecture to canonical implementation owners;
- added dependency classification model.

### I5 — Validation
- added repository hygiene/YAML validation script;
- added yamllint, Kustomize rendering and kubeconform CI.

### I6 — Certifications
- normalized certification navigation;
- preserved historical EX288 tree while adding canonical pointer;
- clarified that learning assets do not imply certification status.

### I7 — Evidence / finalization
- added claim/evidence matrix;
- added final architecture index;
- static validation recorded: Reference Validation run 36854282558 SUCCESS.
