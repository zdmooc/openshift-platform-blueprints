# Stockage

## Objectif

Cette section explique comment les applications peuvent demander et utiliser du stockage persistant dans OpenShift. Elle couvre les concepts de Volumes Persistants (PV), de Revendications de Volumes Persistants (PVC) et de Classes de Stockage (StorageClasses).

## Concepts

La gestion du stockage dans Kubernetes et OpenShift est basée sur une séparation claire des responsabilités entre les administrateurs de cluster et les développeurs.

| Objet | Description | Qui le gère ? |
|---|---|---|
| **PersistentVolume (PV)** | Un morceau de stockage dans le cluster qui a été provisionné par un administrateur. C\"est une ressource du cluster, comme un nœud. | Administrateur |
| **PersistentVolumeClaim (PVC)** | Une demande de stockage par un utilisateur. C\"est comme un pod qui consomme des ressources de nœud ; un PVC consomme des ressources de PV. | Développeur |
| **StorageClass** | Fournit un moyen pour les administrateurs de décrire les "classes" de stockage qu\"ils offrent. Différentes classes peuvent correspondre à des niveaux de service (par ex., `rapide`, `lent`) ou à des politiques de sauvegarde. | Administrateur |

### Provisionnement Dynamique

Le provisionnement dynamique permet de créer des volumes de stockage à la demande. Lorsqu\"un développeur crée un PVC, s\"il n\"y a pas de PV statique disponible qui correspond à la demande, une `StorageClass` peut provisionner automatiquement un nouveau PV pour ce PVC.

- **Provisioner** : Chaque `StorageClass` a un `provisioner` qui détermine quel plugin de volume est utilisé pour provisionner les PV.

### Diagramme : Cycle de Vie du Stockage Persistant

```mermaid
flowchart TD
    subgraph "1️⃣ Configuration par l'Admin"
        ADMIN["👨‍💻 Administrateur"] --> SC["StorageClass<br/>name: fast-ssd<br/>provisioner: kubernetes.io/aws-ebs<br/>parameters: type=gp3"]
    end

    subgraph "2️⃣ Demande par le Développeur"
        DEV["👩‍💻 Développeur"] --> PVC["PersistentVolumeClaim<br/>name: myapp-data<br/>storageClassName: fast-ssd<br/>size: 10Gi<br/>accessMode: RWO"]
    end

    subgraph "3️⃣ Provisionnement Dynamique"
        PVC -->|"Demande de stockage"| PROVISIONER["Provisioner<br/>(aws-ebs-csi-driver)"]
        PROVISIONER -->|"Crée"| PV["PersistentVolume<br/>name: pv-abc123<br/>capacity: 10Gi<br/>volumeHandle: vol-xyz"]
    end

    subgraph "4️⃣ Liaison (Binding)"
        PV <-->|"Bound"| PVC
    end

    subgraph "5️⃣ Utilisation par l'Application"
        POD["📦 Pod: myapp"] -->|"Monte le volume"| PVC
        PVC -."Accès au stockage".-> STORAGE["💾 Stockage Physique<br/>(AWS EBS Volume)"]
    end

    subgraph "6️⃣ Libération"
        DEL["🗑️ Suppression du PVC"] --> RECLAIM{"Reclaim Policy?"}
        RECLAIM -->|"Retain"| KEEP["PV conservé<br/>Données intactes"]
        RECLAIM -->|"Delete"| DELETE["PV et volume supprimés<br/>Données perdues"]
        RECLAIM -->|"Recycle"| CLEAN["PV nettoyé<br/>Réutilisable"]
    end

    style SC fill:#FFD700
    style PVC fill:#87CEEB
    style PV fill:#90EE90
    style STORAGE fill:#FFB6C1
```

### Diagramme : Modes d'Accès au Stockage

