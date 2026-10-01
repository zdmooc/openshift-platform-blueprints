# Asset Status Model

**Date:** 2026-10-01

The repository uses explicit evidence levels to prevent architecture intent from being confused with runtime proof.

## Status vocabulary

| Status | Meaning |
|---|---|
| `REFERENCE` | Architecture, concept, pattern or knowledge asset. |
| `IMPLEMENTED` | Manifest/code exists in Git. |
| `STATIC_VALIDATED` | Syntax/schema/render validation passed. |
| `CI_RUNTIME_PROVEN` | Runtime behavior executed successfully in CI. |
| `CRC_RUNTIME_PROVEN` | Executed successfully on OpenShift Local / CRC. |
| `MULTINODE_PROVEN` | Behavior observed on a multi-node cluster. |
| `PRODUCTION_REFERENCE` | Design pattern suitable as an architecture reference; not a claim of client production deployment. |
| `STALE_REQUALIFICATION_REQUIRED` | Useful heritage requiring review before reuse. |

## Rules

1. A higher level never follows automatically from a lower one.
2. `IMPLEMENTED` does not mean deployable.
3. `STATIC_VALIDATED` does not mean runtime tested.
4. CRC single-node evidence does not prove worker/AZ/site resilience.
5. Certification labs remain learning assets even when executable.
6. Examples must not contain real credentials or private customer data.
7. Architecture documents may describe target-state capabilities not implemented in this repository.

## Current repository baseline

At the start of the 2026-10-01 cleanup program:

- architecture and certification content: `REFERENCE`;
- legacy `platform/` GitOps assets: `STALE_REQUALIFICATION_REQUIRED`;
- no repository-wide CI runtime claim;
- selected executable assets are being repaired and will first target `STATIC_VALIDATED`.
