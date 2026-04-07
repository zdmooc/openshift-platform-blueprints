# Lab 04 — Custom S2I

## Temps cible
35 minutes

## Objectif
Utiliser les scripts `.s2i/bin/assemble` et `.s2i/bin/run` fournis dans `shared/apps/basic-node` pour construire une image S2I personnalisée.

## Préparation
```bash
oc new-project ex288-lab04
oc apply -f manifests/
oc start-build basic-node-s2i --from-dir=../../shared/apps/basic-node --follow
```
