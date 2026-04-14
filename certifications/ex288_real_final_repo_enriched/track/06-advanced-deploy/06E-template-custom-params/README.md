# 06E — Template custom params

## Objectif
Pratiquer plusieurs paramètres sur un template.

## Commandes
```bash

oc new-project ex288-06e || oc project ex288-06e

mkdir -p rendered/ex288-06e
sed 's/CHANGE_ME/ex288-06e/g' shared/templates/basic-node-template.yaml > rendered/ex288-06e/basic-node-template.yaml

oc process -f rendered/ex288-06e/basic-node-template.yaml -p APP_NAME=custom-app -p MESSAGE='hello custom' | oc apply -f -
oc get all

```

## Vérifications
- paramètres bien substitués
