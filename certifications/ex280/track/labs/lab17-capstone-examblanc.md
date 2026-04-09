# Lab17 — Capstone / Examen Blanc

## Objectif

Simuler un mini-examen EX280 en 90–120 minutes.

## Pré-requis

- Labs 00→16 déjà pratiqués.

```bash
export NS=ex280-capstone-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Scénario

### A — Déploiement et exposition
1. Déployer `web` avec 2 replicas
2. Créer un Service
3. Créer une Route
4. Tester depuis un pod interne et via host externe si possible

### B — ConfigMaps / Secrets
1. Créer `app-config` et `app-secret`
2. Déployer un pod qui lit les deux
3. Exporter / réappliquer le YAML

### C — PVC / probes / resources
1. Créer un PVC
2. Monter le volume
3. Ajouter readiness/liveness
4. Ajouter requests/limits

### D — RBAC / SA / API
1. Créer `api-reader`
2. Créer Role + RoleBinding
3. Déployer un pod appelant l’API
4. Vérifier un refus `403`

### E — Quotas / LimitRange
1. Créer ResourceQuota
2. Créer LimitRange
3. Prouver l’injection de defaults
4. Provoquer un dépassement simple

### F — Troubleshooting
1. Casser une image ou une probe
2. Diagnostiquer avec :
```bash
oc get pods
oc describe pod -l app=<app>
oc get events --sort-by=.lastTimestamp | tail -n 20
oc logs -l app=<app> || true
```
3. Corriger

### G — Batch
1. Créer un Job
2. Créer un CronJob
3. Suspendre le CronJob

## Vérifications

- Deployment, Service, Route présents
- ConfigMap + Secret présents
- PVC présent
- Role + RoleBinding présents
- ResourceQuota + LimitRange présents
- Job + CronJob présents
- l’erreur finale est diagnostiquée puis corrigée

## Nettoyage
```bash
oc delete project "$NS"
```
