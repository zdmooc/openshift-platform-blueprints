# GitOps Platform Reference Architecture

## 1. Objectif du document

Ce document décrit l’**architecture de référence GitOps** portée par le dépôt `openshift-platform-blueprints`.

Son objectif est de clarifier :

- le rôle de GitOps dans la plateforme ;
- le périmètre géré de manière déclarative ;
- la séparation entre configuration de plateforme et workloads ;
- les principes d’organisation autour d’Argo CD ;
- la trajectoire d’industrialisation progressive.

Ce document sert de cadre d’architecture.
Il ne remplace pas les manifests techniques, mais il explique **comment ils doivent être pensés et structurés**.

---

## 2. Pourquoi GitOps dans ce dépôt

Le dépôt `openshift-platform-blueprints` cherche à démontrer une approche OpenShift structurée, reproductible et crédible.

Dans cette logique, GitOps joue un rôle central car il permet de :

- faire de Git la source de vérité des configurations réutilisables ;
- tracer les changements ;
- limiter les écarts entre intention, configuration et état du cluster ;
- structurer proprement les responsabilités entre plateforme et applicatif ;
- préparer une démarche plus industrielle, même à partir d’un lab.

GitOps est donc ici à la fois :

- un **mode de gestion technique** ;
- un **principe d’architecture** ;
- un **vecteur de crédibilité portfolio**.

---

## 3. Positionnement de GitOps dans la plateforme

GitOps est utilisé pour porter progressivement les éléments de plateforme qui gagnent à être :

- déclaratifs ;
- versionnés ;
- relisibles ;
- rejouables ;
- validables.

L’architecture cible ne consiste pas à mettre “tout” dans GitOps sans discernement.
Elle consiste à définir un périmètre pertinent, progressif et défendable.

---

## 4. Principes GitOps retenus

### 4.1. Git comme source de vérité
Les éléments structurants de la plateforme doivent être définis dans Git et non maintenus principalement par modifications manuelles dans le cluster.

### 4.2. Déclaratif avant impératif
La cible privilégie les ressources déclaratives et les conventions stables plutôt que des suites d’actions manuelles difficiles à reproduire.

### 4.3. Séparation des responsabilités
La configuration plateforme doit être distinguée des workloads applicatifs ou des expérimentations ponctuelles.

### 4.4. Progressivité
Le dépôt n’a pas besoin d’être totalement GitOps dès le premier jour.
La logique retenue est d’étendre GitOps par paliers cohérents.

### 4.5. Lisibilité
Une architecture GitOps crédible doit rester compréhensible.
La structuration des dossiers et des Applications Argo CD doit être simple à expliquer.

---

## 5. Périmètre GitOps cible

### 5.1. Ce qui a vocation à être géré par GitOps
Le périmètre cible inclut principalement :

- certains namespaces ou projets standardisés ;
- quotas et limites ;
- rôles et bindings réutilisables ;
- policies réseau de base ;
- composants transverses de plateforme ;
- certaines briques observabilité ;
- certaines briques sécurité ;
- applications de démonstration suffisamment stabilisées.

### 5.2. Ce qui n’a pas vocation à être forcé trop tôt dans GitOps
Ne doivent pas nécessairement entrer trop tôt dans le périmètre GitOps :

- les expérimentations rapides ;
- les essais ponctuels de sandbox ;
- les éléments encore instables ou non normalisés ;
- certaines opérations dépendant fortement du contexte d’infrastructure.

L’idée n’est pas d’être dogmatique.
L’idée est d’être structuré.

---

## 6. Séparation plateforme / workloads

L’un des principes majeurs de cette architecture GitOps est la séparation entre :

- la **configuration de plateforme** ;
- les **workloads** ;
- les **expérimentations ou labs**.

### 6.1. Configuration de plateforme
Elle regroupe les éléments structurants et mutualisés :

- namespaces de base ;
- quotas ;
- RBAC ;
- NetworkPolicies ;
- composants transverses ;
- certaines politiques communes.

### 6.2. Workloads
Ils représentent les applications, composants métiers ou démonstrateurs hébergés sur la plateforme.

### 6.3. Sandbox / expérimentation
Ils servent à tester avant stabilisation.
Une fois un composant ou une configuration jugés suffisamment mûrs, ils peuvent être promus vers le périmètre GitOps normalisé.

---

## 7. Organisation cible dans le dépôt

L’architecture GitOps s’appuie sur une séparation claire dans le dépôt.

```text
platform/
└── gitops/
    ├── argocd-apps/
    └── cluster-config/
```

### 7.1. `platform/gitops/argocd-apps/`
Ce répertoire porte les objets Argo CD, par exemple :

- `Application`
- `AppProject`
- éventuellement `ApplicationSet` dans des étapes ultérieures

Cette zone représente le **plan de pilotage GitOps**.

### 7.2. `platform/gitops/cluster-config/`
Ce répertoire porte les manifests de configuration plateforme, par exemple :

- namespaces ;
- quotas ;
- RBAC ;
- policies réseau ;
- autres composants transverses.

Cette zone représente le **contenu géré par GitOps**.

---

## 8. Rôle d’Argo CD

Argo CD est le composant central de synchronisation GitOps retenu dans cette architecture.

Son rôle est de :

- lire l’état désiré depuis Git ;
- comparer cet état à l’état du cluster ;
- synchroniser les écarts ;
- donner de la visibilité sur les statuts ;
- fournir un cadre simple pour organiser les déploiements déclaratifs.

