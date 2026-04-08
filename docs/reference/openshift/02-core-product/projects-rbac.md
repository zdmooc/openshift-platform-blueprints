# Projets & RBAC

## Objectif

Cette section explique comment OpenShift gère le multi-tenancy à l\'aide des Projets et comment le contrôle d\'accès basé sur les rôles (RBAC) est utilisé pour sécuriser l\'accès aux ressources du cluster.

## Concepts

### Projets (Projects)

Un **Projet** est un espace de noms Kubernetes (`Namespace`) avec des annotations supplémentaires. C\'est l\'unité de base de l\'isolation des ressources dans OpenShift. Chaque projet a son propre ensemble de politiques, de contraintes et de comptes de service.

- **Isolation** : Les ressources d\'un projet sont isolées des autres projets.
- **Quotas** : Des quotas de ressources (CPU, mémoire, stockage) peuvent être appliqués à chaque projet.
- **Réseau** : Par défaut, les pods d\'un projet ne peuvent pas communiquer avec les pods d\'autres projets (via `NetworkPolicy`).

### Contrôle d\'accès basé sur les rôles (RBAC)

RBAC est le mécanisme standard de Kubernetes pour contrôler l\'accès à l\'API. OpenShift étend ce modèle avec des rôles et des bindings supplémentaires.

| Objet RBAC | Description |
|---|---|
| **Role** | Un ensemble de permissions (verbes : `get`, `list`, `create`, etc.) sur des ressources (`pods`, `services`, etc.) au sein d\'un projet (namespaced). |
| **ClusterRole** | Un ensemble de permissions sur des ressources à l\'échelle du cluster (non-namespaced, comme `nodes`) ou sur des ressources dans tous les projets. |
| **RoleBinding** | Lie un `Role` à un ou plusieurs sujets (utilisateurs, groupes, comptes de service) au sein d\'un projet. |
| **ClusterRoleBinding** | Lie un `ClusterRole` à un ou plusieurs sujets à l\'échelle du cluster. |

OpenShift fournit plusieurs `ClusterRole` par défaut :

- `cluster-admin` : Super-utilisateur, accès complet à tout le cluster.
- `admin` : Administrateur d\'un projet.
- `edit` : Peut modifier la plupart des objets dans un projet, mais ne peut pas gérer les rôles et les bindings.
- `view` : Accès en lecture seule à un projet.

### Diagramme RBAC : Flux d'Autorisation

```mermaid
flowchart TD
    USER["👤 User: alice"] --> REQUEST["Requête API:<br/>GET /api/v1/namespaces/dev/pods"]
    REQUEST --> AUTH{"Authentification<br/>(OAuth Server)"}
    AUTH -->|"Token Valide"| AUTHZ{"Autorisation<br/>(RBAC)"}
    AUTH -->|"Token Invalide"| DENY1[" ❌ 401 Unauthorized"]
    
    AUTHZ --> CHECK1{"Vérifier<br/>RoleBindings<br/>dans 'dev'"}
    CHECK1 -->|"Trouvé"| ROLE1["RoleBinding: alice-edit<br/>→ Role: edit"]
    CHECK1 -->|"Pas trouvé"| CHECK2{"Vérifier<br/>ClusterRoleBindings"}
    
    ROLE1 --> PERM1{"Role 'edit'<br/>permet-il<br/>GET pods?"}
    PERM1 -->|"Oui"| ALLOW[" ✅ 200 OK<br/>Requête autorisée"]
    PERM1 -->|"Non"| DENY2[" ❌ 403 Forbidden"]
    
    CHECK2 -->|"Trouvé"| ROLE2["ClusterRoleBinding:<br/>alice-cluster-reader<br/>→ ClusterRole: cluster-reader"]
    CHECK2 -->|"Pas trouvé"| DENY2
    
    ROLE2 --> PERM2{"ClusterRole<br/>permet-il<br/>GET pods?"}
    PERM2 -->|"Oui"| ALLOW
    PERM2 -->|"Non"| DENY2
    
    style ALLOW fill:#90EE90
    style DENY1 fill:#FFB6C1
    style DENY2 fill:#FFB6C1
```

