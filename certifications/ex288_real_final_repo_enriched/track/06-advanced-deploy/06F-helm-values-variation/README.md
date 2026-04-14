# 06F — Helm values variation

## Objectif
Tester une variation de valeurs Helm sans changer le chart.

## Commandes
```bash

oc new-project ex288-06f || oc project ex288-06f

mkdir -p rendered/ex288-06f
sed 's/CHANGE_ME/ex288-06f/g' shared/charts/basic-node/values.yaml > rendered/ex288-06f/values.yaml

helm template basic-node shared/charts/basic-node -f rendered/ex288-06f/values.yaml --set env.APP_MESSAGE='hello override'

```

## Vérifications
- rendu Helm avec override visible
