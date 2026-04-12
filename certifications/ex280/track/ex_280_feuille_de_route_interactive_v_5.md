# Feuille de route EX280 – V5 (CRC + dépôt unifié)

## 1. Objectif

Reprendre la pratique **EX280** sur **CRC / OpenShift Local** avec un **seul chemin de vérité**, propre, cohérent et maintenable.

Cette feuille de route ne décrit plus les anciennes versions du dépôt.
Elle reflète désormais le **track V5 unifié**.

Objectifs :

- pratiquer l’EX280 en mode **CLI-first** ;
- travailler sur un parcours **court, rejouable, discipliné** ;
- éviter les doublons documentaires ;
- garder une séparation claire entre :
  - le **track pratique actif** ;
  - les **notes de préparation** ;
  - l’**archive théorique PDF** ;
  - le **réservoir externe d’idées**.

---

## 2. Chemins de vérité

### 2.1. Dépôt principal

Racine locale :

```text
/c/workspaces/openshift2026/rh-openshift-architect-lab
```

Le travail EX280 se fait maintenant ici :

```text
certifications/ex280/
```

---

### 2.2. Dossier EX280 actif

Chemin actif :

```text
certifications/ex280/
```

Contenu principal :

- `README.md` → point d’entrée général ;
- `PREPARATION.md` → feuille de route de préparation ;
- `LABS.md` → vue synthétique du parcours ;
- `CHECKLIST.md` → checklist personnelle ;
- `NOTES.md` → journal de bord ;
- `docs/EX280-book-archive-v1.pdf` → archive théorique légère ;
- `track/checklists/ex280-objectives-checklist.md` → checklist opérationnelle ;
- `track/labs/` → **labs V5 actifs**.

---

### 2.3. Réservoir externe

Référence externe éventuelle :

```text
/c/workspaces/openshift2026/EX280-Ultimate-Guide
```

Rôle :

- banque d’idées ;
- variantes ;
- scénarios complémentaires ;
- support secondaire.

Règle :

- **ne pas le traiter comme chemin principal** ;
- ne pas recopier en vrac ;
- ne l’utiliser qu’en cas de besoin ciblé.

---

### 2.4. Archive théorique locale

Le livre source ancien a été remplacé par une archive PDF locale :

```text
certifications/ex280/docs/EX280-book-archive-v1.pdf
```

Rôle :

- support de révision ;
- rappel théorique ;
- lecture ponctuelle.

Ce PDF n’est plus le centre du dispositif.
Le centre du dispositif est désormais le **track V5**.

---

## 3. Architecture pratique actuelle

### 3.1. Checklist track

```text
certifications/ex280/track/checklists/ex280-objectives-checklist.md
```

### 3.2. Labs actifs

```text
certifications/ex280/track/labs/
```

Contenu actif V5 :

- `00-README.md`
- `lab00-env-bootstrap-crc.md`
- `lab01-projects-context-query-images.md`
- `lab02-declarative-deploy-service-route-rollout.md`
- `lab03-configmaps-secrets.md`
- `lab04-pvc-probes-resources.md`
- `lab05-routes-tls.md`
- `lab06-networkpolicies.md`
- `lab07-non-http-loadbalancer.md`
- `lab08-htpasswd-users-groups-rbac.md`
- `lab09-serviceaccounts-rbac-api.md`
- `lab10-scc-privileged-runtime-security.md`
- `lab11-quotas-limitrange-projecttemplate-scaling.md`
- `lab12-templates.md`
- `lab13-helm-kustomize.md`
- `lab14-operators-olm.md`
- `lab15-logging-events-troubleshooting.md`
- `lab16-jobs-cronjobs.md`
- `lab17-capstone-examblanc.md`

---

## 4. Parcours V5 officiel

## Lab00 — Bootstrap CRC

Fichier :

```text
lab00-env-bootstrap-crc.md
```

