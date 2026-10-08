# Labs — EX380

**Statut dépôt : REPO_PREP_COMPLETE**  
**Exécution runtime globale : NOT_CLAIMED**

## Parcours canonique existant

| Bloc | Sujet | Labs présents |
|---|---|---:|
| 00 | Prereq refresh / EX280 | 1 |
| 01 | Authentication & identities | 4 |
| 02 | OADP backup / restore | 4 |
| 03 | Cluster partitioning | 3 |
| 04 | Advanced scheduling | 4 |
| 05 | OpenShift GitOps | 4 |
| 06 | Monitoring / metrics | 3 |
| 07 | Logging / Loki / Vector | 4 |
| 08 | Exam scenarios | 4 |

## Détail

### 00 — Prérequis
- révision EX280.

### 01 — Identité
- IdP LDAP ;
- Keycloak/OIDC ;
- GroupSync ;
- RBAC/kubeconfig.

### 02 — Data protection
- installation OADP ;
- backup namespace stateful ;
- restore namespace ;
- schedules / snapshots.

### 03 — Partitionnement cluster
- node labels / nodeSelector ;
- MachineConfigPools ;
- dedicated infra nodes.

### 04 — Scheduling avancé
- taints / tolerations ;
- PDB / résilience ;
- affinity / anti-affinity ;
- project defaults.

### 05 — GitOps
- installation OpenShift GitOps ;
- namespace infra ;
- namespace application ;
- App-of-Apps.

### 06 — Monitoring
- troubleshooting métriques applicatives ;
- troubleshooting métriques cluster ;
- alerts / silences.

### 07 — Logging
- logging operator ;
- forward logs vers Loki ;
- Event Router ;
- rétention.

### 08 — Scénarios
- full-stack DR ;
- cluster partitioning ;
- GitOps end-to-end ;
- incident observabilité.

## Règle d'exécution

Chaque lab rejoué doit consigner :
- version OpenShift ;
- environnement ;
- date ;
- commandes structurantes ;
- résultat positif/négatif ;
- limite rencontrée ;
- evidence path.

Un lab écrit n'est pas une preuve runtime.
