# Notes personnelles — EX380

## Contexte de preuve

Ce fichier est destiné aux résultats de rejeu. Ne pas confondre contenu du kit et exécution observée.

Pour chaque session :
- Date :
- OpenShift version :
- Environnement :
- Namespace(s) :
- Lab / scénario :
- Résultat :
- Incident rencontré :
- RCA / correctif :
- Evidence path :
- À revoir :

## Concepts à retenir

### Identity
IdP, OIDC, LDAP, GroupSync, RBAC, kubeconfig.

### Data protection
OADP, Velero, CSI/S3, Backup, Restore, Schedule, snapshot.

### Scheduling / partitioning
labels, nodeSelector, MCP, taints/tolerations, affinity/anti-affinity, PDB.

### GitOps
OpenShift GitOps / Argo CD, desired state, namespaces infra/apps, App-of-Apps.

### Observabilité
Prometheus, Alertmanager, métriques, alertes, silences, Loki/Vector/Event Router.

## Limites à toujours signaler

- CRC mono-nœud ne valide pas un comportement HA multi-node ;
- certains scénarios MCP/infra nodes nécessitent un cluster plus complet ;
- OADP utile seulement avec backend/snapshot support réellement disponible ;
- aucun examen officiel n'est réputé réussi par la présence de ce track.
