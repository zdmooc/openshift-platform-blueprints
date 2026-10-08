# EX380 — Readiness Gate

**Date : 2026-10-08**

## Repository gate

- [x] scope documented;
- [x] learning path structured;
- [x] labs mapped to real files;
- [x] Day-2 evidence gates defined;
- [x] truth boundary documented;
- [x] four integrated scenarios available.

**Verdict repository : READY_FOR_STRUCTURED_REPLAY.**

## Scenario cards

### S1 — Full-stack DR
Path: `book-v1/08-exam-scenarios/scenario-01-full-stack-dr.md`

Expected replay record:
- start time / end time;
- resources affected;
- backup/restore or recovery sequence;
- health checks;
- residual limitations.

### S2 — Cluster partitioning
Path: `book-v1/08-exam-scenarios/scenario-02-cluster-partitioning.md`

Expected replay record:
- node labels/selectors;
- scheduling result;
- dedicated-node assumptions;
- CRC or multi-node limitation.

### S3 — GitOps end-to-end
Path: `book-v1/08-exam-scenarios/scenario-03-gitops-end-to-end.md`

Expected replay record:
- desired state;
- sync result;
- drift/self-heal;
- rollback;
- workload revalidation.

### S4 — Observability incident
Path: `book-v1/08-exam-scenarios/scenario-04-observability-incident.md`

Expected replay record:
- symptom;
- metric/log signal;
- diagnostic path;
- RCA;
- remediation;
- post-fix verification.

## Human-only certification gate

The following remains intentionally outside repository automation:
- timed execution by the candidate;
- exam booking;
- official exam result.

The CV may say **"EX380 — préparation en cours"**. It must not say **"certifié EX380"** until independently verified.
