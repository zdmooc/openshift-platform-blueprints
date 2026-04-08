# OpenShift Platform Blueprints

Dépôt principal de démonstration technique centré sur **Red Hat OpenShift**, l’ingénierie de plateforme et les pratiques **cloud-native** associées.

Ce dépôt a une double vocation :

- servir de **portfolio technique** orienté OpenShift ;
- structurer un ensemble de ressources réutilisables autour des **certifications**, des **blueprints de plateforme**, des **use cases** et des **livrables d’architecture**.

---

## Objectif

Ce dépôt n’est pas un simple espace de notes.

Il est conçu pour montrer un niveau de travail cohérent autour de :

- l’administration et l’exploitation d’environnements OpenShift ;
- le déploiement d’applications cloud-native ;
- les pratiques GitOps, CI/CD et automatisation ;
- la sécurité, la gouvernance et l’observabilité ;
- la structuration de cas d’usage concrets sur OpenShift ;
- un positionnement **Architecte / Expert OpenShift**.

---

## Positionnement

Ce dépôt vise à démontrer une capacité à travailler sur les axes suivants :

- **OpenShift Administration**
- **OpenShift Application Development**
- **GitOps / Argo CD / CI-CD**
- **Platform Engineering**
- **SRE / Observabilité**
- **Sécurité / Gouvernance / Réseau**
- **Cas d’usage métier sur OpenShift**

Il sert à la fois de :

- support de progression ;
- base de capitalisation ;
- vitrine technique ;
- socle de démonstration en contexte CV / mission / entretien.

---

## Structure du dépôt

```text
.
├── certifications/
├── platform/
├── use-cases/
├── common/
└── portfolio/
```

Chaque répertoire a un rôle précis.

---

## 1. Certifications

Le dossier `certifications/` regroupe les parcours de certification OpenShift cœur et les supports associés.

Noyau actuel :

- `certifications/ex280/` — **OpenShift Administration**
- `certifications/ex288/` — **OpenShift Application Development**
- `certifications/ex370/` — **OpenShift Data Foundation**
- `certifications/ex380/` — **Automation / Integration / Operations**
- `certifications/ex480/` — **Multi-cluster / Governance**
- `certifications/ex482/` — **Event-driven / Kafka**

Selon la certification, on peut y trouver :

- un `README.md` de cadrage ;
- un `book-v1/` pour le support long ;
- un `track/` pratique ;
- des fichiers de préparation (`PREPARATION.md`) ;
- des notes (`NOTES.md`) ;
- des checklists (`CHECKLIST.md`) ;
- des archives ou versions historiques.

### Finalité de ce dossier

Le but n’est pas uniquement la révision d’examen.

Ce dossier sert aussi à :

- structurer un parcours de montée en compétence ;
- transformer les révisions en actifs réutilisables ;
- relier les certifications aux problématiques réelles de plateforme ;
- montrer une progression crédible vers un profil OpenShift confirmé.

---

## 2. Platform

Le dossier `platform/` porte les **blueprints de plateforme réutilisables**.

On y place les composants structurants d’une plateforme OpenShift moderne, par exemple :

- GitOps ;
- Argo CD ;
- CI/CD ;
- sécurité ;
- réseau ;
- observabilité ;
- bootstrap d’environnement ;
- standards de structuration ;
- patterns d’industrialisation.

### Finalité de ce dossier

Le rôle de `platform/` est de fournir des éléments :

- réutilisables ;
- structurés ;
- orientés exploitation réelle ;
- compatibles avec une logique d’architecture et de delivery.

En d’autres termes, `platform/` contient le **socle technique réemployable**.

---

## 3. Use Cases

Le dossier `use-cases/` relie les blueprints à des scénarios concrets.

Exemples de use cases visés :

- **IBM ODM on OpenShift**
- **Keycloak / SSO / OIDC**
- **Kafka / architectures event-driven**
- **SRE / observabilité / runbooks**
- **OpenShift sur Azure**
- **déploiements applicatifs industrialisés**

### Finalité de ce dossier

Chaque use case a vocation à documenter :

- le contexte ;
- l’objectif ;
- l’architecture cible ;
- les composants mobilisés ;
- les contraintes ;
- les conventions de déploiement ;
- les points de vigilance ;
- les liens vers les blueprints de `platform/`.

Le but est de faire le pont entre **architecture**, **plateforme** et **mise en œuvre**.

---

## 4. Common

Le dossier `common/` regroupe les éléments partagés entre plusieurs certifications, plusieurs use cases ou plusieurs blueprints.

On peut y trouver par exemple :

- des scripts ;
- des templates ;
- des manifests partagés ;
- des applications de référence ;
- des conventions ;
- des ressources communes.

### Finalité de ce dossier

Éviter la duplication et centraliser les éléments transverses utiles à plusieurs parties du dépôt.

---

## 5. Portfolio

Le dossier `portfolio/` est destiné aux éléments de démonstration orientés :

- architecture ;
- cadrage ;
- synthèse ;
- preuve de travail ;
- valorisation CV / mission / entretien.

On peut y placer :

- des livrables techniques ;
- des DAT ou dossiers de cadrage ;
- des synthèses ;
- des notes de positionnement ;
- des éléments de storytelling technique ;
- des démonstrateurs de posture architecte.

### Finalité de ce dossier

Montrer non seulement la capacité à produire du contenu technique, mais aussi à le **structurer**, le **présenter** et le **valoriser**.

---

## Principes d’organisation

Ce dépôt suit quelques principes simples :

### 1. Lisibilité
Chaque dossier doit avoir un rôle clair.

### 2. Réutilisabilité
Les contenus doivent pouvoir être repris dans un autre contexte : lab, mission, support de préparation, démonstration.

### 3. Séparation des préoccupations
- `certifications/` pour les parcours certifiants ;
- `platform/` pour les blueprints techniques ;
- `use-cases/` pour les scénarios concrets ;
- `common/` pour le partagé ;
- `portfolio/` pour la démonstration globale.

### 4. Progression
Le dépôt doit pouvoir accompagner une montée en compétence du niveau administration / développement vers un niveau plateforme / architecture.

### 5. Cohérence portfolio
Le dépôt doit rester lisible pour un recruteur, un client ou un pair technique qui le découvre sans contexte préalable.

---

## Navigation conseillée

Ordre de lecture recommandé :

1. commencer par `certifications/` ;
2. poursuivre avec `platform/` ;
3. explorer ensuite `use-cases/` ;
4. utiliser `common/` comme socle partagé ;
5. terminer par `portfolio/` pour la vue globale et démonstrative.

---

## Public visé

Ce dépôt peut intéresser :

- les ingénieurs OpenShift ;
- les consultants plateforme ;
- les architectes cloud / DevOps ;
- les profils SRE / GitOps / sécurité ;
- les personnes préparant des certifications OpenShift ;
- les recruteurs ou clients souhaitant évaluer un niveau de structuration technique.

---

## Auteur

**Zidane Djamal**  
Architecte Cloud & DevOps | Expert OpenShift & Kubernetes

Ce dépôt rassemble des ressources orientées terrain, architecture et industrialisation, construites pour servir à la fois de support de progression et de portfolio technique.
