# Qu'est-ce qui est comptabilisé dans le licensing ?

## Objectif

Cette section clarifie précisément quelles ressources de calcul (cores/vCPU) sont comptabilisées dans les souscriptions OpenShift et lesquelles ne le sont pas. C'est un point crucial pour estimer correctement le coût d'un cluster.

## Ce qui est comptabilisé

En règle générale, **tous les nœuds sur lesquels des charges de travail utilisateur peuvent être exécutées (schedulable) nécessitent une souscription**.

- **Nœuds Worker** : C'est la principale ressource comptabilisée. Le nombre total de cores ou de vCPU de tous les nœuds worker est additionné pour déterminer le nombre de souscriptions nécessaires.

- **Nœuds d'Infrastructure (Infra Nodes)** : Si vous utilisez des nœuds dédiés pour exécuter des composants de l'infrastructure du cluster (comme le routeur Ingress, le registre d'images, la pile de monitoring), ces nœuds **sont également comptabilisés** et nécessitent des souscriptions.

## Ce qui n'est PAS comptabilisé

- **Nœuds de Control Plane (Maîtres)** : Les nœuds qui exécutent les composants du control plane (API server, etcd, scheduler, etc.) **ne sont pas comptabilisés** et ne nécessitent pas de souscriptions OpenShift. Red Hat les fournit "gratuitement" dans le cadre de la plateforme.

## Ratio Cores vs vCPU

Red Hat utilise un ratio standard pour convertir les vCPU en cores physiques :

**2 vCPU = 1 Core**

Une souscription OpenShift est généralement vendue par "2 cores". Donc, une souscription de 2 cores peut couvrir :

- 2 cores physiques
- 4 vCPU

## Exemple de calcul

Imaginons un cluster avec la configuration suivante :

- **3 Nœuds Maîtres** : 4 vCPU chacun (Total : 12 vCPU) -> **Non comptabilisés**
- **5 Nœuds Worker** : 8 vCPU chacun (Total : 40 vCPU)
- **2 Nœuds Infra** : 4 vCPU chacun (Total : 8 vCPU)

**Calcul du total de vCPU à souscrire :**

Total vCPU = vCPU des Workers + vCPU des Nœuds Infra
Total vCPU = 40 + 8 = 48 vCPU

**Conversion en cores :**

Total Cores = Total vCPU / 2
Total Cores = 48 / 2 = 24 Cores

**Nombre de souscriptions (vendues par pack de 2 cores) :**

Nombre de souscriptions = Total Cores / 2
Nombre de souscriptions = 24 / 2 = 12 souscriptions

## Où chercher dans la documentation officielle

- **Guide des souscriptions OpenShift** : Ce document est la source de vérité pour les règles de licensing. [https://www.redhat.com/en/resources/openshift-subscription-guide-detail](https://www.redhat.com/en/resources/openshift-subscription-guide-detail)

## À retenir / Pièges fréquents

- **N'oubliez pas les nœuds Infra** : Un piège courant est d'oublier de compter les nœuds d'infrastructure dans le calcul des souscriptions.
- **Le SMT/Hyper-Threading ne compte pas (généralement)** : Le licensing est basé sur les cores physiques, pas sur les threads logiques. Un core avec 2 threads compte comme 1 core.
- **Les règles peuvent changer** : Les politiques de licensing peuvent évoluer. Référez-vous toujours au guide des souscriptions le plus récent de Red Hat.
