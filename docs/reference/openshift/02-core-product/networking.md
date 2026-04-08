# Networking

## Objectif

Cette section couvre les concepts fondamentaux du réseau dans OpenShift. Elle explique comment les pods communiquent entre eux et avec le monde extérieur, et comment sécuriser ces communications.

## Concepts

### Software-Defined Networking (SDN)

OpenShift utilise un SDN pour créer un réseau virtuel pour les pods et les services. Le SDN par défaut est **OpenShift SDN**, qui est basé sur Open vSwitch (OVS). Il offre trois modes :

- **`network-policy` (par défaut)** : Mode le plus sécurisé. Il active les `NetworkPolicy` pour isoler les projets.
- **`multitenant`** : Isole complètement les projets les uns des autres.
- **`subnet`** : Mode le plus simple où tous les pods peuvent communiquer entre eux à travers tous les projets.

### Communication Pod-à-Pod

Chaque pod a sa propre adresse IP unique au sein du cluster. Le SDN garantit que les pods peuvent communiquer directement entre eux, même s'ils sont sur des nœuds différents.

### Services

Les services fournissent un point d'accès stable pour un groupe de pods. `kube-proxy` sur chaque nœud programme les règles réseau (iptables ou IPVS) pour router le trafic destiné à l'IP d'un service vers l'un des pods correspondants.

### Ingress Controller & Routes

L'**Ingress Controller** est un routeur qui gère tout le trafic externe entrant dans le cluster. Il est généralement déployé sur les nœuds d'infrastructure. Il lit les objets `Route` et configure le routage en conséquence.

### Network Policies

Les **Network Policies** sont des règles de pare-feu pour les pods. Elles permettent de définir de manière granulaire quels pods peuvent communiquer avec quels autres pods. Par défaut, dans un projet, tous les pods peuvent communiquer entre eux, mais les `NetworkPolicy` peuvent restreindre ce comportement.

### Diagramme : Architecture Réseau OpenShift SDN

```mermaid
graph TB
    subgraph "Utilisateurs Externes"
        USER1["🌍 Client HTTPS"]
        USER2["🌍 Client HTTP"]
    end

    subgraph "Ingress Layer"
        LB["Load Balancer<br/>(Cloud ou externe)"]
        USER1 --> LB
        USER2 --> LB
        
        LB --> ROUTER1["Ingress Router Pod 1<br/>(HAProxy)<br/>Nœud Infra 1"]
        LB --> ROUTER2["Ingress Router Pod 2<br/>(HAProxy)<br/>Nœud Infra 2"]
    end

    subgraph "Nœud Worker 1 - 10.128.0.0/24"
        OVS1["Open vSwitch (OVS)"]
        VXLAN1["VXLAN Tunnel"]
        
        POD1A["📦 Pod A<br/>10.128.0.5<br/>Project: dev"]
        POD1B["📦 Pod B<br/>10.128.0.6<br/>Project: dev"]
        
        OVS1 --> POD1A
        OVS1 --> POD1B
    end

    subgraph "Nœud Worker 2 - 10.129.0.0/24"
        OVS2["Open vSwitch (OVS)"]
        VXLAN2["VXLAN Tunnel"]
        
        POD2A["📦 Pod C<br/>10.129.0.5<br/>Project: prod"]
        POD2B["📦 Pod D<br/>10.129.0.6<br/>Project: prod"]
        
        OVS2 --> POD2A
        OVS2 --> POD2B
    end

    subgraph "Service Layer"
        SVC1["Service: myapp<br/>ClusterIP: 172.30.1.100<br/>Project: dev"]
        SVC2["Service: webapp<br/>ClusterIP: 172.30.2.50<br/>Project: prod"]
        
        SVC1 -."Load Balance".-> POD1A
        SVC1 -."Load Balance".-> POD1B
        SVC2 -."Load Balance".-> POD2A
    end

    ROUTER1 --> SVC1
    ROUTER1 --> SVC2
    ROUTER2 --> SVC1
    ROUTER2 --> SVC2

    OVS1 <-->|"VXLAN Overlay"| OVS2
    
    POD1A -."Peut communiquer<br/>(même projet)".-> POD1B
    POD1A -."Bloqué par<br/>NetworkPolicy".-> POD2A

    style LB fill:#FF6B6B
    style ROUTER1 fill:#FFA500
    style ROUTER2 fill:#FFA500
    style SVC1 fill:#87CEEB
    style SVC2 fill:#87CEEB
    style OVS1 fill:#90EE90
    style OVS2 fill:#90EE90
```