But :
- vérifier CRC ;
- vérifier `oc` ;
- vérifier l’utilisateur courant ;
- vérifier les nœuds ;
- vérifier les cluster operators ;
- démarrer proprement un projet de test.

---

## Lab01 — Projects, Context, Queries, Images

Fichier :

```text
lab01-projects-context-query-images.md
```

But :
- projets ;
- contexte `oc` ;
- requêtes et formats ;
- images, tags, digests ;
- inspection des ressources.

---

## Lab02 — Déclaratif, Deployment, Service, Route, Rollout

Fichier :

```text
lab02-declarative-deploy-service-route-rollout.md
```

But :
- manifests YAML ;
- `oc apply` ;
- déploiement ;
- service ;
- route ;
- patch ;
- rollout ;
- rollback.

---

## Lab03 — ConfigMaps & Secrets

Fichier :

```text
lab03-configmaps-secrets.md
```

But :
- création de ConfigMaps ;
- création de Secrets ;
- injection par env ;
- montage en volume ;
- mise à jour.

---

## Lab04 — PVC, Probes, Resources

Fichier :

```text
lab04-pvc-probes-resources.md
```

But :
- PVC ;
- persistance ;
- probes ;
- requests/limits ;
- robustesse applicative.

---

## Lab05 — Routes & TLS

Fichier :

```text
lab05-routes-tls.md
```

But :
- exposition HTTP ;
- TLS edge ;
- lecture d’une route ;
- diagnostic route/service/endpoints.

---

## Lab06 — NetworkPolicies

Fichier :

```text
lab06-networkpolicies.md
```

But :
- deny-all ;
- ouvertures ciblées ;
- contrôle ingress ;
- tests de connectivité.

---

## Lab07 — Non-HTTP / LoadBalancer

Fichier :

```text
lab07-non-http-loadbalancer.md
```

But :
- exposition non-HTTP ;
- service `LoadBalancer` ;
- variante CRC si pas de LB externe.

---

## Lab08 — HTPasswd, Users, Groups, RBAC

Fichier :

```text
lab08-htpasswd-users-groups-rbac.md
```

But :
- HTPasswd ;
- users ;
- groups ;
- rôles ;
- contrôles d’accès.

---

## Lab09 — ServiceAccounts, RBAC, API

Fichier :

```text
lab09-serviceaccounts-rbac-api.md
```

But :
- ServiceAccounts ;
- RBAC minimal ;
- accès API Kubernetes ;
- lecture seule ;
- vérification `403` sur action interdite.

---

## Lab10 — SCC & Runtime Security

Fichier :

```text
lab10-scc-privileged-runtime-security.md
```

But :
- SCC ;
- pod privilégié ;
- binding SCC ;
- compréhension des erreurs de sécurité runtime.

---

## Lab11 — Quotas, LimitRange, Project Template, Scaling

Fichier :

```text
lab11-quotas-limitrange-projecttemplate-scaling.md
```

But :
- ResourceQuota ;
- LimitRange ;
- project template ;
- scaling ;
- contrôle de consommation.

---

## Lab12 — Templates

Fichier :

```text
lab12-templates.md
```

But :
- templates OpenShift ;
- paramètres ;
- `oc process` ;
- instanciation.

---

## Lab13 — Helm & Kustomize

Fichier :

```text
lab13-helm-kustomize.md
```

But :
- Helm ;
- release simple ;
- Kustomize ;
- overlays ;
- packaging léger.

---

## Lab14 — Operators & OLM

Fichier :

```text
lab14-operators-olm.md
```

But :
- OperatorGroup ;
- Subscription ;
- CSV ;
- cycle OLM minimal.

---

## Lab15 — Logging, Events & Troubleshooting

Fichier :

```text
lab15-logging-events-troubleshooting.md
```

But :
- méthode de diagnostic ;
- `events` ;
- `describe` ;
- `logs` ;
- image cassée ;
- probes KO ;
- service sans endpoints ;
- quota dépassé.

