# Glossaire du Licensing OpenShift

## Objectif

Cette section définit les termes clés liés au licensing et à la souscription de Red Hat OpenShift. Comprendre ce vocabulaire est essentiel pour naviguer dans les discussions commerciales et techniques sur le coût et la valeur d'OpenShift.

## Termes Clés

| Terme | Définition |
|---|---|
| **Souscription (Subscription)** | Un contrat avec Red Hat qui donne droit à l'accès aux logiciels, aux mises à jour, aux correctifs de sécurité et au support technique. Le licensing d'OpenShift est basé sur des souscriptions. |
| **Core** | Une unité de traitement physique dans un CPU. Le licensing d'OpenShift est principalement basé sur le nombre de cores. |
| **vCPU (virtual CPU)** | Un CPU virtuel assigné à une machine virtuelle. Dans le contexte du licensing OpenShift, 2 vCPU sont généralement équivalents à 1 core physique. |
| **Nœud (Node)** | Une machine (physique ou virtuelle) qui fait partie du cluster OpenShift. On distingue les nœuds de control plane (maîtres) et les nœuds worker. |
| **Cluster** | Un ensemble de nœuds qui exécutent OpenShift. |
| **Socket** | Un connecteur physique sur une carte mère qui accueille un CPU. Un CPU peut contenir plusieurs cores. |
| **Red Hat OpenShift Platform Plus** | L'édition la plus complète d'OpenShift, qui inclut Advanced Cluster Management (ACM), Advanced Cluster Security (ACS) et Quay. |
| **Red Hat OpenShift Kubernetes Engine (OKE)** | Une édition basique d'OpenShift qui fournit uniquement les fonctionnalités essentielles de Kubernetes. |
| **Red Hat OpenShift Container Platform (OCP)** | L'édition standard d'OpenShift, qui inclut toutes les fonctionnalités de la plateforme de conteneurs. |
| **Managed OpenShift** | Des offres OpenShift gérées par des fournisseurs de cloud, comme **ROSA** (Red Hat OpenShift Service on AWS), **ARO** (Azure Red Hat OpenShift) et **ROKS** (Red Hat OpenShift on IBM Cloud). |

## Où chercher dans la documentation officielle

- **Guide des souscriptions OpenShift** : [https://www.redhat.com/en/resources/openshift-subscription-guide-detail](https://www.redhat.com/en/resources/openshift-subscription-guide-detail)

## À retenir / Pièges fréquents

- **Core vs vCPU** : La conversion entre cores physiques et vCPU est un point clé à comprendre pour le licensing sur des environnements virtualisés.
- **Les souscriptions couvrent tout** : Une souscription OpenShift inclut le système d'exploitation (Red Hat CoreOS) et tous les composants de la plateforme. Vous n'avez pas besoin de souscriptions séparées pour RHEL sur vos nœuds CoreOS.
- **Les éditions ont des fonctionnalités différentes** : Assurez-vous de choisir l'édition d'OpenShift qui correspond à vos besoins. OCP est le choix le plus courant, mais OKE peut être suffisant pour des besoins basiques, et Platform Plus est nécessaire pour la gestion multi-cluster et la sécurité avancée.
