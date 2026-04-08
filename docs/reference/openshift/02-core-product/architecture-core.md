# Architecture Core d'OpenShift

## Objectif

Cette section approfondit l\'architecture d\'OpenShift en décrivant les composants clés du control plane et des nœuds worker, ainsi que leurs interactions. Comprendre cette architecture est fondamental pour l\'administration, le dépannage et l\'optimisation d\'un cluster.

## Concepts

L\'architecture d\'OpenShift repose sur Kubernetes et y ajoute des dizaines de composants pour offrir une plateforme de conteneurs complète.

### Control Plane

Le control plane est le cerveau du cluster. Il est généralement réparti sur 3 nœuds maîtres pour la haute disponibilité.

| Composant | Description |
|---|---|
| **API Server (kube-apiserver)** | Point d\'entrée central pour toutes les opérations de gestion du cluster. Valide et traite les requêtes REST. |
| **etcd** | Base de données clé-valeur distribuée qui stocke l\'état complet du cluster. Source de vérité unique. |
| **Scheduler (kube-scheduler)** | Assigne les nouveaux pods aux nœuds worker en fonction des ressources disponibles et des contraintes. |
| **Controller Manager (kube-controller-manager)** | Exécute les contrôleurs qui régulent l\'état du cluster (par ex., contrôleur de réplication, contrôleur de nœud). |
| **OpenShift API Server** | Fournit les API spécifiques à OpenShift (par ex., pour les `Routes`, `Projects`, `Builds`). |
| **OpenShift Controller Manager** | Exécute les contrôleurs spécifiques à OpenShift (par ex., contrôleur de projet, contrôleur de route). |

### Nœuds Worker

Les nœuds worker exécutent les charges de travail des applications.

| Composant | Description |
|---|---|
| **Kubelet** | Agent qui s\'exécute sur chaque nœud. S\'assure que les conteneurs décrits dans les PodSpecs sont en cours d\'exécution et en bonne santé. |
| **Container Runtime (CRI-O)** | Moteur d\'exécution de conteneurs qui gère le cycle de vie des conteneurs (tirer les images, démarrer/arrêter les conteneurs). OpenShift utilise CRI-O. |
| **Kube-proxy** | Gère la communication réseau à l\'intérieur et à l\'extérieur du cluster. Maintient les règles réseau sur les nœuds. |

### Diagramme d\'Architecture Simplifié

```mermaid
flowchart TD
    subgraph Control Plane Nodes
        direction LR
        etcd[etcd]
        api[API Server]
        sched[Scheduler]
        cm[Controller Manager]
    end

    subgraph Worker Node 1
        direction TB
        kubelet1[Kubelet]
        cri-o1[CRI-O]
        proxy1[Kube-proxy]
        pod1[Pod A] --- cri-o1
        pod2[Pod B] --- cri-o1
    end

    subgraph Worker Node 2
        direction TB
        kubelet2[Kubelet]
        cri-o2[CRI-O]
        proxy2[Kube-proxy]
        pod3[Pod C] --- cri-o2
    end

    user[User/Admin] -- oc/kubectl --> api
    api <--> etcd
    api -- Watch --> sched
    api -- Watch --> cm
    api -- Instructs --> kubelet1
    api -- Instructs --> kubelet2
```

### Diagramme d'Architecture Complète avec Opérateurs

```mermaid
graph TB
    subgraph "Control Plane (HA - 3 nœuds)"
        API["API Server<br/>(kube-apiserver + openshift-apiserver)"]
        ETCD[("etcd<br/>(Distributed Key-Value Store)")]
        SCHED["Scheduler<br/>(kube-scheduler)"]
        CM["Controller Manager<br/>(kube + openshift)"]
        OLM["Operator Lifecycle Manager<br/>(OLM)"]
    end

    subgraph "Infrastructure Services"
        ROUTER["Ingress Router<br/>(HAProxy)"]
        REGISTRY["Internal Registry<br/>(Quay/Image Registry)"]
        MONITOR["Monitoring Stack<br/>(Prometheus + Grafana)"]
        DNS["DNS<br/>(CoreDNS)"]
    end

    subgraph "Worker Node 1"
        KUBELET1["Kubelet"]
        CRIO1["CRI-O Runtime"]
        PROXY1["Kube-proxy"]
        SDN1["SDN/OVN Plugin"]
        POD1A["Pod: App A"]
        POD1B["Pod: App B"]
    end

    subgraph "Worker Node 2"
        KUBELET2["Kubelet"]
        CRIO2["CRI-O Runtime"]
        PROXY2["Kube-proxy"]
        SDN2["SDN/OVN Plugin"]
        POD2A["Pod: App C"]
    end

    subgraph "Storage Layer"
        PV["Persistent Volumes<br/>(NFS, iSCSI, Ceph, Cloud)"]
    end

    USER["👤 User/Admin<br/>(oc/kubectl/Web Console)"] --> API
    API <--> ETCD
    API --> SCHED
    API --> CM
    API --> OLM
    OLM --> ROUTER
    OLM --> REGISTRY
    OLM --> MONITOR
    
    API --> KUBELET1
    API --> KUBELET2
    
    KUBELET1 --> CRIO1
    KUBELET2 --> CRIO2
    
    CRIO1 --> POD1A
    CRIO1 --> POD1B
    CRIO2 --> POD2A
    
    POD1A -.-> PV
    POD2A -.-> PV
    
    ROUTER --> POD1A
    ROUTER --> POD2A
    
    DNS --> POD1A
    DNS --> POD1B
    DNS --> POD2A
    
    MONITOR -."Scrape Metrics".-> KUBELET1
    MONITOR -."Scrape Metrics".-> KUBELET2
```

## Où chercher dans la documentation officielle

- **Architecture du Control Plane** : [https://docs.openshift.com/container-platform/latest/architecture/control-plane.html](https://docs.openshift.com/container-platform/latest/architecture/control-plane.html)
- **Architecture des nœuds Worker** : [https://docs.openshift.com/container-platform/latest/architecture/worker-nodes.html](https://docs.openshift.com/container-platform/latest/architecture/worker-nodes.html)
- **Composants du cluster** : [https://docs.openshift.com/container-platform/latest/architecture/understanding-the-architecture.html](https://docs.openshift.com/container-platform/latest/architecture/understanding-the-architecture.html)

## Commandes clés

```bash
# Lister les pods des composants du control plane
oc get pods -n openshift-kube-apiserver
oc get pods -n openshift-etcd
oc get pods -n openshift-kube-scheduler
oc get pods -n openshift-kube-controller-manager

# Afficher les logs d\'un composant du control plane
oc logs <pod-name> -n openshift-kube-apiserver

# Inspecter la configuration du kubelet sur un nœud
oc get node <node-name> -o json | jq .spec
```

## À retenir / Pièges fréquents

- **etcd est critique** : Une perte du quorum etcd signifie la perte du cluster. La sauvegarde d\'etcd est la tâche de maintenance la plus importante.
- **Le Kubelet est roi sur son nœud** : Le Kubelet est l\'agent principal qui gère tout sur un nœud worker. Si le Kubelet est en panne, le nœud est considéré comme `NotReady`.
- **CRI-O vs Docker** : OpenShift n\'utilise plus Docker comme moteur de conteneurs. Il utilise CRI-O, une implémentation légère de l\'interface CRI (Container Runtime Interface) de Kubernetes.