### Diagramme : Exemple de NetworkPolicy

```mermaid
graph TD
    subgraph "Project: frontend"
        POD_FE["📦 Pod: web-ui<br/>Labels: app=frontend"]
    end

    subgraph "Project: backend"
        POD_API["📦 Pod: api-server<br/>Labels: app=api"]
        POD_DB["📦 Pod: database<br/>Labels: app=db"]
        
        NP["NetworkPolicy: allow-from-api<br/>PodSelector: app=db<br/>Ingress:<br/>- from: app=api<br/>  port: 5432"]
    end

    subgraph "Project: monitoring"
        POD_MON["📦 Pod: prometheus"]
    end

    POD_FE -->|" ✅ Autorisé<br/>HTTP:8080"| POD_API
    POD_API -->|" ✅ Autorisé<br/>PostgreSQL:5432"| POD_DB
    POD_FE -." ❌ Bloqué<br/>par NetworkPolicy".-> POD_DB
    POD_MON -." ❌ Bloqué<br/>par NetworkPolicy".-> POD_DB

    NP -."Applique la règle".-> POD_DB

    NOTE["Règle: Seul le pod 'api-server'<br/>peut accéder au pod 'database'<br/>sur le port 5432"]

    style POD_DB fill:#FFB6C1
    style NP fill:#FFD700
    style POD_API fill:#90EE90
```

## Où chercher dans la documentation officielle

- **Vue d'ensemble du réseau** : [https://docs.openshift.com/container-platform/latest/networking/understanding-networking.html](https://docs.openshift.com/container-platform/latest/networking/understanding-networking.html)
- **OpenShift SDN** : [https://docs.openshift.com/container-platform/latest/networking/openshift_sdn/about-openshift-sdn.html](https://docs.openshift.com/container-platform/latest/networking/openshift_sdn/about-openshift-sdn.html)
- **Network Policies** : [https://docs.openshift.com/container-platform/latest/networking/network_policy/about-network-policy.html](https://docs.openshift.com/container-platform/latest/networking/network_policy/about-network-policy.html)

## Commandes clés

```bash
# Voir la configuration réseau du cluster
oc get network.config.openshift.io cluster -o yaml

# Lister les NetworkPolicies dans le projet courant
oc get networkpolicy

# Créer une NetworkPolicy à partir d'un fichier YAML
oc create -f my-network-policy.yaml

# Lister les pods et leurs adresses IP
oc get pods -o wide

# Lister les services et leurs adresses IP de cluster
oc get services
```

## À retenir / Pièges fréquents

- **Le mode SDN est immuable** : Le mode de l'OpenShift SDN est défini à l'installation et ne peut pas être changé par la suite.
- **La politique par défaut est `allow-all`** : Au sein d'un projet, si aucune `NetworkPolicy` n'est appliquée, tous les pods peuvent communiquer entre eux. La première `NetworkPolicy` appliquée à un pod change ce comportement en `deny-all` (sauf ce qui est explicitement autorisé).
- **Isolation des projets** : L'isolation entre les projets est une fonctionnalité clé du SDN d'OpenShift. Comprenez comment votre mode SDN gère cette isolation.
- **DNS du cluster** : OpenShift dispose d'un DNS interne qui permet aux pods de se trouver en utilisant les noms des services. Par exemple, un pod peut atteindre un service nommé `database` dans le même projet en utilisant simplement l'adresse `database`.
