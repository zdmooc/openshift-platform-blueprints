# 06B — Kustomize overlays

## Objectif
Appliquer plusieurs overlays Kustomize.

## Commandes
```bash

oc new-project ex288-06b || oc project ex288-06b

# adapter shared/kustomize/base/deployment.yaml en remplaçant CHANGE_ME par ex288-06b
oc apply -k shared/kustomize/overlays/dev
oc apply -k shared/kustomize/overlays/prod

```

## Vérifications
- changements observables entre dev et prod

## À retenir
- base + overlays
- bien contrôler namespace et image avant `oc apply -k`
