# OpenShift Certification Learning Tracks

**Status:** REFERENCE / LEARNING ASSETS / GOVERNANCE COMPLETE  
**Last review:** 2026-10-08

This directory contains structured learning material related to Red Hat OpenShift certification domains.

The presence of a track, lab, correction, mock exam or book does **not** mean the corresponding certification has been obtained.

## Canonical tracks

| Track | Current repository path | Portfolio role |
|---|---|---|
| EX280 | `certifications/ex280/` | primary OpenShift administration preparation |
| EX288 | `certifications/ex288_real_final_repo_enriched/` | complementary application development preparation |
| EX370 | `certifications/ex370/` | complementary ODF/storage preparation |
| EX380 | `certifications/ex380/` | primary advanced administration/automation preparation |
| EX480 | `certifications/ex480/track/` | lightweight multi-cluster/governance reference |
| EX482 | `certifications/ex482/` | lightweight event-driven/Kafka reference |

## 2026-10-08 completion

Repository-side certification governance has been normalized:
- EX280 path aligned with its real Lab00→Lab17 track;
- EX380 path aligned with its real identity/OADP/scheduling/GitOps/observability content;
- EX288 historical tree audited and retained without disruptive rename;
- EX370 ODF preparation separated from runtime HA claims;
- portfolio wording and evidence boundaries centralized;
- certification structure is now checked in CI.

## Expected structure

A mature track can contain:
- `README.md`;
- `PREPARATION.md`;
- `CHECKLIST.md`;
- `LABS.md`;
- `STATUS.md`;
- `track/` or `book-v1/`;
- explicit evidence only when actual execution exists.

Lightweight tracks may intentionally contain fewer assets.

## Separation from platform architecture

Certification labs do not own production platform standards.

Canonical owners remain:
- `architecture/`, `docs/standards/`, `docs/governance/` for architecture;
- `platform/` for small validated examples;
- Cluster Factory / Shared Platform / specialist repositories for runtime implementations.

## Truth boundary

A learning track is normally `REFERENCE` or `IMPLEMENTED`. Runtime levels are promoted only from observed evidence.

Safe CV wording:
- "EX280 — préparation en cours";
- "EX380 — préparation en cours";
- "parcours technique EX288 / EX370".

Unsafe without independent proof:
- "certifié EX280/EX380/EX288/EX370".

## Portfolio use

The certification area demonstrates structured learning, technical depth, repeatable exercises and disciplined evidence boundaries. It complements — but does not replace — professional experience and runtime proofs in canonical repositories.

See:
- `CERTIFICATION_INDEX.md`;
- `PORTFOLIO_READINESS.md`.