Dans le dépôt, Argo CD ne doit pas être présenté comme un simple outil de déploiement.
Il doit être compris comme un **composant de gouvernance technique de la plateforme**.

---

## 9. Modèle app-of-apps

L’architecture cible est compatible avec un modèle **app-of-apps**.

L’idée est d’avoir une application racine qui référence plusieurs sous-applications structurées, par exemple :

- plateforme namespaces ;
- plateforme quotas ;
- plateforme RBAC ;
- plateforme réseau ;
- plateforme observabilité ;
- plateforme sécurité.

Ce modèle présente plusieurs avantages :

- meilleure lisibilité ;
- meilleur découpage ;
- possibilité de faire évoluer chaque bloc indépendamment ;
- alignement avec une logique de plateforme modulaire.

Ce modèle ne doit cependant pas devenir une source de complexité excessive.
Il doit rester simple à comprendre.

---

## 10. Flux GitOps cible

Le flux cible peut être résumé ainsi :

```mermaid
flowchart LR
    Author[Auteur / Architecte / Contributeur] --> Git[Repository Git]
    Git --> Review[Revue / validation]
    Review --> Main[Branche principale]
    Main --> Argo[Argo CD]
    Argo --> Cluster[Cluster OpenShift]
```

### Étapes principales
1. un changement est préparé dans le dépôt ;
2. le contenu est relu, corrigé et versionné ;
3. le changement est intégré à la branche de référence ;
4. Argo CD détecte l’écart ;
5. le cluster converge vers l’état désiré.

Ce flux est volontairement simple.
Il suffit largement pour un dépôt de consolidation crédible.

---

## 11. Articulation avec la sécurité

GitOps et sécurité sont liés dans cette architecture.

GitOps permet notamment de mieux gérer :

- les rôles et bindings standardisés ;
- certaines policies réseau ;
- certaines conventions de déploiement ;
- les écarts de configuration ;
- la traçabilité des changements.

Cela ne remplace pas une stratégie sécurité complète, mais cela contribue fortement à la maîtrise de la configuration de plateforme.

---

## 12. Articulation avec l’observabilité

GitOps peut également piloter certains éléments liés à l’observabilité, par exemple :

- ServiceMonitors ;
- composants de monitoring supplémentaires ;
- dashboards ou ressources connexes ;
- configurations standardisées de supervision.

Cela renforce l’idée d’une plateforme où observabilité et exploitation ne sont pas traitées à part.

---

## 13. Limites et vigilance

Pour rester crédible, l’architecture GitOps du dépôt doit éviter plusieurs dérives.

### 13.1. YAML non fiables
Des manifests non valides ou non appliquables dégradent fortement la crédibilité du dépôt.

### 13.2. Complexité prématurée
Il vaut mieux une architecture GitOps simple et solide qu’une structure trop ambitieuse mais peu maîtrisée.

### 13.3. Mélange des responsabilités
Il faut éviter de mélanger sans discernement :

- plateforme ;
- applicatif ;
- documentation ;
- expérimentation.

### 13.4. Promesses trop fortes
Le dépôt doit rester honnête sur son niveau de maturité.
Une cible bien structurée vaut mieux qu’une prétention d’industrialisation totale non démontrée.

---

## 14. Trajectoire cible

La trajectoire GitOps souhaitée peut être résumée en plusieurs étapes.

### Étape 1 — Base lisible
- structure GitOps simple ;
- premiers manifests propres ;
- séparation plateforme / workloads.

### Étape 2 — Normalisation
- standardisation des conventions ;
- fiabilisation des YAML ;
- amélioration de la cohérence des Applications Argo CD.

### Étape 3 — Extension
- ajout progressif de blocs sécurité, observabilité et use cases ;
- meilleure articulation avec les autres dossiers du dépôt.

### Étape 4 — Projection avancée
- ouverture éventuelle vers ApplicationSet ;
- extension multi-cluster ;
- gouvernance plus avancée.

---

## 15. Lien avec le reste du dépôt

### Avec `overview/platform-overview.md`
Le document de vue d’ensemble positionne GitOps comme bloc structurant de la plateforme.

### Avec `platform/`
Le dossier `platform/` porte les artefacts concrets de cette architecture.

### Avec `docs/`
Le dossier `docs/` permet d’approfondir les concepts OpenShift nécessaires à la compréhension du modèle GitOps.

### Avec `certifications/`
Les parcours de certification permettent de pratiquer les briques qui alimentent ensuite l’architecture GitOps.

---

## 16. Conclusion

L’architecture GitOps décrite ici doit être comprise comme un **cadre de référence réaliste et progressif** pour `openshift-platform-blueprints`.

Elle vise à montrer qu’une plateforme OpenShift crédible repose non seulement sur des composants techniques, mais aussi sur :

- une bonne séparation des responsabilités ;
- une logique déclarative ;
- une structure de dépôt lisible ;
- un mode de gestion reproductible ;
- une trajectoire d’industrialisation claire.

C’est cette cohérence qui donne de la valeur au dépôt, aussi bien comme support d’apprentissage que comme vitrine technique.

---

## Auteur

**Zidane Djamal**  
Architecte technique / plateforme / cloud-native  
OpenShift | Kubernetes | GitOps | Sécurité | Observabilité | Architecture

