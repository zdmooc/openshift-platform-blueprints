# Installation d'OpenShift

## Objectif

Cette section a pour but de vous guider à travers les différentes méthodes d'installation de Red Hat OpenShift Container Platform (OCP). Elle couvre les concepts clés, les prérequis et les liens vers la documentation officielle pour chaque type d'installation.

## Concepts

L'installation d'OpenShift peut être réalisée de deux manières principales :

- **Installer-Provisioned Infrastructure (IPI)** : L'installateur OpenShift provisionne et gère l'infrastructure sous-jacente (machines virtuelles, réseaux, etc.). C'est la méthode la plus simple et la plus automatisée, mais elle est limitée à certains fournisseurs de cloud (AWS, Azure, GCP, etc.).
- **User-Provisioned Infrastructure (UPI)** : Vous êtes responsable de la création et de la gestion de l'infrastructure. L'installateur OpenShift déploie ensuite le cluster sur cette infrastructure existante. Cette méthode offre plus de flexibilité et est utilisée pour les déploiements sur des infrastructures sur site (bare metal, vSphere, etc.).

### Diagramme : Méthodes d'Installation OpenShift

```mermaid
graph TD
    START["🚀 Installation OpenShift"] --> CHOICE{"Type d'infrastructure?"}
    
    CHOICE -->|"Cloud Public"| IPI["IPI<br/>(Installer-Provisioned Infrastructure)"]
    CHOICE -->|"On-Premise / Hybride"| UPI["UPI<br/>(User-Provisioned Infrastructure)"]
    CHOICE -->|"Edge / IoT"| ASSISTED["Assisted Installer<br/>(Interface Web)"]
    
    IPI --> IPI_CLOUDS{"Fournisseur Cloud?"}
    IPI_CLOUDS -->|"AWS"| IPI_AWS["☁️ AWS IPI<br/>✅ Automatique<br/>✅ Haute dispo intégrée"]
    IPI_CLOUDS -->|"Azure"| IPI_AZURE["☁️ Azure IPI<br/>✅ Automatique<br/>✅ Intégration Azure AD"]
    IPI_CLOUDS -->|"GCP"| IPI_GCP["☁️ GCP IPI<br/>✅ Automatique<br/>✅ Intégration GCP IAM"]
    IPI_CLOUDS -->|"OpenStack"| IPI_OSP["☁️ OpenStack IPI<br/>✅ Cloud privé"]
    
    UPI --> UPI_TYPES{"Plateforme?"}
    UPI_TYPES -->|"vSphere"| UPI_VSPHERE["💻 vSphere UPI<br/>⚠️ Infrastructure manuelle<br/>✅ Flexibilité maximale"]
    UPI_TYPES -->|"Bare Metal"| UPI_BM["🔧 Bare Metal UPI<br/>⚠️ Configuration réseau complexe<br/>✅ Performances maximales"]
    UPI_TYPES -->|"RHOSP"| UPI_RHOSP["🔴 RHOSP UPI<br/>⚠️ Infrastructure manuelle<br/>✅ Intégration Red Hat"]
    
    ASSISTED --> ASSISTED_FLOW["🌐 Assisted Installer<br/>1. Télécharger ISO<br/>2. Booter les serveurs<br/>3. Configurer via Web UI<br/>4. Validation automatique<br/>5. Installation lancée"]
    
    IPI_AWS --> RESULT["✅ Cluster OpenShift Opérationnel"]
    IPI_AZURE --> RESULT
    IPI_GCP --> RESULT
    IPI_OSP --> RESULT
    UPI_VSPHERE --> RESULT
    UPI_BM --> RESULT
    UPI_RHOSP --> RESULT
    ASSISTED_FLOW --> RESULT
    
    style IPI fill:#90EE90
    style UPI fill:#FFD700
    style ASSISTED fill:#87CEEB
    style RESULT fill:#98FB98
```

### Diagramme : Flux d'Installation IPI (AWS)

```mermaid
sequenceDiagram
    participant User as 👨‍💻 Utilisateur
    participant Installer as openshift-install
    participant AWS as ☁️ AWS API
    participant Cluster as 🔵 Cluster OpenShift
    
    User->>Installer: 1. openshift-install create install-config
    Installer->>User: install-config.yaml créé
    
    User->>User: 2. Éditer install-config.yaml<br/>(région, instance types, etc.)
    
    User->>Installer: 3. openshift-install create cluster
    
    Installer->>AWS: 4. Créer VPC, Subnets, Security Groups
    AWS-->>Installer: Infrastructure réseau créée
    
    Installer->>AWS: 5. Créer Load Balancers (API, Ingress)
    AWS-->>Installer: Load Balancers créés
    
    Installer->>AWS: 6. Lancer instances EC2 (Bootstrap, Masters, Workers)
    AWS-->>Installer: Instances en cours de démarrage
    
    Installer->>Cluster: 7. Bootstrap initialise le cluster
    Cluster-->>Installer: Control Plane opérationnel
    
    Installer->>AWS: 8. Supprimer instance Bootstrap
    AWS-->>Installer: Bootstrap supprimé
    
    Installer->>Cluster: 9. Configurer Operators (Ingress, Registry, etc.)
    Cluster-->>Installer: Operators opérationnels
    
    Installer->>User: ✅ Installation complète!<br/>kubeconfig et kubeadmin password fournis
    
    Note over User,Cluster: Durée totale: 30-45 minutes
```

## Où chercher dans la documentation officielle

La documentation d'installation est l'une des plus importantes. Voici les points d'entrée principaux :

- **Page principale de l'installation** : [https://docs.openshift.com/container-platform/latest/installing/index.html](https://docs.openshift.com/container-platform/latest/installing/index.html)
- **Installation sur AWS (IPI)** : [https://docs.openshift.com/container-platform/latest/installing/installing_aws/installing-aws-default.html](https://docs.openshift.com/container-platform/latest/installing/installing_aws/installing-aws-default.html)
- **Installation sur vSphere (UPI)** : [https://docs.openshift.com/container-platform/latest/installing/installing_vsphere/installing-vsphere.html](https://docs.openshift.com/container-platform/latest/installing/installing_vsphere/installing-vsphere.html)
- **Installation sur Bare Metal (UPI)** : [https://docs.openshift.com/container-platform/latest/installing/installing_bare_metal/installing-bare-metal.html](https://docs.openshift.com/container-platform/latest/installing/installing_bare_metal/installing-bare-metal.html)

## Commandes clés

L'installation d'OpenShift est principalement pilotée par l'outil `openshift-install`.

```bash
# Créer un fichier de configuration pour l'installation
openshift-install create install-config

# Créer les manifestes Kubernetes pour la personnalisation
openshift-install create manifests

# Lancer la création du cluster
openshift-install create cluster

# Détruire un cluster
openshift-install destroy cluster
```

## À retenir / Pièges fréquents

- **DNS** : La configuration DNS est l'un des points les plus critiques et les plus sujets aux erreurs lors de l'installation. Assurez-vous que les enregistrements DNS requis sont correctement configurés avant de lancer l'installation.
- **Prérequis** : Chaque type d'installation a des prérequis spécifiques en termes de ressources (CPU, RAM, stockage), de réseau et de permissions. Lisez attentivement la documentation avant de commencer.
- **Fichier `install-config.yaml`** : Ce fichier est le cœur de votre configuration d'installation. Sauvegardez-le précieusement, car il est nécessaire pour ajouter des nœuds au cluster ou pour le détruire.