### Diagramme : Hiérarchie des Rôles par Défaut

```mermaid
graph TD
    CA["cluster-admin<br/>🔑 Accès complet au cluster"]
    ADMIN["admin<br/>🛠️ Administrateur de projet"]
    EDIT["edit<br/>✏️ Éditeur de projet"]
    VIEW["view<br/>👁️ Lecture seule"]
    BASIC["basic-user<br/>👤 Utilisateur de base"]
    
    CA -->|"Inclut toutes les permissions"| ADMIN
    ADMIN -->|"Inclut les permissions"| EDIT
    EDIT -->|"Inclut les permissions"| VIEW
    
    CA -."Peut gérer".-> NODES["Nœuds"]
    CA -."Peut gérer".-> NS["Namespaces"]
    CA -."Peut gérer".-> CRD["CRDs"]
    
    ADMIN -."Peut gérer".-> RBAC["RBAC dans le projet"]
    ADMIN -."Peut gérer".-> QUOTA["Quotas"]
    ADMIN -."Peut gérer".-> LIMITS["LimitRanges"]
    
    EDIT -."Peut créer/modifier".-> PODS["Pods"]
    EDIT -."Peut créer/modifier".-> SVC["Services"]
    EDIT -."Peut créer/modifier".-> ROUTES["Routes"]
    
    VIEW -."Peut lire".-> PODS
    VIEW -."Peut lire".-> SVC
    VIEW -."Peut lire".-> ROUTES
    
    BASIC -."Peut créer".-> PROJECTS["Ses propres projets"]
    
    style CA fill:#FF6B6B
    style ADMIN fill:#FFA500
    style EDIT fill:#FFD700
    style VIEW fill:#90EE90
    style BASIC fill:#87CEEB
```

## Où chercher dans la documentation officielle

- **Gestion des projets** : [https://docs.openshift.com/container-platform/latest/applications/projects/working-with-projects.html](https://docs.openshift.com/container-platform/latest/applications/projects/working-with-projects.html)
- **Utilisation de RBAC** : [https://docs.openshift.com/container-platform/latest/authentication/using-rbac.html](https://docs.openshift.com/container-platform/latest/authentication/using-rbac.html)

## Commandes clés

```bash
# Créer un nouveau projet
oc new-project my-project

# Lister les projets
oc get projects

# Changer de projet courant
oc project my-project

# Ajouter le rôle \'admin\' à l\'utilisateur \'alice\' sur le projet courant
oc adm policy add-role-to-user admin alice

# Ajouter le rôle \'view\' au groupe \'developers\' sur le projet \'test-project\'
oc adm policy add-role-to-group view developers -n test-project

# Vérifier si un utilisateur peut effectuer une action
oc adm policy can-i <verb> <resource> -n <project>
# Exemple : oc adm policy can-i create pods -n my-project

# Décrire un rôle pour voir ses permissions
oc describe clusterrole admin
```

## À retenir / Pièges fréquents

- **`oc new-project` vs `oc new-app`** : `oc new-project` crée un nouveau projet et y bascule. `oc new-app` crée des applications au sein du projet courant.
- **Privilège minimum** : Appliquez toujours le principe du moindre privilège. N\'accordez que les permissions strictement nécessaires. Évitez d\'utiliser `cluster-admin` pour les tâches quotidiennes.
- **`Role` vs `ClusterRole`** : Utilisez un `Role` pour les permissions limitées à un seul projet. Utilisez un `ClusterRole` pour les permissions qui s\'appliquent à l\'ensemble du cluster ou à plusieurs projets.
- **Comptes de service (ServiceAccounts)** : Les pods utilisent des `ServiceAccounts` pour interagir avec l\'API server. Sécurisez également les permissions de vos `ServiceAccounts`.
