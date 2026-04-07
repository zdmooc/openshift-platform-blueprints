# Stratégie d'examen

## Séquence conseillée

1. Lire tout le sujet pendant 10 à 15 minutes.
2. Marquer les tâches :
   - faciles / rapides ;
   - moyennes ;
   - diagnostics / dépannage.
3. Sécuriser d'abord les tâches les plus simples et visibles.
4. Vérifier **après chaque action** :
   - `oc get all`
   - `oc describe ...`
   - `oc logs ...`
   - `oc get events --sort-by=.lastTimestamp`
5. Garder une vigilance constante sur :
   - mauvais namespace ;
   - mauvais nom de ressource ;
   - oubli de tag d'image ;
   - Route non pointée vers le bon Service ;
   - Secret / ConfigMap non monté ou mal référencé ;
   - BuildConfig qui pointe sur la mauvaise source ou le mauvais contextDir.

## Diagnostic réflexe

```bash
oc project
oc get all
oc get pods
oc describe pod <pod>
oc logs <pod> --all-containers=true
oc get events --sort-by=.lastTimestamp | tail -n 20
oc describe bc <name>
oc describe is <name>
oc describe route <name>
oc auth can-i <verb> <resource> --as <user>
```
