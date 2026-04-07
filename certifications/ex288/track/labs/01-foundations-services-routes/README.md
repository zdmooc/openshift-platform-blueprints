# Lab 01 — Fondations : projet, déploiement, service, route

## Temps cible
20 minutes

## Objectif
Créer un projet propre, déployer une application existante, l'exposer par Service puis Route, et vérifier le résultat.

## Préparation
```bash
oc new-project ex288-lab01
```

## Tâches
1. Déployer l'image `registry.access.redhat.com/ubi9/httpd-24`.
2. Créer un Service sur le port 8080.
3. Créer une Route.
4. Vérifier l'accès.
5. Ajouter le label `track=foundation` au Deployment.

## Exemple de solution rapide
```bash
oc create deployment web --image=registry.access.redhat.com/ubi9/httpd-24
oc expose deployment web --port=8080
oc expose service web
oc get route
curl http://$(oc get route web -o jsonpath='{.spec.host}')
oc label deployment web track=foundation
```
