# Authentification & SSO

## Objectif

Cette section explique comment OpenShift gère l'authentification des utilisateurs et comment configurer le Single Sign-On (SSO) en s'intégrant avec des fournisseurs d'identité (IdP) externes.

## Concepts

### Authentification dans OpenShift

Le serveur d'API OpenShift délègue l'authentification à un composant central : l'**opérateur d'authentification de cluster**. Ce dernier configure un serveur OAuth interne qui gère le flux d'authentification.

### Fournisseurs d'Identité (IdP)

OpenShift peut être configuré pour utiliser un ou plusieurs fournisseurs d'identité pour authentifier les utilisateurs. Cela permet aux utilisateurs de se connecter avec leurs identifiants d'entreprise existants.

Quelques IdP courants :

- **HTPasswd** : Un simple fichier plat contenant des noms d'utilisateur et des mots de passe hachés. Utile pour les tests, mais **non recommandé pour la production**.
- **LDAP / Active Directory** : Permet de s'authentifier auprès d'un annuaire d'entreprise.
- **OpenID Connect (OIDC)** : Un protocole d'authentification standard basé sur OAuth 2.0. Permet de s'intégrer avec des fournisseurs comme Keycloak, Okta, Azure AD, etc.
- **GitHub, GitLab, Google** : Permet aux utilisateurs de se connecter avec leurs comptes de ces plateformes.

### Flux d'authentification (avec un IdP externe)

1. L'utilisateur accède à la console web d'OpenShift ou utilise la CLI `oc login`.
2. OpenShift redirige l'utilisateur vers la page de connexion de l'IdP configuré.
3. L'utilisateur s'authentifie auprès de l'IdP.
4. L'IdP renvoie un code d'autorisation à OpenShift.
5. Le serveur OAuth d'OpenShift échange ce code contre un token d'accès auprès de l'IdP.
6. Le serveur OAuth d'OpenShift crée un token d'accès OpenShift et le renvoie à l'utilisateur.
7. L'utilisateur utilise ce token pour toutes les requêtes ultérieures à l'API OpenShift.

## Où chercher dans la documentation officielle

- **Comprendre l'authentification** : [https://docs.openshift.com/container-platform/latest/authentication/understanding-authentication.html](https://docs.openshift.com/container-platform/latest/authentication/understanding-authentication.html)
- **Configuration des fournisseurs d'identité** : [https://docs.openshift.com/container-platform/latest/authentication/identity_providers/configuring-identity-providers.html](https://docs.openshift.com/container-platform/latest/authentication/identity_providers/configuring-identity-providers.html)
- **Configuration de HTPasswd** : [https://docs.openshift.com/container-platform/latest/authentication/identity_providers/configuring-htpasswd-identity-provider.html](https://docs.openshift.com/container-platform/latest/authentication/identity_providers/configuring-htpasswd-identity-provider.html)

## Commandes clés

```bash
# Voir la configuration OAuth globale du cluster
oc get oauth cluster -o yaml

# Créer un secret contenant le fichier htpasswd
oc create secret generic htpass-secret --from-file=htpasswd=<path/to/users.htpasswd> -n openshift-config

# Appliquer une ressource personnalisée (CR) pour configurer l'IdP HTPasswd
# (Voir la documentation pour le contenu du fichier htpasswd-cr.yaml)
oc apply -f htpasswd-cr.yaml

# Lister les utilisateurs connus par OpenShift
oc get users

# Lister les identités connues par OpenShift
oc get identities
```

## À retenir / Pièges fréquents

- **User vs Identity** : OpenShift a deux objets distincts : `User` et `Identity`. Une `Identity` représente une identité unique provenant d'un IdP (par ex., `alice` de l'IdP `my_ldap`). Un `User` regroupe une ou plusieurs identités. Cela permet à un même utilisateur de se connecter via différents IdP.
- **La configuration de l'authentification est centralisée** : Toute la configuration des IdP se fait en modifiant la ressource `oauth/cluster`.
- **Le SSO n'est pas l'autorisation** : L'authentification (prouver qui vous êtes) est distincte de l'autorisation (ce que vous avez le droit de faire). Une fois authentifié, c'est le RBAC qui détermine vos permissions.
- **Redémarrage des pods** : Après avoir modifié la configuration OAuth, les pods de l'opérateur d'authentification et du serveur OAuth redémarrent automatiquement pour appliquer les changements.
