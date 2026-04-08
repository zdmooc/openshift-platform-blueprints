# Chapitres Fonctionnels

## Objectif

Cette section sert d\'index et de point d\'entrée vers les principaux domaines fonctionnels de la documentation OpenShift. Elle vous aide à localiser rapidement la documentation relative à un sujet spécifique comme le réseau, le stockage, la sécurité, etc.

## Concepts

La documentation OpenShift est organisée en plusieurs grands chapitres fonctionnels. Comprendre ces chapitres vous permet de naviguer plus efficacement.

| Chapitre | Description | Lien vers la documentation |
|---|---|---|
| **Networking** | Tout ce qui concerne le réseau dans OpenShift : CNI, SDN, Ingress, Egress, Routes, Network Policies, etc. | [Networking](https://docs.openshift.com/container-platform/latest/networking/index.html) |
| **Storage** | Gestion du stockage persistant : Persistent Volumes (PV), Persistent Volume Claims (PVC), Storage Classes, provisionnement dynamique, etc. | [Storage](https://docs.openshift.com/container-platform/latest/storage/index.html) |
| **Security** | Sécurisation du cluster et des applications : RBAC, Pod Security Standards, SCC, secrets, certificats, etc. | [Security and Compliance](https://docs.openshift.com/container-platform/latest/security/index.html) |
| **Authentication** | Gestion des utilisateurs et des groupes : fournisseurs d\'identité (IdP), OAuth, tokens, etc. | [Authentication](https://docs.openshift.com/container-platform/latest/authentication/index.html) |
| **Operators** | Gestion du cycle de vie des applications avec les Operators et l\'Operator Lifecycle Manager (OLM). | [Operators](https://docs.openshift.com/container-platform/latest/operators/index.html) |
| **Observability** | Monitoring, logging et alerting : Prometheus, Grafana, Alertmanager, Fluentd, etc. | [Observability](https://docs.openshift.com/container-platform/latest/observability/index.html) |
| **Machine Management** | Gestion des nœuds du cluster : MachineSets, MachineAutoscaler, etc. | [Machine Management](https://docs.openshift.com/container-platform/latest/machine_management/index.html) |

## Où chercher dans la documentation officielle

Le meilleur point de départ est la page d\'accueil de la documentation, qui liste tous les chapitres fonctionnels. Vous pouvez également utiliser la fonction de recherche pour trouver des sujets spécifiques.

- **Page d\'accueil de la documentation** : [https://docs.openshift.com/container-platform/latest/welcome/index.html](https://docs.openshift.com/container-platform/latest/welcome/index.html)

## Commandes clés

Il n\'y a pas de commandes spécifiques pour naviguer dans la documentation, mais connaître les objets Kubernetes/OpenShift associés à chaque chapitre peut vous aider à explorer votre cluster :

```bash
# Networking
oc get network.config.openshift.io cluster -o yaml
oc get netnamespace
oc get egressnetworkpolicy

# Storage
oc get storageclass
oc get pv
oc get pvc

# Security
oc get scc
oc get role,clusterrole
oc get rolebinding,clusterrolebinding

# Operators
oc get packagemanifest
oc get subscription
oc get installplan
oc get csv
```

## À retenir / Pièges fréquents

- **Ne vous perdez pas** : La documentation est vaste. Utilisez la structure des chapitres fonctionnels pour vous orienter.
- **Commencez par les concepts** : Avant de plonger dans les détails d\'une configuration, assurez-vous de bien comprendre les concepts de base du chapitre fonctionnel correspondant.
- **Utilisez les exemples** : La documentation officielle regorge d\'exemples de configuration YAML. Utilisez-les comme point de départ pour vos propres configurations.
