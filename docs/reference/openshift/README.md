# OpenShift Documentation Map 🗺️

**Un guide complet, structuré et orienté action pour maîtriser Red Hat OpenShift Container Platform (OCP)**

## 🎯 Objectif

Ce dépôt offre une **carte de navigation** claire de la documentation officielle OpenShift, combinée avec des guides synthétiques et des diagrammes d'architecture. L'objectif est de répondre à trois besoins principaux :

1. **Comprendre la structure** de la documentation OpenShift officielle (versions 4.16, 4.18, 4.19)
2. **Maîtriser les compétences essentielles** pour les administrateurs et architectes (certifications EX280 / EX288)
3. **Optimiser les coûts** grâce à une compréhension claire du licensing et des modèles de souscription

## 📚 Structure du Dépôt

### 📍 Carte de la Documentation (`01-doc-map/`)

Exploration structurée de la documentation officielle OpenShift :

- **Vue d'ensemble** : Orientation générale et concepts clés
- **Architecture Discover** : Concepts fondamentaux (control plane, workers, infra nodes)
- **Installation** : Méthodes d'installation et prérequis
- **Mise à jour & Migration** : Stratégies de mise à jour et migration
- **Configuration Post-Installation** : Étapes essentielles après déploiement
- **Chapitres Fonctionnels** : Index des domaines clés
- **Mindmap Doc Map** : Représentation visuelle de la structure

### 🏗️ Produit Core (`02-core-product/`)

Guides détaillés sur les composants et fonctionnalités essentiels :

- **Architecture Core** : Composants, flux de données, interactions
- **Projets & RBAC** : Gestion des namespaces et contrôle d'accès
- **Workloads, Services & Routes** : Déploiement et exposition des services
- **Registry & Images** : Gestion des images conteneur
- **Stockage** : PersistentVolumes et StorageClasses
- **Networking** : CNI, SDN, network policies
- **Sécurité** : Pod Security Standards, RBAC avancé
- **Authentification & SSO** : OAuth, LDAP, SSO
- **Observabilité & Opérations** : Monitoring, logging, alerting
- **Operators & OLM** : Lifecycle management
- **Disconnected & Mirroring** : Déploiements en environnement fermé

### 💰 Licensing & FinOps (`03-licensing-finops/`)

Maîtrise complète des modèles de licensing et optimisation des coûts :

- **Glossaire** : Définitions (core-pair, socket-pair, AI accelerator)
- **Ce qui compte** : Règles de comptage des ressources
- **Éditions & Souscriptions** : Types de souscriptions
- **Arbres de Décision** : Sélection du modèle approprié
- **Scénarios Concrets** : Exemples chiffrés avec calculs
- **FAQ & Pièges** : Questions fréquentes et erreurs courantes

### 🎓 Piste Examen (`04-exam-track/`)

Préparation aux certifications Red Hat :

- **Checklist EX280** : Compétences et domaines
- **Ponts EX288** : Connexions entre EX280 et EX288
- **Exercices** : Drills et entraînements ciblés
- **Scénarios Style Examen** : Cas pratiques similaires aux examens

## 🚀 Utilisation

### Installation locale

```bash
# Cloner le dépôt
git clone https://github.com/zdmooc/openshift-doc-map.git
cd openshift-doc-map

# Installer les dépendances
pip install mkdocs mkdocs-material pymdown-extensions

# Lancer le serveur local
mkdocs serve
```

Accédez à `http://localhost:8000` pour consulter la documentation.

### Build statique

```bash
mkdocs build
```

La documentation statique sera générée dans le dossier `site/`.

## 📋 Principes de Contenu

Chaque page de documentation suit une structure cohérente :

- **Objectif** : Clarté sur ce que vous apprendrez
- **Concepts** : Explications théoriques essentielles
- **Où chercher** : Liens vers la documentation officielle
- **Commandes clés** : Exemples `oc`, `kubectl`, `helm`
- **Vérifications** : Comment valider votre compréhension
- **À retenir / Pièges** : Points critiques et erreurs courantes

## ⚠️ Respect du Copyright

Ce dépôt **ne copie pas** la documentation Red Hat verbatim. Nous :

- Paraphrasons et synthétisons les concepts
- Renvoyons systématiquement vers les pages officielles
- Citons très brièvement (max 1–2 phrases) uniquement si indispensable
- Créons des diagrammes et schémas originaux

**Sources officielles** :
- [docs.redhat.com](https://docs.redhat.com) - Documentation OCP par version
- [docs.openshift.com](https://docs.openshift.com) - Routes, ingress, contenus OCP
- Red Hat Self-managed OpenShift subscription guide

## 🤝 Contribution

Les contributions sont bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour les directives.

## 📄 Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.

## 📞 Support

Pour des questions, des corrections ou des suggestions, ouvrez une issue sur GitHub.

---

**Dernière mise à jour** : Décembre 2025
**Versions OpenShift couvertes** : 4.16, 4.18, 4.19
**Statut** : v1.0 - Production Ready
