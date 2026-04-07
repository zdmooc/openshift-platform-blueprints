# EX288-V5-Labs

Dépôt de préparation **pratique** pour l'examen **Red Hat Certified OpenShift Application Developer (EX288)**.

Objectif du dépôt :
- transformer le guide PDF en **artefacts exécutables** ;
- fournir des **labs chronométrés** avec manifests, templates, chart Helm, scripts S2I et ressources Tekton ;
- offrir une progression orientée **résultat observable**, fidèle à l'esprit de l'examen.

> Référence de version de travail : OpenShift 4.18  
> Dernière mise à jour du dépôt : 2026-04-07

## Structure

- `docs/` : cadrage, stratégie d'examen, checklist, runbook de dépannage.
- `shared/` : applications de démonstration, chart Helm, templates, scripts communs.
- `labs/01-...` à `labs/14-...` : labs chronométrés et mocks d'examen.
- `scripts/` : scripts utilitaires pour préparer l'environnement.

## Labs actuellement prêts à exécuter

Les labs suivants contiennent des manifests et ressources directement exploitables :
- `01-foundations-services-routes`
- `02-configmaps-secrets-probes`
- `03-imagestream-buildconfig-containerfile`
- `04-custom-s2i`
- `05-triggers-hooks`
- `06-templates`
- `07-helm-kustomize`
- `08-tekton-pipelines`
- `09-operator-consumption`
- `10-registry-internal`
- `11-rbac-debug`
- `12-initcontainer-bluegreen`

Les répertoires `13-mock-exam-a` et `14-mock-exam-b` fournissent des sujets complets de simulation 3h.

## Démarrage rapide

1. Se connecter au cluster :
   ```bash
   oc login <api-url> -u <user> -p <password>
   oc whoami
   oc version
   ```
2. Vérifier les prérequis :
   ```bash
   ./scripts/check-prereqs.sh
   ```
3. Commencer par :
   ```bash
   cd labs/01-foundations-services-routes
   cat README.md
   ```

## Philosophie

Ce dépôt ne cherche pas à reproduire mot pour mot l'examen.  
Il cherche à muscler les gestes utiles :
- créer vite ;
- diagnostiquer vite ;
- corriger proprement ;
- revérifier immédiatement.
