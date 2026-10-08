# EX380 — Day-2 Evidence Plan

**Date : 2026-10-08**  
**But :** relier le track de préparation aux preuves réellement observables sans dupliquer les responsabilités des dépôts canoniques.

## Mapping

| Domaine EX380 | Matériel du track | Owner runtime principal | Niveau à revendiquer ici |
|---|---|---|---|
| Identity / RBAC | `book-v1/01-auth-identities/` | `shared-platform-services-openshift` / `keycloak-enterprise-roadmap-v7` | REFERENCE / preparation |
| OADP backup/restore | `book-v1/02-oadp-backup-restore/` | `k8s-openshift-cluster-factory` | REFERENCE jusqu'à replay dédié |
| Cluster partitioning | `book-v1/03-cluster-partitioning/` | `k8s-openshift-cluster-factory` | REFERENCE ; CRC limitation |
| Advanced scheduling | `book-v1/04-advanced-scheduling/` | Cluster Factory / workload repos | REFERENCE + reuse possible |
| OpenShift GitOps | `book-v1/05-gitops-openshift/` | `argocd-expert-pack` + Shared Platform | REFERENCE ; runtime ailleurs |
| Monitoring | `book-v1/06-monitoring-metrics/` | Cluster Factory / observability owners | REFERENCE ; runtime ailleurs |
| Logging | `book-v1/07-logging-loki-vector/` | `elk-log-data-platform` | REFERENCE ; runtime elsewhere |
| Exam scenarios | `book-v1/08-exam-scenarios/` | n/a | human replay required |

## Gate OADP

Pour transformer OADP en preuve runtime :
1. installer/utiliser un OADP Operator compatible ;
2. configurer un backend réellement accessible ;
3. créer un workload avec état ;
4. effectuer backup ;
5. supprimer la ressource/namespace ciblé ;
6. restaurer ;
7. vérifier l'intégrité de la donnée ;
8. stocker sorties et versions.

Aucun document statique ne remplace ces huit étapes.

## Gate scheduling

Le track couvre taints/tolerations, affinity/anti-affinity et PDB. Sur CRC mono-nœud, les comportements multi-node ne doivent pas être promus. Les preuves de scheduling doivent être rejouées sur un environnement adapté lorsque le comportement exige plusieurs nœuds.

## Gate GitOps

Le track peut réutiliser les preuves déjà présentes dans les dépôts GitOps/Shared Platform :
- Synced / Healthy ;
- drift ;
- self-heal ;
- prune ;
- rollback.

Le track EX380 n'en devient pas owner.

## Gate observabilité

Une preuve acceptable doit inclure au minimum :
- target/scrape ou collecte active ;
- métrique/log réellement généré ;
- requête permettant de le retrouver ;
- alerte ou diagnostic reproductible.

## Règle finale

Le parcours EX380 est désormais **complet côté préparation documentaire**. Les sujets nécessitant un environnement réel sont explicitement séparés du statut de préparation.
