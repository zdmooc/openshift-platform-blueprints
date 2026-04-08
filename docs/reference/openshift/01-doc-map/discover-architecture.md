# Architecture Discover

## Objectif

Cette section a pour but de vous présenter les concepts fondamentaux de l'architecture de Red Hat OpenShift Container Platform (OCP). Vous découvrirez les différents types de nœuds, leurs rôles et comment ils interagissent pour former un cluster OpenShift fonctionnel.

## Concepts

Un cluster OpenShift est composé de deux types de nœuds principaux :

- **Nœuds de contrôle (Control Plane Nodes)** : Ils hébergent les services qui gèrent le cluster. Ils sont responsables de la prise de décision, de la planification des pods, de la gestion de l'état du cluster, etc. Un cluster OpenShift de production nécessite trois nœuds de contrôle pour la haute disponibilité.
- **Nœuds de calcul (Worker Nodes)** : C'est là que les applications des utilisateurs s'exécutent. Les nœuds de calcul sont gérés par les nœuds de contrôle.

En plus de ces deux types de nœuds, il existe un troisième type de nœud :

- **Nœuds d'infrastructure (Infrastructure Nodes)** : Ce sont des nœuds de calcul spécialisés qui hébergent les services d'infrastructure du cluster, tels que le registre d'images, le routeur Ingress, le monitoring, etc. L'utilisation de nœuds d'infrastructure permet de séparer les charges de travail des utilisateurs des services du cluster.

## Où chercher dans la documentation officielle

Pour en savoir plus sur l'architecture d'OpenShift, consultez les sections suivantes de la documentation officielle :

- **Architecture du cluster** : [https://docs.openshift.com/container-platform/latest/architecture/cluster-architecture.html](https://docs.openshift.com/container-platform/latest/architecture/cluster-architecture.html)
- **Nœuds de contrôle** : [https://docs.openshift.com/container-platform/latest/architecture/control-plane.html](https://docs.openshift.com/container-platform/latest/architecture/control-plane.html)
- **Nœuds de calcul** : [https://docs.openshift.com/container-platform/latest/architecture/worker-nodes.html](https://docs.openshift.com/container-platform/latest/architecture/worker-nodes.html)

## Commandes clés

Voici quelques commandes `oc` et `kubectl` utiles pour explorer l'architecture de votre cluster :

```bash
# Lister tous les nœuds du cluster
oc get nodes

# Obtenir des informations détaillées sur un nœud spécifique
oc describe node <node-name>

# Lister les pods qui s'exécutent sur les nœuds de contrôle
oc get pods -n openshift-kube-apiserver
oc get pods -n openshift-etcd
oc get pods -n openshift-kube-controller-manager
oc get pods -n openshift-kube-scheduler
```

## À retenir / Pièges fréquents

- **Ne pas exécuter de charges de travail utilisateur sur les nœuds de contrôle** : Les nœuds de contrôle sont essentiels au bon fonctionnement du cluster. L'exécution de charges de travail utilisateur sur ces nœuds peut entraîner des problèmes de performance et de stabilité.
- **Utiliser des nœuds d'infrastructure pour les services partagés** : Cela permet d'isoler les services du cluster des applications des utilisateurs et d'améliorer la sécurité et la stabilité.
- **Comprendre le rôle de chaque composant du control plane** : Chaque composant (API server, etcd, scheduler, controller manager) a un rôle spécifique. Comprendre ces rôles est essentiel pour le dépannage et la gestion avancée du cluster.
