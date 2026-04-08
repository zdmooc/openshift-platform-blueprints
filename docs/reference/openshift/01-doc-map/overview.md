# Vue d'ensemble de la Documentation OpenShift

## Objectif

Cette section a pour but de vous donner une vue d'ensemble de la documentation officielle de Red Hat OpenShift Container Platform (OCP). Elle vous aidera à comprendre comment la documentation est structurée, où trouver les informations dont vous avez besoin et comment naviguer efficacement à travers les différentes versions.

## Concepts

La documentation OpenShift est vaste et couvre un large éventail de sujets. Elle est organisée par version majeure et mineure d'OCP (par exemple, 4.16, 4.18, 4.19). Chaque version de la documentation est un ensemble complet de guides et de références.

Les principaux types de documents que vous rencontrerez sont :

- **Guides d'installation** : Instructions détaillées pour déployer OpenShift sur différentes plateformes (Bare Metal, vSphere, AWS, etc.).
- **Guides d'administration** : Tâches courantes de gestion, de configuration et de maintenance du cluster.
- **Guides de développement** : Informations pour les développeurs qui créent et déploient des applications sur OpenShift.
- **Référence d'architecture** : Explications approfondies sur les composants et les concepts fondamentaux d'OpenShift.
- **Notes de version** : Nouveautés, bogues corrigés et problèmes connus pour chaque version.

## Où chercher dans la documentation officielle

La documentation officielle est la source de vérité pour tout ce qui concerne OpenShift. Voici les liens principaux :

- **Portail de la documentation Red Hat** : [https://docs.redhat.com/en/documentation/openshift_container_platform](https://docs.redhat.com/en/documentation/openshift_container_platform)
- **Documentation OpenShift (nouvelle interface)** : [https://docs.openshift.com/container-platform/](https://docs.openshift.com/container-platform/)

## Commandes clés

Il n'y a pas de commandes spécifiques pour naviguer dans la documentation, mais voici quelques commandes `oc` et `kubectl` utiles pour obtenir des informations sur votre cluster, ce qui peut vous aider à trouver la bonne documentation :

```bash
# Obtenir la version du cluster OpenShift
oc version

# Obtenir des informations sur les opérateurs du cluster
oc get clusteroperators
```

## À retenir / Pièges fréquents

- **Vérifiez toujours la version** : Assurez-vous que vous consultez la documentation correspondant à la version de votre cluster OpenShift.
- **Utilisez la recherche** : La fonction de recherche sur le portail de documentation est puissante. Utilisez des mots-clés précis pour trouver rapidement ce que vous cherchez.
- **Ne négligez pas les notes de version** : Elles contiennent des informations cruciales sur les changements, les dépréciations et les problèmes connus.