---

## Lab16 — Jobs & CronJobs

Fichier :

```text
lab16-jobs-cronjobs.md
```

But :
- job one-shot ;
- cronjob ;
- historique ;
- batch simple.

---

## Lab17 — Capstone / Examen blanc

Fichier :

```text
lab17-capstone-examblanc.md
```

But :
- rejouer un scénario global ;
- enchaîner plusieurs briques ;
- travailler sous contrainte de temps.

---

## 5. Ordre de travail recommandé

### Phase 1 — Fondations

- [ ] Lab00 — Bootstrap CRC
- [ ] Lab01 — Projects / Context / Images
- [ ] Lab02 — Déclaratif / Deploy / Route / Rollout
- [ ] Lab03 — ConfigMaps / Secrets
- [ ] Lab04 — PVC / Probes / Resources

Règle : tant que ces 5 labs ne sont pas fluides, on ne monte pas plus haut.

---

### Phase 2 — Réseau et sécurité

- [ ] Lab05 — Routes & TLS
- [ ] Lab06 — NetworkPolicies
- [ ] Lab07 — Non-HTTP / LoadBalancer
- [ ] Lab08 — HTPasswd / Users / Groups / RBAC
- [ ] Lab09 — ServiceAccounts / RBAC / API
- [ ] Lab10 — SCC / Runtime Security

---

### Phase 3 — Contrôle, packaging, opérateurs

- [ ] Lab11 — Quotas / LimitRange / Project Template / Scaling
- [ ] Lab12 — Templates
- [ ] Lab13 — Helm / Kustomize
- [ ] Lab14 — Operators / OLM
- [ ] Lab15 — Logging / Events / Troubleshooting

---

### Phase 4 — Batch et synthèse

- [ ] Lab16 — Jobs / CronJobs
- [ ] Lab17 — Capstone / Examen blanc

---

## 6. Règles de travail (mode examen)

### Règle 1 — CLI-first

Tout ce qui est critique doit être faisable avec `oc`.

### Règle 2 — Vérification de contexte avant chaque lab

Toujours commencer par :

```bash
oc whoami
oc project
oc get nodes
oc get co
```

### Règle 3 — Routine de diagnostic unique

En cas de problème :

```bash
oc project
oc get pods -o wide
oc get events --sort-by=.lastTimestamp | tail -n 30
oc describe <ressource>
oc logs <pod> --all-containers --tail=200
```

### Règle 4 — Notes obligatoires

Après chaque lab, noter :

- date ;
- objectif ;
- commandes importantes ;
- erreurs ;
- cause racine ;
- correctif ;
- points à retenir.

---

## 7. Boucle de progression

### Premier passage

- faire tous les labs une fois avec support ;
- comprendre les objets ;
- compléter `NOTES.md`.

### Deuxième passage

- refaire les labs avec moins d’aide ;
- chronométrer certains thèmes ;
- remplir la checklist.

### Troisième passage

- refaire les labs à froid ;
- enchaîner plusieurs labs ;
- lancer le capstone en temps limité.

---

## 8. Références internes utiles

### Pilotage

- `certifications/ex280/README.md`
- `certifications/ex280/PREPARATION.md`
- `certifications/ex280/LABS.md`
- `certifications/ex280/CHECKLIST.md`
- `certifications/ex280/NOTES.md`

### Track actif

- `certifications/ex280/track/checklists/ex280-objectives-checklist.md`
- `certifications/ex280/track/labs/00-README.md`
- `certifications/ex280/track/labs/lab00...lab17`

### Archive théorique

- `certifications/ex280/docs/EX280-book-archive-v1.pdf`

---

## 9. Règle finale

Le chemin de vérité est maintenant :

```text
certifications/ex280/track/labs/
```

V1, V2 et V3 ne sont plus le parcours actif.
Le travail quotidien doit se faire sur le **track V5 unifié**.

