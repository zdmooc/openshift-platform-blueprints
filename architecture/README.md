# Architecture

Ce répertoire constitue le **socle d’architecture** du dépôt `openshift-platform-blueprints`.

Il rassemble les documents qui donnent la **vision d’ensemble**, les **référentiels d’architecture**, les **patterns structurants** et les éléments de **valorisation portfolio** autour d’OpenShift.

L’objectif de ce dossier n’est pas de détailler toutes les commandes ou tous les manifests, mais de poser un cadre clair sur :

- la logique globale du dépôt ;
- les grands choix d’architecture ;
- les patterns techniques réutilisables ;
- la trajectoire entre lab, industrialisation et architecture de plateforme ;
- la manière de présenter ces éléments dans un contexte portfolio, mission ou entretien.

---

## Rôle du dossier `architecture/`

Le dossier `architecture/` sert à formaliser la partie la plus structurante du dépôt.

Il permet de répondre aux questions suivantes :

- quelle vision globale de plateforme OpenShift est portée par ce dépôt ;
- quels sont les principaux blocs fonctionnels et techniques ;
- comment GitOps, sécurité, observabilité et multi-cluster s’articulent entre eux ;
- comment relier une pratique de lab à une posture d’architecte ;
- comment transformer des travaux techniques en actifs lisibles pour un recruteur, un client ou un pair technique.

Autrement dit, `architecture/` ne remplace ni `platform/`, ni `docs/`, ni `certifications/`.
Il leur donne une **colonne vertébrale**.

---

## Positionnement dans le dépôt

Le dépôt `openshift-platform-blueprints` est organisé autour de quatre grands blocs complémentaires :

- `architecture/` pour la vision, les architectures de référence et le positionnement ;
- `docs/` pour la synthèse documentaire et la structuration de la connaissance ;
- `platform/` pour les blueprints techniques et les artefacts réutilisables ;
- `certifications/` pour les parcours de progression et de préparation.

Dans cette logique :

- `architecture/` explique **pourquoi** et **comment structurer** ;
- `docs/` aide à **comprendre** ;
- `platform/` aide à **mettre en œuvre** ;
- `certifications/` aide à **apprendre et progresser**.

---

## Structure du dossier

```text
architecture/
├── README.md
├── overview/
├── reference-architectures/
└── portfolio/
```

### 1. `overview/`
Cette partie regroupe les vues globales du dépôt et de la plateforme cible.

On y trouve les documents qui permettent de comprendre rapidement :

- le contexte du lab ou de la plateforme ;
- la topologie générale ;
- les grands composants ;
- l’organisation des namespaces et des briques transverses ;
- les hypothèses de départ.

C’est le meilleur point d’entrée pour obtenir une lecture synthétique avant d’entrer dans les détails.

### 2. `reference-architectures/`
Cette partie contient les architectures de référence par thème.

Les grands sujets attendus dans cette zone sont notamment :

- GitOps ;
- sécurité ;
- observabilité / SRE ;
- multi-cluster ;
- patterns de plateforme ;
- autres briques structurantes à mesure que le dépôt se consolide.

Ces documents ont vocation à expliciter les **principes**, les **patterns**, les **frontières de responsabilité** et les **cibles d’industrialisation**.

### 3. `portfolio/`
Cette partie regroupe les éléments les plus orientés **valorisation**.

Elle sert à transformer la matière technique du dépôt en éléments lisibles pour :

- un CV ;
- un entretien ;
- une mission ;
- une présentation de posture architecte.

On y place des synthèses, formulations réutilisables, résumés de valeur et angles de lecture métier / client / recruteur.

---

## Ordre de lecture recommandé

Pour découvrir le dossier `architecture/`, l’ordre conseillé est le suivant.

### Étape 1 — Vue d’ensemble
Commencer par :

- `overview/platform-overview.md`

Objectif : comprendre la plateforme cible, la topologie générale et les grands blocs.

### Étape 2 — Architectures de référence
Poursuivre avec :

- `reference-architectures/gitops-platform.md`
- les autres documents de `reference-architectures/`

Objectif : comprendre les choix d’architecture par domaine.

### Étape 3 — Lecture portfolio
Terminer par :

- `portfolio/portfolio-architect.md`

Objectif : voir comment la matière technique peut être reformulée dans une logique de démonstration de valeur.

---

## Principes de rédaction du dossier

Les documents de `architecture/` doivent suivre quelques règles simples.

### 1. Être structurants
Ils doivent d’abord clarifier la vision, les frontières et les patterns.
Ils ne doivent pas devenir des notes désordonnées.

### 2. Être réutilisables
Chaque document doit pouvoir servir dans plusieurs contextes :

- lab personnel ;
- préparation d’entretien ;
- support d’architecture ;
- démonstration portfolio.

### 3. Rester lisibles
L’objectif n’est pas de produire des documents lourds ou inutilement théoriques.
Le bon niveau est : synthétique, clair, crédible, exploitable.

### 4. Préparer l’industrialisation
Même lorsqu’un document part d’un lab ou d’un dépôt personnel, il doit laisser apparaître une trajectoire réaliste vers des usages plus industriels.

### 5. Servir le dépôt global
Chaque document d’architecture doit contribuer à rendre le dépôt plus homogène, plus compréhensible et plus crédible.

---

## Ce que le dossier ne doit pas devenir

Pour conserver sa valeur, `architecture/` ne doit pas devenir :

- un doublon de `docs/` ;
- un fourre-tout de notes techniques ;
- un emplacement de manifests YAML ;
- un espace de brouillons sans hiérarchie ;
- un empilement de promesses non démontrées.

Les manifests exécutables doivent rester dans `platform/`.
Les guides détaillés et structurés de référence doivent rester dans `docs/`.
Les parcours d’apprentissage et de préparation doivent rester dans `certifications/`.

---

## Articulation avec les autres dossiers

### Avec `docs/`
`architecture/` pose la vision.
`docs/` développe la compréhension détaillée des sujets.

### Avec `platform/`
`architecture/` décrit les patterns et la cible.
`platform/` porte les artefacts techniques concrets.

### Avec `certifications/`
`architecture/` donne le cadre et la hauteur de vue.
`certifications/` permet d’approfondir et de pratiquer.

---

## Ambition de ce dossier

À terme, ce dossier doit permettre à un lecteur externe de comprendre rapidement que le dépôt ne se limite pas à des essais OpenShift, mais cherche à montrer :

- une capacité de structuration ;
- une lecture transverse de la plateforme ;
- une sensibilité à l’industrialisation ;
- une posture d’architecte orientée plateforme, sécurité, observabilité et GitOps.

Ce dossier est donc un élément central de la crédibilité globale de `openshift-platform-blueprints`.

---

## Fichiers prioritaires à stabiliser

Dans la phase actuelle de consolidation, les fichiers suivants doivent être considérés comme prioritaires :

- `overview/platform-overview.md`
- `reference-architectures/gitops-platform.md`
- les autres documents de `reference-architectures/`
- `portfolio/portfolio-architect.md`

Le présent `README.md` sert de point d’entrée et de contrat de lecture pour l’ensemble.

---

## Auteur

**Zidane Djamal**  
Architecte technique / plateforme / cloud-native  
OpenShift | Kubernetes | GitOps | Sécurité | Observabilité | Architecture

