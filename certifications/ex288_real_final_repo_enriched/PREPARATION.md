# Préparation

## Objectif
Travailler l’EX288 avec des labs courts, rejouables et proches du geste réel.

## Règles
- toujours vérifier le projet courant ;
- toujours vérifier le résultat final ;
- ne pas enchaîner des modifications sans contrôle ;
- consigner les erreurs dans `NOTES.md`.

## Commandes réflexes
```bash
oc whoami
oc project
oc get all
oc get is,bc,build
oc get svc,route,endpoints
oc get events --sort-by=.lastTimestamp | tail -n 30
oc describe <resource>
oc logs <pod-or-build>
```
