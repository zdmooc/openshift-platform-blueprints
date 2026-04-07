# Lab 07 — Helm et Kustomize

## Temps cible
35 minutes

## Objectif
Déployer le chart Helm fourni, puis appliquer une variante Kustomize sur un autre projet.

## Préparation
```bash
oc new-project ex288-helm
helm upgrade --install basic-node ../../shared/charts/basic-node
oc new-project ex288-k
oc apply -k ../../shared/kustomize/overlays/dev
```
