# Claim / Evidence Matrix

**Date:** 2026-10-01

| Capability | Repository state | Static validation | CI runtime | CRC/OpenShift | Multi-node |
|---|---|---|---|---|---|
| Repository governance / ownership | IMPLEMENTED | N/A | N/A | N/A | N/A |
| Architecture reference | REFERENCE | documentation checks targeted | N/A | N/A | N/A |
| Namespace examples | IMPLEMENTED | STATIC_VALIDATED — run 36854282558 | NOT_CLAIMED | NOT_CLAIMED | NOT_CLAIMED |
| Quota / LimitRange examples | IMPLEMENTED | STATIC_VALIDATED — run 36854282558 | NOT_CLAIMED | NOT_CLAIMED | NOT_CLAIMED |
| RBAC examples | IMPLEMENTED | STATIC_VALIDATED — run 36854282558 | NOT_CLAIMED | NOT_CLAIMED | NOT_CLAIMED |
| NetworkPolicy examples | IMPLEMENTED | STATIC_VALIDATED — run 36854282558 | NOT_CLAIMED | NOT_CLAIMED | NOT_CLAIMED |
| ServiceMonitor example | IMPLEMENTED | STATIC_VALIDATED — run 36854282558 | NOT_CLAIMED | NOT_CLAIMED | NOT_CLAIMED |
| Demo metrics workload | IMPLEMENTED | STATIC_VALIDATED — run 36854282558 | NOT_CLAIMED | NOT_CLAIMED | NOT_CLAIMED |
| Argo CD Applications | IMPLEMENTED | STATIC_VALIDATED — run 36854282558 | NOT_CLAIMED | NOT_CLAIMED | NOT_CLAIMED |
| Certification tracks | REFERENCE / LEARNING | out of active runtime gate | track-specific only | track-specific only | NOT_CLAIMED |

## Promotion rule

A cell may be promoted only after the corresponding validation result is observed and linked.

A green syntax/render CI does not become a CRC runtime claim.


## Static validation evidence

GitHub Actions workflow: `Reference Validation`.

Run `36854282558`: **SUCCESS**.

Successful gates:
- repository hygiene / stale-reference checks;
- YAML parsing;
- yamllint;
- Kustomize rendering;
- kubeconform schema validation with CRD schemas explicitly allowed to be missing.

No CRC runtime or multi-node claim is derived from this result.
