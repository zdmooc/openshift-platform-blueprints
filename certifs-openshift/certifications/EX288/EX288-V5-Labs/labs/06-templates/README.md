# Lab 06 — Templates OpenShift

## Temps cible
20 minutes

## Objectif
Instancier un Template paramétré puis vérifier les objets créés.

## Préparation
```bash
oc new-project ex288-lab06
oc process -f ../../shared/templates/basic-node-template.yaml -p APP_NAME=tplapp -p MESSAGE='hello template' | oc apply -f -
```
