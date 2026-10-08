# Claim / Evidence Matrix

**Date:** 2026-10-08

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
| EX280 preparation track | REFERENCE / REPO_PREP_COMPLETE | structure validated in CI | human replay only | CRC-oriented material, runtime not globally claimed | NOT_CLAIMED |
| EX288 preparation track | REFERENCE / MATURE_LEARNING_TRACK | structure validated in CI | lab-specific only | runtime not globally claimed | NOT_CLAIMED |
| EX370 preparation track | REFERENCE / REPO_PREP_COMPLETE | structure validated in CI | environment-dependent | ODF runtime not inferred from CRC | NOT_CLAIMED |
| EX380 preparation track | REFERENCE / REPO_PREP_COMPLETE | structure validated in CI | human replay / canonical runtime reuse | track-specific only | NOT_CLAIMED |
| EX480 / EX482 | REFERENCE / LIGHTWEIGHT | structure validated in CI | NOT_CLAIMED | NOT_CLAIMED | NOT_CLAIMED |

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
