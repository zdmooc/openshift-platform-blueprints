# Lab 03 — ImageStream, BuildConfig et Containerfile

## Temps cible
35 minutes

## Objectif
Créer un ImageStream et un BuildConfig utilisant le `Containerfile` de `shared/apps/basic-node`, puis lancer un build binaire.

## Préparation
```bash
oc new-project ex288-lab03
oc apply -f manifests/
oc start-build basic-node-build --from-dir=../../shared/apps/basic-node --follow
```
