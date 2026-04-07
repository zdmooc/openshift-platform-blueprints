# CertifOpenShift

Dépôt de travail pour structurer l'apprentissage des certifications OpenShift et des certifications adjacentes les plus utiles autour de Red Hat OpenShift.

## Objectif

Donner un sens d'ensemble au parcours certification :
- comprendre la logique globale ;
- voir les dépendances entre certifications ;
- disposer d'un espace dédié par certification ;
- préparer plus tard des labs, des notes, des checklists et des plans de révision.

## Logique du dépôt

Ce dépôt mélange deux familles :

1. **Certifications OpenShift officielles / directement présentes dans les parcours OpenShift Red Hat**
2. **Certifications adjacentes mais très utiles** pour compléter un positionnement administrateur, développeur, architecte, sécurité, multicluster, IA ou event-driven.

## Parcours globaux proposés

### 1. Parcours Architecte OpenShift
`EX180 -> EX280 -> EX380 -> EX430 / EX432 / EX370 -> EX229`

### 2. Parcours Virtualization
`EX280 -> EX156 (optionnel) -> EX316 -> EX336`

### 3. Parcours Développeur OpenShift
`EX188 -> EX288 -> EX267 / EX378 / EX328 / EX482`

### 4. Parcours Architecte complet hybride
`EX280 + EX380 + EX430 + EX432 + EX370 + EX288 + EX482`

## Convention de structure

Chaque certification possède son répertoire dédié dans `certifications/`, avec :
- un README de cadrage ;
- une feuille de route de préparation ;
- une proposition de labs ;
- un journal de notes.

## Répertoires principaux

- `README.md` : point d'entrée global
- `CERTIFICATIONS_INDEX.md` : index de toutes les certifications suivies dans ce dépôt
- `GLOBAL/` : vision transverse, liens, parcours et principes
- `ROADMAPS/` : vues par profil cible
- `certifications/` : un sous-répertoire par certification

## Remarques

- Le dépôt est volontairement conçu comme une base évolutive.
- Les noms retenus s'appuient en priorité sur les parcours OpenShift Red Hat.
- Certaines pages Red Hat montrent des variations de libellé entre pages "skills path" et page RHCA ; le dépôt retient les dénominations les plus cohérentes avec les parcours OpenShift publics.

## Étape suivante suggérée

Compléter un premier dossier en profondeur, en général :
- `certifications/EX280/`
- puis `certifications/EX380/`
- puis `certifications/EX430/` ou `certifications/EX432/`
