# Éditions d'OpenShift

## Objectif

Cette section compare les différentes éditions d'OpenShift pour vous aider à choisir celle qui convient le mieux à vos besoins. Le choix de l'édition a un impact significatif sur les fonctionnalités disponibles et le coût.

## Comparaison des Éditions

| Édition | Description | Cas d'usage idéal |
|---|---|---|
| **OpenShift Kubernetes Engine (OKE)** | Fournit les fonctionnalités de base de Kubernetes avec une gestion automatisée du système d'exploitation (CoreOS) et du cluster. C'est l'édition la plus légère. | Équipes qui ont principalement besoin d'un Kubernetes d'entreprise robuste sans les fonctionnalités de plateforme complètes (pas de Serverless, Service Mesh, Pipelines, etc.). |
| **OpenShift Container Platform (OCP)** | L'édition phare et la plus courante. Inclut toutes les fonctionnalités d'OKE, plus une suite complète d'outils pour les développeurs et les opérations : Serverless, Service Mesh, Pipelines (CI/CD), monitoring, logging, etc. | La plupart des cas d'usage en production. Offre une plateforme de conteneurs complète pour créer, déployer et gérer des applications. |
| **OpenShift Platform Plus (OCPP)** | L'édition la plus complète. Inclut tout ce qui se trouve dans OCP, plus trois produits supplémentaires :<br>1. **Advanced Cluster Management (ACM)** pour la gestion multi-cluster.<br>2. **Advanced Cluster Security (ACS)** pour la sécurité et la conformité à l'échelle du cluster.<br>3. **Quay** un registre de conteneurs privé et sécurisé. | Grandes entreprises avec de multiples clusters OpenShift à gérer, ou celles qui ont des exigences de sécurité et de conformité très strictes. |

## Offres Managées

En plus des éditions que vous pouvez installer vous-même, il existe des offres OpenShift gérées par les fournisseurs de cloud en partenariat avec Red Hat :

- **ROSA (Red Hat OpenShift Service on AWS)**
- **ARO (Azure Red Hat OpenShift)**
- **ROKS (Red Hat OpenShift on IBM Cloud)**

Dans ces offres, le fournisseur de cloud et Red Hat gèrent le control plane et l'infrastructure, ce qui vous permet de vous concentrer sur vos applications. Le coût des souscriptions OpenShift est généralement inclus dans le prix du service managé.

## Où chercher dans la documentation officielle

- **Comparaison des éditions** : [https://www.redhat.com/en/technologies/cloud-computing/openshift/platform-plus#compare](https://www.redhat.com/en/technologies/cloud-computing/openshift/platform-plus#compare)

## À retenir / Pièges fréquents

- **Commencer avec OCP** : Pour la plupart des nouveaux projets, OCP est le meilleur point de départ. Il offre le meilleur équilibre entre fonctionnalités et complexité.
- **OCPP pour le multi-cluster** : N'envisagez OCPP que si vous prévoyez de gérer plusieurs clusters OpenShift ou si vous avez besoin des fonctionnalités de sécurité avancées d'ACS dès le départ.
- **Les offres managées réduisent la charge opérationnelle** : Si votre équipe n'a pas l'expertise ou le temps de gérer un cluster OpenShift, les offres managées sont une excellente option, bien que potentiellement plus coûteuses.
