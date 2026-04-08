# Configuration Post-Installation

## Objectif

Cette section décrit les étapes de configuration essentielles à effectuer après l'installation d'un cluster OpenShift pour le sécuriser, le personnaliser et le préparer à accueillir des applications.

## Concepts

Une fois le cluster de base installé, plusieurs tâches de configuration sont recommandées :

- **Configuration du stockage** : Définir des `StorageClass` par défaut pour le provisionnement dynamique des volumes persistants.
- **Personnalisation de l'authentification** : Configurer un fournisseur d'identité (IdP) comme LDAP, OpenID Connect (OIDC) ou GitHub pour gérer les utilisateurs et les groupes.
- **Gestion des certificats** : Remplacer les certificats auto-signés par défaut par des certificats signés par une autorité de certification (CA) de confiance.
- **Configuration du monitoring** : Personnaliser les alertes, les tableaux de bord et la rétention des métriques pour la pile de monitoring intégrée.
- **Configuration du registre d'images** : Configurer le stockage pour le registre d'images interne et exposer une route pour y accéder de l'extérieur.

## Où chercher dans la documentation officielle

- **Vue d'ensemble de la configuration post-installation** : [https://docs.openshift.com/container-platform/latest/post_installation_configuration/index.html](https://docs.openshift.com/container-platform/latest/post_installation_configuration/index.html)
- **Configuration du stockage** : [https://docs.openshift.com/container-platform/latest/storage/understanding-persistent-storage.html](https://docs.openshift.com/container-platform/latest/storage/understanding-persistent-storage.html)
- **Configuration d'un fournisseur d'identité** : [https://docs.openshift.com/container-platform/latest/authentication/understanding-identity-providers.html](https://docs.openshift.com/container-platform/latest/authentication/understanding-identity-providers.html)

## Commandes clés

```bash
# Configurer un fournisseur d'identité HTPasswd (pour des tests rapides)
oc create secret generic htpass-secret --from-file=htpasswd=</path/to/users.htpasswd> -n openshift-config
oc apply -f htpasswd-cr.yaml

# Lister les StorageClasses disponibles
oc get sc

# Annoter une StorageClass comme étant celle par défaut
oc patch storageclass <storage-class-name> -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

# Voir la configuration de l'authentification
oc get oauth cluster -o yaml
```

## À retenir / Pièges fréquents

- **Ne pas utiliser HTPasswd en production** : Le fournisseur d'identité HTPasswd est pratique pour le développement et les tests, mais il n'est pas recommandé pour les environnements de production. Utilisez un IdP d'entreprise comme LDAP ou OIDC.
- **Configurer une `StorageClass` par défaut** : Sans une `StorageClass` par défaut, le provisionnement dynamique des `PersistentVolumeClaim` (PVC) ne fonctionnera pas, ce qui empêchera de nombreuses applications de se déployer correctement.
- **Sauvegarder les configurations** : Toute modification apportée dans l'espace de noms `openshift-config` doit être traitée comme une configuration critique et sauvegardée.
- **Attention aux certificats** : La gestion des certificats peut être complexe. Assurez-vous de bien comprendre les implications avant de remplacer les certificats par défaut.
