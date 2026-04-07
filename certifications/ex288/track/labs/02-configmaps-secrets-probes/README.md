# Lab 02 — ConfigMaps, Secrets et probes

## Temps cible
30 minutes

## Objectif
Déployer l'application `basic-node` sans build préalable, en injectant ConfigMap et Secret, puis ajouter les probes.

## Préparation
```bash
oc new-project ex288-lab02
oc create configmap app-config --from-literal=APP_MESSAGE='hello from configmap'
oc create configmap app-code --from-file=server.js=files/server.js
oc create secret generic app-secret --from-literal=token='s3cr3t'
oc apply -f manifests/
oc expose service basic-node
```
