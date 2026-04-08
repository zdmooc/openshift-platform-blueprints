# Registre d'Images & Gestion des Images

## Objectif

Cette section explique comment OpenShift gère les images de conteneurs, y compris le registre d'images intégré, les ImageStreams et les stratégies de build pour créer des images à partir du code source.

## Concepts

### Registre d'Images Intégré

OpenShift inclut un **registre d'images intégré** qui stocke les images de conteneurs créées par les builds ou poussées manuellement. Ce registre est géré par l'**Image Registry Operator**.

- **Stockage** : Le registre nécessite un stockage persistant (par ex., NFS, S3, Azure Blob).
- **Sécurité** : L'accès au registre est contrôlé par RBAC. Seuls les utilisateurs autorisés peuvent pousser ou tirer des images.
- **Haute disponibilité** : Le registre peut être déployé en mode HA avec plusieurs réplicas.

### ImageStreams

Un **ImageStream** est un objet spécifique à OpenShift qui fournit une abstraction au-dessus des images de conteneurs. Il permet de référencer des images par des tags symboliques (par ex., `latest`, `v1.0`) plutôt que par des digests SHA256.

**Avantages des ImageStreams :**

- **Découplage** : Les déploiements peuvent référencer un ImageStream au lieu d'une image spécifique, ce qui facilite les mises à jour.
- **Déclencheurs automatiques** : Lorsqu'une nouvelle image est poussée vers un ImageStream, cela peut déclencher automatiquement un nouveau déploiement.
- **Importation d'images externes** : Les ImageStreams peuvent pointer vers des images dans des registres externes (par ex., Docker Hub, Quay.io).

### Stratégies de Build

OpenShift peut créer des images de conteneurs à partir de code source en utilisant différentes stratégies de build :

| Stratégie | Description |
|---|---|
| **Source-to-Image (S2I)** | Combine le code source avec une image de base (builder image) pour produire une nouvelle image exécutable. Pas besoin de Dockerfile. |
| **Docker** | Utilise un Dockerfile présent dans le dépôt de code source pour construire l'image. |
| **Pipeline** | Utilise un pipeline Tekton ou Jenkins pour orchestrer le processus de build. |

### Diagramme : Flux de Build et Push d'Image

```mermaid
flowchart TD
    subgraph "1️⃣ Code Source"
        GIT["📁 Dépôt Git<br/>github.com/user/myapp"]
    end

    subgraph "2️⃣ Build Process"
        BC["BuildConfig<br/>myapp-build"]
        GIT -->|"Webhook / Manual Trigger"| BC
        
        BC -->|"S2I Strategy"| S2I["Builder Pod<br/>python:3.9 + code source"]
        BC -->|"Docker Strategy"| DOCKER["Builder Pod<br/>Exécute docker build"]
        
        S2I --> IMAGE1["Image de conteneur<br/>myapp:latest"]
        DOCKER --> IMAGE1
    end

    subgraph "3️⃣ Registre Interne"
        REGISTRY["Internal Registry<br/>image-registry.openshift-image-registry.svc"]
        IMAGE1 -->|"Push"| REGISTRY
    end

    subgraph "4️⃣ ImageStream"
        IS["ImageStream: myapp<br/>Tag: latest"]
        REGISTRY --> IS
    end

    subgraph "5️⃣ Déploiement"
        DEPLOY["Deployment: myapp"]
        IS -->|"Trigger"| DEPLOY
        DEPLOY --> POD["Pod: myapp-xyz"]
    end

    style BC fill:#FFD700
    style REGISTRY fill:#87CEEB
    style IS fill:#90EE90
```

### Diagramme : Stratégies de Build Comparées

```mermaid
graph LR
    subgraph "Source-to-Image (S2I)"
        SRC1["📝 Code Source<br/>(Python, Node.js, etc.)"] --> BUILDER1["🏗️ Builder Image<br/>(python:3.9-ubi8)"]
        BUILDER1 --> OUT1["📦 Image Finale<br/>(Prête à exécuter)"]
        NOTE1["✅ Pas de Dockerfile<br/>✅ Sécurisé (image de base contrôlée)<br/>✅ Standardisé"]
    end

    subgraph "Docker Build"
        SRC2["📝 Code Source<br/>+ Dockerfile"] --> DOCKER2["🐳 Docker Build"]
        DOCKER2 --> OUT2["📦 Image Finale"]
        NOTE2["✅ Flexibilité maximale<br/>⚠️ Nécessite Dockerfile<br/>⚠️ Sécurité à gérer"]
    end

    subgraph "Pipeline (Tekton)"
        SRC3["📝 Code Source"] --> PIPELINE["⚙️ Pipeline Tekton<br/>(Tasks: test, build, scan)"]
        PIPELINE --> OUT3["📦 Image Finale<br/>(Testée + Scannée)"]
        NOTE3["✅ CI/CD complet<br/>✅ Tests automatisés<br/>⚠️ Plus complexe"]
    end

    style BUILDER1 fill:#90EE90
    style DOCKER2 fill:#FFD700
    style PIPELINE fill:#87CEEB
```

## Où chercher dans la documentation officielle

- **Registre d'images intégré** : [https://docs.openshift.com/container-platform/latest/registry/index.html](https://docs.openshift.com/container-platform/latest/registry/index.html)
- **ImageStreams** : [https://docs.openshift.com/container-platform/latest/openshift_images/image-streams-manage.html](https://docs.openshift.com/container-platform/latest/openshift_images/image-streams-manage.html)
- **Builds** : [https://docs.openshift.com/container-platform/latest/cicd/builds/understanding-builds.html](https://docs.openshift.com/container-platform/latest/cicd/builds/understanding-builds.html)

## Commandes clés

```bash
# Lister les ImageStreams
oc get imagestreams
oc get is

# Décrire un ImageStream
oc describe is myapp

# Importer une image externe dans un ImageStream
oc import-image myapp --from=docker.io/myuser/myapp:latest --confirm

# Créer un build à partir de code source (S2I)
oc new-build python:3.9~https://github.com/user/myapp.git

# Démarrer un build manuellement
oc start-build myapp

# Suivre les logs d'un build
oc logs -f bc/myapp

# Lister les builds
oc get builds
```

## À retenir / Pièges fréquents

- **Le registre nécessite du stockage** : Le registre d'images intégré ne fonctionnera pas sans un backend de stockage configuré. Sur les clouds publics, il utilise généralement le stockage objet (S3, Azure Blob).
- **ImageStreams vs Images** : Un ImageStream n'est pas une image, c'est un pointeur vers une ou plusieurs images. Pensez-y comme un tag Git qui peut pointer vers différents commits.
- **S2I est puissant** : La stratégie S2I est l'une des fonctionnalités les plus puissantes d'OpenShift. Elle permet aux développeurs de déployer du code sans avoir à écrire de Dockerfile.
- **Les builds consomment des ressources** : Les builds s'exécutent dans des pods et consomment des ressources (CPU, mémoire). Assurez-vous de dimensionner correctement vos projets et de définir des quotas si nécessaire.
