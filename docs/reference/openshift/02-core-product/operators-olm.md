# Operators & OLM

## Objectif

Cette section présente le concept d'Operators et comment l'Operator Lifecycle Manager (OLM) simplifie le déploiement et la gestion des applications complexes sur OpenShift.

## Concepts

### Operators

Un **Operator** est une méthode de packaging, de déploiement et de gestion d'une application Kubernetes. C'est un contrôleur spécifique à une application qui étend l'API Kubernetes pour créer, configurer et gérer des instances d'applications complexes pour le compte d'un utilisateur.

Un Operator encode la connaissance opérationnelle humaine d'un service dans un logiciel. Par exemple, un Operator de base de données pourrait automatiser des tâches comme la sauvegarde, la restauration, le redimensionnement et la mise à jour de la base de données.

### Operator Lifecycle Manager (OLM)

L'**OLM** est un composant d'OpenShift qui gère le cycle de vie des Operators dans un cluster. Il s'occupe de l'installation, de la mise à jour et de la gestion des dépendances des Operators.

| Objet OLM | Description |
|---|---|
| **OperatorHub** | Une collection d'Operators prêts à être installés, disponible directement dans la console web d'OpenShift. |
| **Subscription** | Un objet qui exprime l'intention d'installer un Operator. Il spécifie le canal de mise à jour et la politique d'approbation. |
| **InstallPlan** | Créé par l'OLM en réponse à une `Subscription`. Il décrit l'ensemble des ressources qui doivent être créées pour installer ou mettre à jour un Operator. |
| **ClusterServiceVersion (CSV)** | Représente une version spécifique d'un Operator. Il contient les métadonnées (icône, description) et les définitions techniques (CRD, déploiements, RBAC) nécessaires pour exécuter l'Operator. |

### Custom Resource Definitions (CRD)

Les Operators fonctionnent en définissant leurs propres types d'objets via des **Custom Resource Definitions (CRD)**. Par exemple, l'Operator Prometheus définit une CRD `Prometheus` qui permet de créer une instance de Prometheus en créant simplement un objet `Prometheus`.

### Diagramme : Cycle de Vie d'un Operator avec OLM

```mermaid
flowchart TD
    START["👨‍💻 Admin cherche un Operator"] --> OPERATORHUB["🏪 OperatorHub<br/>(Catalogue d'Operators)"]
    
    OPERATORHUB --> SELECT["Sélectionner Operator<br/>Ex: PostgreSQL Operator"]
    
    SELECT --> CREATE_SUB["Créer Subscription<br/>Channel: stable<br/>Approval: Automatic"]
    
    CREATE_SUB --> OLM[" ⚙️ OLM détecte la Subscription"]
    
    OLM --> CREATE_IP["OLM crée InstallPlan<br/>(Liste des ressources à installer)"]
    
    CREATE_IP --> APPROVAL{"Approval Mode?"}
    APPROVAL -->|"Automatic"| INSTALL
    APPROVAL -->|"Manual"| WAIT_APPROVAL[" ⏸️ Attente approbation manuelle"]
    WAIT_APPROVAL --> ADMIN_APPROVE["👨‍💻 Admin approuve"]
    ADMIN_APPROVE --> INSTALL
    
    INSTALL["OLM installe les ressources<br/>- CRDs<br/>- ClusterServiceVersion (CSV)<br/>- Deployment de l'Operator<br/>- RBAC"]
    
    INSTALL --> CSV_READY["CSV: Succeeded<br/>Operator opérationnel"]
    
    CSV_READY --> USER_CREATE[" 👩‍💻 Utilisateur crée Custom Resource<br/>Ex: PostgreSQL CR"]
    
    USER_CREATE --> OPERATOR_WATCH[" 👁️ Operator détecte le CR"]
    
    OPERATOR_WATCH --> OPERATOR_RECONCILE[" ♻️ Operator reconcile<br/>Crée Pods, Services, PVCs, etc."]
    
    OPERATOR_RECONCILE --> APP_RUNNING[" ✅ Application opérationnelle<br/>(PostgreSQL cluster)"]
    
    CSV_READY --> UPDATE_AVAILABLE{"Nouvelle version<br/>disponible?"}
    UPDATE_AVAILABLE -->|"Oui"| NEW_IP["OLM crée nouvel InstallPlan"]
    NEW_IP --> APPROVAL2{"Approval?"}
    APPROVAL2 -->|"Automatic"| UPGRADE["Mise à jour automatique"]
    APPROVAL2 -->|"Manual"| WAIT_APPROVAL2[" ⏸️ Attente approbation"]
    WAIT_APPROVAL2 --> UPGRADE
    UPGRADE --> CSV_READY
    
    style OPERATORHUB fill:#87CEEB
    style CSV_READY fill:#90EE90
    style APP_RUNNING fill:#98FB98
```

