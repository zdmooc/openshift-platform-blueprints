# Arbres de Décision pour le Licensing

## Objectif

Cette section fournit des arbres de décision simplifiés pour vous aider à choisir la bonne édition d'OpenShift et à estimer le nombre de souscriptions nécessaires.

## Arbre de Décision : Quelle édition choisir ?

```mermaid
graph TD
    A[Start] --> B{Avez-vous besoin de gérer plusieurs clusters OpenShift de manière centralisée ?};
    B -- Oui --> C[OpenShift Platform Plus (OCPP)];
    B -- Non --> D{Avez-vous besoin de fonctionnalités de plateforme avancées comme Service Mesh, Serverless ou Pipelines ?};
    D -- Oui --> E[OpenShift Container Platform (OCP)];
    D -- Non --> F{Avez-vous seulement besoin d'un Kubernetes robuste et supporté ?};
    F -- Oui --> G[OpenShift Kubernetes Engine (OKE)];
    F -- Non --> E;
```

## Arbre de Décision : Combien de souscriptions ?

```mermaid
graph TD
    A[Start] --> B{Listez tous les nœuds de votre cluster.};
    B --> C{Séparez les nœuds en 3 catégories : Control Plane, Infra, Worker.};
    C --> D{Ignorez les nœuds de Control Plane.};
    D --> E{Additionnez le nombre de cores/vCPU de tous les nœuds Worker.};
    E --> F{Additionnez le nombre de cores/vCPU de tous les nœuds Infra.};
    F --> G{Total vCPU = vCPU Workers + vCPU Infra};
    G --> H{Total Cores = Total vCPU / 2};
    H --> I{Nombre de souscriptions = Total Cores / 2 (car vendues par pack de 2)};
    I --> J[End];
```

## Où chercher dans la documentation officielle

Ces arbres de décision sont des simplifications basées sur le guide de souscription officiel.

- **Guide des souscriptions OpenShift** : [https://www.redhat.com/en/resources/openshift-subscription-guide-detail](https://www.redhat.com/en/resources/openshift-subscription-guide-detail)

## À retenir / Pièges fréquents

- **Ce sont des guides, pas des règles absolues** : Des cas particuliers peuvent exister. En cas de doute, consultez toujours un représentant Red Hat.
- **L'auto-évaluation est la clé** : La meilleure façon de choisir la bonne édition est d'évaluer honnêtement vos besoins actuels et futurs.
- **Ne sur-provisionnez pas** : Commencez petit et grandissez. Il est plus facile d'ajouter des souscriptions ou de passer à une édition supérieure que l'inverse.
