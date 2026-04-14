# 02C — Internal registry publish consume

## Objectif
Vérifier l’usage du registre interne et la consommation d’image.

## Commandes
```bash

oc new-project ex288-02c || oc project ex288-02c
oc registry info
oc get is
# selon le cluster, tag/push puis déploiement depuis l'image interne

```

## Vérifications
- URL du registre récupérée
- image ou imagestream visible

## Notes
Ce lab dépend des droits et de la configuration du cluster.