```mermaid
graph TD
    subgraph "ReadWriteOnce (RWO)"
        RWO_PVC["PVC: RWO<br/>1 seul nœud à la fois"]
        RWO_PVC --> NODE1["🖥️ Nœud 1"]
        NODE1 --> POD1A["📦 Pod A"]
        NODE1 --> POD1B["📦 Pod B"]
        NODE2["🖥️ Nœud 2"] -."Accès refusé".-> RWO_PVC
        NOTE_RWO["Cas d'usage:<br/>Bases de données<br/>Stockage bloc (EBS, iSCSI)"]
    end

    subgraph "ReadWriteMany (RWX)"
        RWX_PVC["PVC: RWX<br/>Plusieurs nœuds simultanément"]
        RWX_PVC --> NODE3["🖥️ Nœud 1"]
        RWX_PVC --> NODE4["🖥️ Nœud 2"]
        NODE3 --> POD3A["📦 Pod A"]
        NODE4 --> POD4A["📦 Pod B"]
        NOTE_RWX["Cas d'usage:<br/>Fichiers partagés<br/>NFS, CephFS"]
    end

    subgraph "ReadOnlyMany (ROX)"
        ROX_PVC["PVC: ROX<br/>Lecture seule sur plusieurs nœuds"]
        ROX_PVC --> NODE5["🖥️ Nœud 1"]
        ROX_PVC --> NODE6["🖥️ Nœud 2"]
        NODE5 --> POD5A["📦 Pod A (Read)"]
        NODE6 --> POD6A["📦 Pod B (Read)"]
        NOTE_ROX["Cas d'usage:<br/>Données statiques<br/>Configuration partagée"]
    end

    style RWO_PVC fill:#FFD700
    style RWX_PVC fill:#90EE90
    style ROX_PVC fill:#87CEEB
```

## Où chercher dans la documentation officielle

- **Comprendre le stockage persistant** : [https://docs.openshift.com/container-platform/latest/storage/understanding-persistent-storage.html](https://docs.openshift.com/container-platform/latest/storage/understanding-persistent-storage.html)
- **Provisionnement dynamique** : [https://docs.openshift.com/container-platform/latest/storage/dynamic-provisioning.html](https://docs.openshift.com/container-platform/latest/storage/dynamic-provisioning.html)

## Commandes clés

```bash
# Lister les StorageClasses
oc get storageclass
oc get sc

# Lister les PersistentVolumes
oc get persistentvolume
oc get pv

# Lister les PersistentVolumeClaims dans le projet courant
oc get persistentvolumeclaim
oc get pvc

# Créer un PVC à partir d\"un fichier YAML
oc create -f my-pvc.yaml

# Décrire un PV pour voir ses détails et son statut
oc describe pv <pv-name>

# Décrire un PVC pour voir à quel PV il est lié
oc describe pvc <pvc-name>
```

## À retenir / Pièges fréquents

- **Modes d\"accès (Access Modes)** : Un PV peut être monté de différentes manières : `ReadWriteOnce` (RWO - monté en lecture/écriture par un seul nœud), `ReadOnlyMany` (ROX - monté en lecture seule par plusieurs nœuds), et `ReadWriteMany` (RWX - monté en lecture/écriture par plusieurs nœuds). Tous les types de stockage ne supportent pas tous les modes.
- **Politique de récupération (Reclaim Policy)** : La `reclaimPolicy` d\"un PV indique au cluster quoi faire du volume après qu\"il a été libéré de sa revendication. Les options sont `Retain` (garder le volume), `Recycle` (déprécié) et `Delete` (supprimer le volume).
- **Binding** : Un PVC se lie à un PV. Pour que le binding réussisse, le PV doit satisfaire les exigences du PVC (taille, mode d\"accès). Dans le cas du provisionnement dynamique, le PV est créé pour correspondre exactement au PVC.
- **Configurer une `StorageClass` par défaut** : Il est crucial d\"avoir une `StorageClass` par défaut pour que le provisionnement dynamique fonctionne de manière transparente pour les développeurs.
