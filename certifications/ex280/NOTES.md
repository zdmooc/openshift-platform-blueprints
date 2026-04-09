Notes personnelles — EX280
Objectif

Ce fichier est le journal de bord de la préparation EX280.

Il doit contenir du terrain, pas seulement de la théorie.

1. Contexte de travail
Environnement
Cluster :
Version OpenShift :
CRC :
OS poste :
CLI oc :
Namespace principal :
Date de début de préparation :
Rappels
Toujours vérifier le projet courant
Toujours noter les erreurs réelles
Toujours garder une trace des commandes qui m’ont réellement aidé
2. Concepts à retenir
OpenShift
Project = Namespace avec surcouche OpenShift
Route = exposition HTTP/HTTPS spécifique OpenShift
SCC = contrôle de sécurité spécifique OpenShift
Operator = installation / cycle de vie d’une capacité via OLM
Kubernetes / OpenShift communs
Deployment
Pod
Service
PVC
ConfigMap
Secret
Job
CronJob
NetworkPolicy
ResourceQuota
LimitRange
Différences importantes à garder en tête
ce qui est spécifique OpenShift ;
ce qui est standard Kubernetes ;
ce qui est faisable sur CRC mais avec limites ;
ce qui peut être différent sur un cluster plus complet.
3. Commandes / objets clés
Vérifications de base
oc whoami
oc project
oc get nodes
oc get co
Déploiement / exposition
oc create deployment <nom> --image=<image>
oc expose deployment <nom> --port=<port>
oc expose service <nom>
oc get svc,route,endpoints
Configuration
oc create configmap <nom> --from-literal=KEY=VALUE
oc create secret generic <nom> --from-literal=KEY=VALUE
oc set env deployment/<nom> --from=configmap/<nom>
oc set env deployment/<nom> --from=secret/<nom>
Stockage / probes / ressources
oc get pvc
oc describe pvc <nom>
oc set probe deployment/<nom> --readiness --open-tcp=<port>
oc set probe deployment/<nom> --liveness --open-tcp=<port>
oc set resources deployment/<nom> --requests=cpu=50m,memory=64Mi --limits=cpu=200m,memory=256Mi
RBAC / sécurité
oc auth can-i <verbe> <ressource> -n <ns>
oc adm policy add-role-to-user <role> <user> -n <ns>
oc adm policy add-role-to-group <role> <group> -n <ns>
oc get sa
oc set serviceaccount deployment/<nom> <sa>
oc get scc
Réseau
oc get route
oc describe route <nom>
oc get networkpolicy
oc describe networkpolicy <nom>
Troubleshooting
oc get events --sort-by=.lastTimestamp | tail -n 30
oc describe <ressource>
oc logs <pod> --all-containers --tail=200
oc logs <pod> --previous --all-containers --tail=200
Automatisation utile
oc process -f <template>.yaml -p KEY=VALUE | oc apply -f -
helm install <release> <chart>
helm upgrade <release> <chart>
helm rollback <release> <revision>
oc apply -k <dossier>
oc get subscription,csv -n <ns>
4. Erreurs fréquentes
Erreurs déjà rencontrées






Forme à utiliser
Problème
Symptôme
Commande utilisée pour diagnostiquer
Cause racine
Correctif
À retenir
5. Journal par lab
Lab00
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab01
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab02
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab03
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab04
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab05
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab06
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab07
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab08
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab09
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab10
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab11
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab12
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab13
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
Lab14
Date
Résultat
Commandes utiles
Erreurs
Correctifs
Niveau de fluidité
6. Questions à approfondir
Quelles limites CRC influencent certains labs ?
Quels objets sont OpenShift spécifiques et doivent être parfaitement maîtrisés ?
Quelles commandes me font encore perdre du temps ?
Quels thèmes sont encore trop lents à refaire à froid ?
Où se situe la frontière utile entre EX280 strict et pont vers EX288 ?
7. Liens utiles
documentation officielle OpenShift :
documentation oc :
pages de révision personnelles :
labs prioritaires :
archive PDF locale : docs/EX280-book-archive-v1.pdf
8. Synthèse courte
Ce que je sais bien faire






Ce que je dois retravailler






Niveau actuel
découverte / pratique / examen
Prochaine séance