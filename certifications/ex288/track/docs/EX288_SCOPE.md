# Périmètre visé

Ce dépôt couvre principalement les zones suivantes :

- projets, déploiements, services, routes, probes ;
- ConfigMaps, Secrets, variables d'environnement, volumes ;
- ImageStreams, BuildConfigs, builds à partir de Containerfile ;
- S2I et personnalisation de scripts `assemble` / `run` ;
- triggers et hooks ;
- templates OpenShift ;
- chart Helm et surcouche Kustomize ;
- pipelines Tekton ;
- consommation simple d'un Operator ;
- diagnostic transversal ;
- sujets complémentaires souvent utiles : registry interne, RBAC, init containers, blue/green.

## Ce que ce dépôt n'essaie pas de faire

- couvrir toute l'administration cluster ;
- remplacer DO288 ;
- fournir un support théorique exhaustif ;
- garantir que chaque scénario tombe exactement à l'examen.
