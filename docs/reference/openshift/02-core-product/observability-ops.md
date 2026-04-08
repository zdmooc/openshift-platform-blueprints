# Observabilité & Opérations

## Objectif

Cette section décrit la pile d'observabilité intégrée d'OpenShift, qui fournit des capacités de monitoring, de logging et d'alerting pour le cluster et les applications. Elle couvre également les opérations de jour 2, comme la gestion des nœuds et la sauvegarde/restauration.

## Concepts

### Pile de Monitoring

OpenShift inclut une pile de monitoring pré-configurée et auto-actualisable basée sur Prometheus.

- **Prometheus** : Collecte et stocke les métriques du cluster et des applications.
- **Grafana** : Fournit des tableaux de bord pour visualiser les métriques collectées par Prometheus.
- **Alertmanager** : Gère les alertes déclenchées par Prometheus et les envoie aux destinataires configurés (par ex., email, Slack).
- **Monitoring des applications utilisateur** : Il est possible d'activer le monitoring pour vos propres applications afin de collecter leurs métriques personnalisées.

### Pile de Logging

La pile de logging centralise les logs de tous les composants du cluster et des applications.

- **Fluentd** : Agent qui s'exécute sur chaque nœud pour collecter les logs des conteneurs et les logs système.
- **Elasticsearch (obsolète) / Loki** : Stocke et indexe les logs collectés. OpenShift tend à remplacer Elasticsearch par Loki, qui est plus léger.
- **Kibana** : Interface web pour rechercher, visualiser et analyser les logs stockés.

### Opérations de Jour 2

- **Gestion des nœuds** : OpenShift utilise le **Machine API Operator** pour gérer le cycle de vie des nœuds. Vous pouvez ajouter ou supprimer des nœuds en utilisant des objets `MachineSet`.
- **Sauvegarde et Restauration** : La sauvegarde la plus critique est celle d'**etcd**. Des outils comme l'**Operator for etcd Backup** peuvent automatiser ce processus. Pour les applications, des outils comme **Velero** ou l'**OpenShift API for Data Protection (OADP)** peuvent être utilisés pour sauvegarder les ressources et les volumes persistants.

## Où chercher dans la documentation officielle

- **Vue d'ensemble du monitoring** : [https://docs.openshift.com/container-platform/latest/monitoring/understanding-the-monitoring-stack.html](https://docs.openshift.com/container-platform/latest/monitoring/understanding-the-monitoring-stack.html)
- **Vue d'ensemble du logging** : [https://docs.openshift.com/container-platform/latest/logging/cluster-logging-deploying.html](https://docs.openshift.com/container-platform/latest/logging/cluster-logging-deploying.html)
- **Sauvegarde d'etcd** : [https://docs.openshift.com/container-platform/latest/backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.html](https://docs.openshift.com/container-platform/latest/backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.html)

## Commandes clés

```bash
# Accéder à la console Grafana (nécessite un port-forward)
oc port-forward -n openshift-monitoring service/grafana 3000

# Voir les règles d'alerte
oc get prometheusrules -n openshift-monitoring

# Voir les logs d'un pod
oc logs <pod-name>

# Suivre les logs d'un pod en temps réel
oc logs -f <pod-name>

# Lister les MachineSets
oc get machinesets -n openshift-machine-api

# Mettre à l'échelle un MachineSet pour ajouter des nœuds
oc scale machineset <machineset-name> --replicas=3 -n openshift-machine-api
```

## À retenir / Pièges fréquents

- **Le monitoring consomme des ressources** : La pile de monitoring peut être gourmande en CPU et en mémoire, en particulier sur les grands clusters. Ajustez ses ressources si nécessaire.
- **Le logging est optionnel** : Contrairement au monitoring, la pile de logging n'est pas installée par défaut. Elle doit être déployée via un opérateur depuis OperatorHub.
- **Sauvegardez etcd régulièrement** : C'est votre filet de sécurité en cas de défaillance catastrophique du control plane.
- **Comprendre le Machine API** : Le Machine API est un outil puissant pour gérer les nœuds, mais il ne fonctionne que sur les clusters provisionnés par l'installateur (IPI) sur des fournisseurs de cloud pris en charge.
