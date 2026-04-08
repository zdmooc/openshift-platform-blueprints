# FAQ & Pièges Courants

## Objectif

Cette section répond aux questions fréquemment posées sur le licensing d'OpenShift et met en évidence les pièges courants à éviter pour garantir une gestion des coûts efficace et conforme.

## Questions Fréquemment Posées (FAQ)

**Q : Les nœuds de control plane (maîtres) nécessitent-ils des souscriptions ?**

R : Non, les nœuds de control plane ne sont pas comptabilisés et ne nécessitent pas de souscriptions OpenShift.

**Q : Qu'en est-il des nœuds d'infrastructure ?**

R : Oui, les nœuds dédiés à l'infrastructure (routeurs, registre, monitoring) sont comptabilisés et nécessitent des souscriptions.

**Q : Comment le SMT (Hyper-Threading) est-il compté ?**

R : Le licensing est basé sur les cœurs physiques, pas sur les threads logiques. Un cœur avec 2 threads compte comme 1 seul cœur pour le licensing.

**Q : Puis-je utiliser mes souscriptions RHEL existantes pour les nœuds OpenShift ?**

R : Non, une souscription OpenShift inclut Red Hat CoreOS (RHCOS). Vous n'avez pas besoin de souscriptions RHEL séparées pour vos nœuds RHCOS. Si vous utilisez des nœuds worker RHEL, la souscription OpenShift les couvre également.

**Q : Que se passe-t-il si j'ajoute des nœuds à mon cluster ?**

R : Vous devez acheter des souscriptions supplémentaires pour couvrir les nouveaux cœurs/vCPU ajoutés à votre pool de nœuds worker ou infra.

## Pièges Courants à Éviter

- **Oublier les nœuds d'infrastructure** : C'est l'erreur la plus courante. Assurez-vous de toujours inclure les nœuds infra dans votre calcul.

- **Sous-estimer la croissance** : Ne dimensionnez pas votre achat de souscriptions uniquement pour vos besoins du jour 1. Anticipez la croissance future pour éviter des achats d'urgence.

- **Ignorer les offres managées** : Ne pas évaluer les offres comme ROSA ou ARO. Elles peuvent être plus rentables si vous n'avez pas les compétences ou les ressources pour gérer le cluster vous-même.

- **Ne pas utiliser les bons outils de FinOps** : Ne pas utiliser des outils comme le `MachineAutoscaler` ou des solutions de gestion des coûts du cloud peut entraîner un gaspillage important de ressources et de coûts de souscription.

- **Choisir la mauvaise édition** : Acheter OpenShift Platform Plus alors que vous n'avez qu'un seul cluster et pas de besoins de sécurité avancés est un gaspillage. Inversement, choisir OKE et se rendre compte plus tard que vous avez besoin de Service Mesh vous coûtera plus cher à long terme.

## Où chercher dans la documentation officielle

- **Guide des souscriptions OpenShift** : [https://www.redhat.com/en/resources/openshift-subscription-guide-detail](https://www.redhat.com/en/resources/openshift-subscription-guide-detail)

## À retenir

- **La conformité est votre responsabilité** : C'est à vous de vous assurer que vous avez suffisamment de souscriptions pour couvrir votre utilisation. Red Hat peut effectuer des audits.
- **Parlez à un expert** : En cas de doute, la meilleure approche est de parler à un représentant commercial ou à un architecte de solutions Red Hat. Ils peuvent vous aider à naviguer dans les complexités du licensing.
