# EX380 — Interview Summary

## 30-second positioning

Parcours de préparation OpenShift avancé couvrant identité/RBAC, OADP backup-restore, partitionnement et scheduling, OpenShift GitOps, monitoring, logging et scénarios intégrés. Le dépôt sépare explicitement préparation, preuves runtime et certification officielle.

## Architecture discussion points

- identity provider versus workload identity;
- RBAC and least privilege;
- backup/restore and state protection;
- scheduling constraints and disruption budgets;
- GitOps desired state and recovery;
- metrics/logs for Day-2 diagnosis;
- limits of CRC versus multi-node OpenShift.

## What to demonstrate

Prefer concrete runtime evidence from canonical repositories rather than reading the certification material itself:
- Shared Platform for RBAC/Operator/platform consumption;
- Cluster Factory for Day-2/N3;
- Argo CD expert pack for GitOps;
- ELK/observability repos for logging and metrics.

## Safe wording

**CV:** "Red Hat EX380 — préparation en cours."  
**Interview:** "J'ai structuré un parcours EX380 complet et je rejoue les domaines sur mes environnements OpenShift ; je ne présente pas la certification comme obtenue."
