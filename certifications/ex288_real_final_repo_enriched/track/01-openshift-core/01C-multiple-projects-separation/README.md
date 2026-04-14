# 01C — Multiple projects separation

## Objectif
Valider que les ressources restent séparées par projet.

## Commandes
```bash

oc new-project ex288-01c-a || oc project ex288-01c-a
oc new-project ex288-01c-b || true

oc project ex288-01c-a
oc create configmap cm-a --from-literal=MSG=a

oc project ex288-01c-b
oc create configmap cm-b --from-literal=MSG=b

oc project ex288-01c-a
oc get cm

oc project ex288-01c-b
oc get cm

```

## Vérifications
- chaque projet voit sa propre ConfigMap
