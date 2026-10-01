# OpenShift Certification Learning Tracks

**Status:** REFERENCE / LEARNING ASSETS  
**Last review:** 2026-10-01

This directory contains structured learning material related to Red Hat OpenShift certification domains.

It is a **learning and knowledge area**. The presence of a track, lab or book does **not** mean the corresponding certification has been obtained.

## Canonical tracks

| Track | Current repository path | Portfolio role |
|---|---|---|
| EX280 | `certifications/ex280/` | OpenShift administration foundations |
| EX288 | `certifications/ex288_real_final_repo_enriched/` | OpenShift application development learning assets |
| EX370 | `certifications/ex370/` | OpenShift Data Foundation / storage |
| EX380 | `certifications/ex380/` | advanced administration/automation/operations topics |
| EX480 | `certifications/ex480/` | multi-cluster / governance learning |
| EX482 | `certifications/ex482/` | event-driven / Kafka-related learning |

## Normalization rule

Historical directory names are preserved when renaming hundreds of assets would add risk without architectural value.

The canonical human-readable map is maintained in:

- `certifications/CERTIFICATION_INDEX.md`;
- this README;
- the repository root README.

Future new content should use the normalized track names documented in the index.

## Expected structure of a track

A track may contain:

- `README.md` — scope and navigation;
- `PREPARATION.md` — study plan;
- `CHECKLIST.md` — objectives/checklist;
- `LABS.md` — lab map;
- `track/` — practical progression;
- `book-v1/` — long-form learning support when useful;
- evidence placeholders only when they correspond to actual lab execution.

Not every historical track currently has every element.

## Separation from platform architecture

Certification labs may demonstrate OpenShift concepts, but they do not own production platform standards.

The canonical architecture remains under:

- `architecture/`;
- `docs/standards/`;
- `docs/governance/`.

Small validated platform examples remain under `platform/`.

## Truth boundary

Use the repository evidence vocabulary:

`REFERENCE | IMPLEMENTED | STATIC_VALIDATED | CI_RUNTIME_PROVEN | CRC_RUNTIME_PROVEN | MULTINODE_PROVEN`.

A learning lab is normally `REFERENCE` or `IMPLEMENTED` until an execution result is explicitly stored.

## Portfolio use

The value of this directory is to demonstrate structured learning, technical depth and reusable training material.

It must not be used to imply a certification status that is not independently verified.
