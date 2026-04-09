# EX280 — Labs V5 (fusion propre V1 + V2 + V3)

## Objectif du pack

Ce pack V5 fournit **une seule série active de labs**, cohérente et sans doublons, pour préparer EX280 sur **CRC / OpenShift Local** tout en restant réutilisable sur un cluster OpenShift plus complet.

Il remplace les variantes V1, V2 et V3 par une structure unique :

- progressive ;
- orientée CLI `oc` ;
- compatible CRC quand c’est possible ;
- explicite sur les cas "cluster complet / prod / examen".

## Structure

- `00-README.md` : vue d’ensemble du pack
- `checklists/ex280-objectives-checklist.md` : checklist de progression
- `lab00` à `lab17` : labs actifs

## Ordre conseillé

1. `lab00` — bootstrap CRC, `oc`, vérifications cluster
2. `lab01` — projets, contexte, requêtes, images
3. `lab02` — déclaratif, déploiement, service, route, rollout
4. `lab03` — ConfigMaps et Secrets
5. `lab04` — PVC, probes, requests/limits
6. `lab05` — routes et TLS
7. `lab06` — NetworkPolicies
8. `lab07` — non-HTTP / LoadBalancer
9. `lab08` — HTPasswd, users, groups, RBAC
10. `lab09` — ServiceAccounts, RBAC, accès API
11. `lab10` — SCC, sécurité runtime, privileged
12. `lab11` — quotas, LimitRange, project template, scaling
13. `lab12` — templates
14. `lab13` — Helm et Kustomize
15. `lab14` — Operators et OLM
16. `lab15` — logging, events, troubleshooting
17. `lab16` — jobs et cronjobs
18. `lab17` — capstone / examen blanc

## Conventions

- Shell : `bash` / Git Bash
- Namespace par lab : `ex280-labXX-zidane`
- Les labs sont idempotents autant que possible
- Chaque lab contient :
  - objectif ;
  - prérequis ;
  - tâches ;
  - vérifications ;
  - nettoyage ;
  - pièges fréquents

## Principes de travail

- Commencer par lire tout le lab
- Vérifier toujours le projet courant
- Utiliser en priorité :
  - `oc get`
  - `oc describe`
  - `oc get events --sort-by=.lastTimestamp`
  - `oc logs`
- Corriger le minimum nécessaire avant de passer à l’étape suivante

## Notes environnement

### CRC / OpenShift Local
CRC est parfait pour :
- projets ;
- routes ;
- ConfigMaps / Secrets ;
- PVC ;
- quotas / LimitRange ;
- RBAC / SA / SCC ;
- templates ;
- Helm / Kustomize ;
- troubleshooting ;
- jobs / cronjobs.

### Points dépendants du cluster
Certains labs dépendent davantage du cluster ou de tes droits :
- `HTPasswd` ;
- `LoadBalancer` externe ;
- `Operators` ;
- `HPA` ou métriques selon l’environnement.

Le pack V5 le signale quand nécessaire.

## Résultat attendu

À la fin du pack, tu dois être capable de :

- manipuler rapidement les objets OpenShift utiles à EX280 ;
- diagnostiquer des erreurs courantes ;
- rejouer un mini-exam en 90–120 minutes ;
- utiliser ce dossier comme base propre dans ton dépôt.
