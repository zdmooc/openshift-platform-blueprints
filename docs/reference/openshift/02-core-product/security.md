# Sécurité

## Objectif

Cette section aborde les mécanismes de sécurité fondamentaux d'OpenShift qui permettent de sécuriser le cluster et les applications qui y sont exécutées. Elle couvre les Security Context Constraints (SCC), le Pod Security Standards, la gestion des secrets et la conformité.

## Concepts

OpenShift est conçu avec une approche de sécurité en couches ("defense in depth").

### Security Context Constraints (SCC)

Les **SCC** sont un objet spécifique à OpenShift qui contrôle les permissions des pods. Un SCC définit un ensemble de conditions qu'un pod doit respecter pour être accepté dans le cluster. Il contrôle des aspects tels que :

- L'exécution de conteneurs privilégiés.
- L'accès aux répertoires de l'hôte (`hostPath`).
- L'utilisateur sous lequel le conteneur s'exécute (doit-il être non-root ?).
- Les capacités Linux autorisées.

OpenShift fournit plusieurs SCC par défaut, du plus restrictif (`restricted-v2`) au plus permissif (`anyuid`).

### Pod Security Standards (PSS)

Les **Pod Security Standards** sont la nouvelle norme de Kubernetes pour définir différents niveaux d'isolation pour les pods. Ils sont intégrés dans OpenShift et remplacent progressivement les SCC comme principal mécanisme de contrôle de la sécurité des pods. Les trois niveaux sont :

- `privileged` : Non restreint.
- `baseline` : Minimalement restreint, tout en empêchant les escalades de privilèges connues.
- `restricted` : Fortement restreint, suit les meilleures pratiques de renforcement de la sécurité des pods.

### Gestion des Secrets

Un **Secret** est un objet Kubernetes destiné à contenir une petite quantité de données sensibles, telles qu'un mot de passe, un token ou une clé. Les secrets sont stockés encodés en Base64 dans etcd. Il est fortement recommandé d'activer le chiffrement au repos pour etcd afin de protéger ces données.

### Conformité (Compliance)

Le **Compliance Operator** est un outil qui permet d'évaluer la conformité du cluster par rapport à des profils de sécurité standard (par ex., CIS Benchmark, PCI-DSS). Il scanne le cluster et signale les configurations non conformes, et peut même les corriger automatiquement.

## Où chercher dans la documentation officielle

- **Security Context Constraints (SCC)** : [https://docs.openshift.com/container-platform/latest/authentication/managing-security-context-constraints.html](https://docs.openshift.com/container-platform/latest/authentication/managing-security-context-constraints.html)
- **Pod Security Admission** : [https://docs.openshift.com/container-platform/latest/security/pod_security_admission/about-pod-security-admission.html](https://docs.openshift.com/container-platform/latest/security/pod_security_admission/about-pod-security-admission.html)
- **Gestion des Secrets** : [https://docs.openshift.com/container-platform/latest/nodes/pods/nodes-pods-secrets.html](https://docs.openshift.com/container-platform/latest/nodes/pods/nodes-pods-secrets.html)
- **Compliance Operator** : [https://docs.openshift.com/container-platform/latest/security/compliance_operator/co-scans-and-remediations.html](https://docs.openshift.com/container-platform/latest/security/compliance_operator/co-scans-and-remediations.html)

## Commandes clés

```bash
# Lister les Security Context Constraints
oc get scc

# Décrire un SCC pour voir ses permissions
oc describe scc restricted-v2

# Créer un secret générique
oc create secret generic my-secret --from-literal=username=myuser --from-literal=password=mypassword

# Lister les secrets dans le projet courant
oc get secrets

# Voir le contenu d'un secret (décodé)
oc get secret my-secret -o jsonpath='{.data.password}' | base64 --decode
```

## À retenir / Pièges fréquents

- **`restricted-v2` est la norme** : Par défaut, la plupart des pods s'exécutent avec le SCC `restricted-v2`, qui est très sécurisé (par ex., il force les conteneurs à s'exécuter avec un UID non-root aléatoire). Cela peut poser des problèmes pour les images de conteneurs qui s'attendent à s'exécuter en tant que root.
- **Ne stockez pas de secrets dans les ConfigMaps** : Les `ConfigMaps` sont destinés à la configuration non sensible. Utilisez toujours des `Secrets` pour les données sensibles.
- **Chiffrement d'etcd** : Le chiffrement au repos d'etcd n'est pas activé par défaut. C'est une étape de configuration post-installation cruciale pour la sécurité.
- **Le Compliance Operator n'est pas une solution miracle** : Il aide à identifier et à corriger les problèmes de conformité, mais il ne remplace pas une compréhension approfondie des concepts de sécurité.
