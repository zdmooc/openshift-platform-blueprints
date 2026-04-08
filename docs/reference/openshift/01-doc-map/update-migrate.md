# Mise à jour & Migration

## Objectif

Cette section explique comment mettre à jour un cluster OpenShift vers une nouvelle version et comment migrer des applications et des données entre clusters. Elle couvre les concepts de canaux de mise à jour, de graphes de mise à jour et les stratégies de migration.

## Concepts

### Mise à jour du cluster

La mise à jour d'un cluster OpenShift est un processus géré par le **Cluster Version Operator (CVO)**. Le CVO surveille les opérateurs du cluster et s'assure qu'ils sont à la bonne version.

- **Canaux de mise à jour (Update Channels)** : Ils vous permettent de choisir la cadence à laquelle vous recevez les mises à jour. Les canaux courants sont `stable`, `fast` et `candidate`.
- **Graphe de mise à jour (Update Graph)** : Il définit les chemins de mise à jour valides entre les versions d'OpenShift. Vous ne pouvez pas sauter des versions mineures lors de la mise à jour.

### Migration

La migration fait référence au déplacement d'applications, de données et de configurations d'un cluster OpenShift à un autre. Cela peut être nécessaire pour des raisons de mise à niveau matérielle, de changement de fournisseur de cloud ou de reprise après sinistre.

- **Migration Toolkit for Containers (MTC)** : Un outil qui aide à migrer les applications stateful et stateless entre les clusters OpenShift.

### Diagramme : Processus de Mise à Jour du Cluster

```mermaid
flowchart TD
    START["🚀 Démarrer la mise à jour"] --> CHECK_CHANNEL{"Canal de mise à jour<br/>configuré?"}
    
    CHECK_CHANNEL -->|"Non"| SET_CHANNEL["1️⃣ Définir le canal<br/>stable / fast / candidate"]
    CHECK_CHANNEL -->|"Oui"| CHECK_UPDATES
    
    SET_CHANNEL --> CHECK_UPDATES["2️⃣ Vérifier les mises à jour disponibles<br/>oc adm upgrade"]
    
    CHECK_UPDATES --> GRAPH{"Graphe de mise à jour<br/>valide?"}
    GRAPH -->|"Chemin direct"| DIRECT["Mise à jour directe possible<br/>4.12.0 → 4.12.5"]
    GRAPH -->|"Chemin indirect"| INDIRECT["Mise à jour en plusieurs étapes<br/>4.11.x → 4.12.0 → 4.13.0"]
    
    DIRECT --> BACKUP["3️⃣ Sauvegarder etcd<br/>(CRITIQUE!)"]
    INDIRECT --> BACKUP
    
    BACKUP --> LAUNCH["4️⃣ Lancer la mise à jour<br/>oc adm upgrade --to=X.Y.Z"]
    
    LAUNCH --> CVO["5️⃣ Cluster Version Operator<br/>orchestre la mise à jour"]
    
    CVO --> UPDATE_MASTERS["6️⃣ Mise à jour Control Plane<br/>(Masters un par un)"]
    UPDATE_MASTERS --> MASTERS_OK{"Masters OK?"}
    MASTERS_OK -->|"Erreur"| ROLLBACK[" ❌ Rollback automatique"]
    MASTERS_OK -->|"Succès"| UPDATE_WORKERS
    
    UPDATE_WORKERS["7️⃣ Mise à jour Workers<br/>(MachineConfigOperator)"]
    UPDATE_WORKERS --> DRAIN["Drain pods → Update OS → Reboot"]
    DRAIN --> WORKERS_OK{"Workers OK?"}
    WORKERS_OK -->|"Erreur"| PAUSE[" ⚠️ Pause pour investigation"]
    WORKERS_OK -->|"Succès"| UPDATE_OPERATORS
    
    UPDATE_OPERATORS["8️⃣ Mise à jour Operators<br/>(Ingress, Registry, Monitoring, etc.)"]
    UPDATE_OPERATORS --> VERIFY["9️⃣ Vérification finale<br/>oc get clusterversion<br/>oc get co"]
    
    VERIFY --> COMPLETE[" ✅ Mise à jour complète!"]
    
    style BACKUP fill:#FF6B6B
    style COMPLETE fill:#90EE90
    style ROLLBACK fill:#FFB6C1
```

### Diagramme : Migration avec MTC (Migration Toolkit for Containers)

```mermaid
sequenceDiagram
    participant Admin as 👨‍💻 Administrateur
    participant Source as 🔵 Cluster Source<br/>(OCP 3.11)
    participant MTC as 📦 MTC Operator
    participant S3 as 💾 Stockage Intermédiaire<br/>(S3, NFS)
    participant Target as 🟢 Cluster Cible<br/>(OCP 4.x)
    
    Admin->>Source: 1. Installer MTC Operator
    Admin->>Target: 2. Installer MTC Operator
    
    Admin->>MTC: 3. Créer MigCluster (Source + Target)
    Admin->>MTC: 4. Créer MigStorage (S3/NFS)
    
    Admin->>MTC: 5. Créer MigPlan<br/>(Sélectionner namespaces, PVs)
    MTC->>Source: 6. Analyser les ressources
    Source-->>MTC: Liste des ressources à migrer
    
    Admin->>MTC: 7. Exécuter MigMigration (Stage)
    MTC->>Source: 8. Copier PV data vers S3
    Source->>S3: Transfert des données
    MTC->>Target: 9. Créer ressources (sans trafic)
    
    Admin->>Admin: 10. Valider la migration en staging
    
    Admin->>MTC: 11. Exécuter MigMigration (Cutover)
    MTC->>Source: 12. Quiesce applications (arrêt)
    MTC->>Source: 13. Copie finale des deltas
    Source->>S3: Transfert incrémental
    MTC->>Target: 14. Restaurer PVs depuis S3
    S3->>Target: Restauration des données
    MTC->>Target: 15. Démarrer applications
    Target-->>Admin: ✅ Migration complète!
    
    Note over Admin,Target: Downtime: 5-30 minutes (selon la taille des données)
```

## Où chercher dans la documentation officielle

- **Mise à jour d'un cluster** : [https://docs.openshift.com/container-platform/latest/updating/understanding-openshift-updates.html](https://docs.openshift.com/container-platform/latest/updating/understanding-openshift-updates.html)
- **Migration de clusters** : [https://docs.openshift.com/container-platform/latest/migration/migrating_from_ocp3_to_4/about-migration.html](https://docs.openshift.com/container-platform/latest/migration/migrating_from_ocp3_to_4/about-migration.html)

## Commandes clés

```bash
# Voir les mises à jour disponibles
oc adm upgrade

# Lancer une mise à jour vers une version spécifique
oc adm upgrade --to=<version>

# Voir l'état de la mise à jour
oc get clusterversion

# Voir l'historique des mises à jour
oc adm upgrade history
```

## À retenir / Pièges fréquents

- **Lisez les notes de version** : Avant de lancer une mise à jour, lisez attentivement les notes de version pour connaître les changements, les dépréciations et les problèmes connus.
- **Sauvegardez votre cluster** : Avant toute mise à jour majeure, effectuez une sauvegarde complète de votre cluster, y compris etcd.
- **Testez la mise à jour** : Si possible, testez le processus de mise à jour sur un environnement de non-production avant de le faire en production.
- **Planifiez la migration** : La migration d'applications, en particulier les applications stateful, nécessite une planification minutieuse. Testez votre plan de migration avant de l'exécuter en production.
