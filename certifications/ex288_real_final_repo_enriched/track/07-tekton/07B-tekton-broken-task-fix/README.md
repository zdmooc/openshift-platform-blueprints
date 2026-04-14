# 07B — Tekton broken task fix

## Objectif
Appliquer une Task cassée et identifier le défaut.

## Commandes
```bash

oc new-project ex288-07b || oc project ex288-07b
oc apply -f shared/tekton/task-broken.yaml
oc get task
# corriger ensuite la référence au paramètre manquant

```

## Vérifications
- défaut identifié

## Notes
Nécessite Tekton installé.