### Diagramme : Architecture Operator Pattern

```mermaid
graph TB
    subgraph "Kubernetes API Server"
        API["API Server"]
    end
    
    subgraph "Custom Resources"
        CR1["PostgreSQL CR<br/>name: my-db<br/>replicas: 3<br/>version: 14"]
        CR2["PostgreSQL CR<br/>name: prod-db<br/>replicas: 5<br/>version: 15"]
    end
    
    subgraph "Operator Pod"
        CONTROLLER["Operator Controller<br/>(Reconciliation Loop)"]
        WATCH[" 👁️ Watch CRs"]
        RECONCILE[" ♻️ Reconcile Logic"]
        
        WATCH --> RECONCILE
    end
    
    subgraph "Managed Resources - my-db"
        STS1["StatefulSet<br/>my-db-0, my-db-1, my-db-2"]
        SVC1["Service<br/>my-db"]
        PVC1["PVCs<br/>data-my-db-0/1/2"]
        CM1["ConfigMap<br/>postgresql.conf"]
    end
    
    subgraph "Managed Resources - prod-db"
        STS2["StatefulSet<br/>prod-db-0 ... prod-db-4"]
        SVC2["Service<br/>prod-db"]
        PVC2["PVCs<br/>data-prod-db-0/1/2/3/4"]
    end
    
    CR1 --> API
    CR2 --> API
    API -->|"Watch Events"| WATCH
    
    RECONCILE -->|"Desired State"| CR1
    RECONCILE -->|"Current State"| STS1
    RECONCILE -->|"Create/Update"| API
    
    API --> STS1
    API --> SVC1
    API --> PVC1
    API --> CM1
    API --> STS2
    API --> SVC2
    API --> PVC2
    
    NOTE["L'Operator surveille en continu<br/>et corrige tout écart entre<br/>l'état désiré et l'état actuel"]
    
    style CONTROLLER fill:#FFD700
    style CR1 fill:#87CEEB
    style CR2 fill:#87CEEB
    style STS1 fill:#90EE90
    style STS2 fill:#90EE90
```

## Où chercher dans la documentation officielle

- **Comprendre les Operators** : [https://docs.openshift.com/container-platform/latest/operators/understanding/operators-understanding.html](https://docs.openshift.com/container-platform/latest/operators/understanding/operators-understanding.html)
- **Gestion des Operators avec OLM** : [https://docs.openshift.com/container-platform/latest/operators/olm-managing-operators.html](https://docs.openshift.com/container-platform/latest/operators/olm-managing-operators.html)

## Commandes clés

```bash
# Lister les Operators disponibles dans OperatorHub
oc get packagemanifests -n openshift-marketplace

# Lister les Operators installés dans un projet
oc get subscriptions

# Lister les ClusterServiceVersions (versions d'Operators installées)
oc get clusterserviceversions
oc get csv

# Approuver un plan d'installation manuel
oc patch installplan <installplan-name> --type merge --patch '{"spec":{"approved":true}}'

# Créer une ressource personnalisée (CR) pour déployer une application
# (Exemple pour l'Operator etcd)
oc create -f etcd-cluster.yaml
```

## À retenir / Pièges fréquents

- **Les Operators simplifient la complexité** : Le but principal des Operators est de rendre les applications complexes aussi faciles à gérer que les services cloud natifs.
- **OperatorHub est votre ami** : Avant de déployer manuellement une application complexe (par ex., une base de données, une file de messages), vérifiez si un Operator existe dans OperatorHub.
- **Canaux de mise à jour** : Faites attention au canal de mise à jour que vous choisissez dans votre `Subscription`. Il détermine la rapidité avec laquelle vous recevrez les nouvelles versions de l'Operator.
- **Dépendances** : L'OLM gère les dépendances entre les Operators. Si l'Operator A dépend de l'Operator B, l'OLM s'assurera que l'Operator B est installé et à la bonne version.
