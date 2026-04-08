# Scénarios de Licensing

## Objectif

Cette section présente des scénarios concrets de licensing pour illustrer comment les règles s'appliquent dans la pratique. Ces exemples vous aideront à mieux comprendre comment estimer les coûts pour vos propres cas d'usage.

## Scénario 1 : Petit Cluster de Développement

- **Infrastructure** : vSphere
- **Configuration** :
  - 3 Nœuds Maîtres : 2 vCPU, 8 Go RAM chacun
  - 3 Nœuds Worker : 4 vCPU, 16 Go RAM chacun
- **Édition choisie** : OpenShift Container Platform (OCP)

**Calcul :**
- Nœuds Maîtres : Non comptabilisés.
- Nœuds Worker : 3 nœuds * 4 vCPU/nœud = 12 vCPU
- Total à souscrire : 12 vCPU
- Conversion en cores : 12 vCPU / 2 = 6 Cores
- **Souscriptions nécessaires** : 6 cores / 2 cores par souscription = **3 souscriptions OCP**

## Scénario 2 : Cluster de Production de Taille Moyenne sur AWS

- **Infrastructure** : AWS (IPI)
- **Configuration** :
  - 3 Nœuds Maîtres (m5.xlarge)
  - 10 Nœuds Worker (m5.2xlarge - 8 vCPU, 32 Go RAM chacun)
  - 3 Nœuds Infra (m5.xlarge - 4 vCPU, 16 Go RAM chacun)
- **Édition choisie** : OpenShift Platform Plus (OCPP) pour la sécurité avancée avec ACS.

**Calcul :**
- Nœuds Maîtres : Non comptabilisés.
- Nœuds Worker : 10 nœuds * 8 vCPU/nœud = 80 vCPU
- Nœuds Infra : 3 nœuds * 4 vCPU/nœud = 12 vCPU
- Total à souscrire : 80 + 12 = 92 vCPU
- Conversion en cores : 92 vCPU / 2 = 46 Cores
- **Souscriptions nécessaires** : 46 cores / 2 cores par souscription = **23 souscriptions OCPP**

## Scénario 3 : Cluster Bare Metal pour des charges de travail intensives

- **Infrastructure** : Serveurs physiques (Bare Metal)
- **Configuration** :
  - 3 Nœuds Maîtres : 1 serveur avec 2 sockets, 8 cores/socket
  - 5 Nœuds Worker : 1 serveur avec 2 sockets, 16 cores/socket chacun
- **Édition choisie** : OpenShift Container Platform (OCP)

**Calcul :**
- Nœuds Maîtres : Non comptabilisés.
- Nœuds Worker : 5 nœuds * (2 sockets/nœud * 16 cores/socket) = 5 * 32 = 160 Cores
- Total à souscrire : 160 Cores
- **Souscriptions nécessaires** : 160 cores / 2 cores par souscription = **80 souscriptions OCP**

## Où chercher dans la documentation officielle

- **Guide des souscriptions OpenShift** : [https://www.redhat.com/en/resources/openshift-subscription-guide-detail](https://www.redhat.com/en/resources/openshift-subscription-guide-detail)

## À retenir / Pièges fréquents

- **La granularité est par cluster** : Le licensing est calculé par cluster. Vous ne pouvez pas partager des souscriptions entre différents clusters.
- **Les offres managées ont un modèle différent** : Pour ROSA, ARO, etc., le coût est généralement basé sur la consommation horaire des nœuds, et la souscription OpenShift est incluse. Le calcul est différent.
- **Optimisation des coûts (FinOps)** : Envisagez d'utiliser des `MachineAutoscaler` pour ajuster dynamiquement la taille de votre cluster en fonction de la charge, ce qui peut aider à optimiser les coûts d'infrastructure et, dans certains modèles de facturation cloud, les coûts de souscription.
