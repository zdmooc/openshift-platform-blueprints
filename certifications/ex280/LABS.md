Labs — EX280
Objectif de ce fichier

Ce document liste le parcours pratique officiel du dossier EX280.

Il ne doit pas rester générique. Il doit servir de plan de travail quotidien.

Principes
un lab = un objectif clair ;
un lab doit être rejouable sur CRC ;
un lab doit produire une trace ;
un lab doit pouvoir être nettoyé ;
un lab ne doit pas dériver inutilement vers un sujet hors EX280 strict.
Structure cible d’un lab

Chaque lab devrait idéalement contenir :

objectif ;
prérequis ;
étapes ;
vérifications ;
nettoyage ;
pièges fréquents ;
commandes à retenir.
Parcours officiel
Lab00 — Environnement CRC
Objectif

Valider l’environnement de travail avant toute autre chose.

Contenu
login ;
vérification du contexte ;
santé minimale du cluster ;
vérification des nodes ;
vérification des cluster operators ;
création d’un projet de test.
Vérifications
oc whoami
oc project
oc get nodes
oc get co
Lab01 — Projets, contextes et vues de base
Objectif

Comprendre le cadre de travail avant de déployer.

Contenu
projets ;
changement de projet ;
listing des ressources de base ;
vues utiles ;
lecture de namespace / project.
Compétences
ne pas se tromper de projet ;
lire rapidement l’état du namespace ;
retrouver les ressources principales.
Lab02 — Déploiement, Service, Route, ConfigMap, Secret
Objectif

Déployer une application simple et l’exposer.

Contenu
deployment ;
service ;
route ;
ConfigMap ;
Secret ;
injection de variables d’environnement ;
test d’accès.
Vérifications
pod Running ;
service présent ;
route présente ;
configuration visible dans le conteneur.
Lab03 — PVC, probes, requests/limits
Objectif

Ajouter de la fiabilité et de la persistance à une application simple.

Contenu
PVC ;
montage d’un volume ;
test de persistance ;
readiness probe ;
liveness probe ;
requests ;
limits.
Vérifications
PVC Bound ;
fichier persistant après redémarrage ;
probes visibles ;
resources visibles dans le pod.
Lab04 — Users, Groups, RBAC, HTPasswd
Objectif

Comprendre et pratiquer la gestion des accès.

Contenu
users ;
groups ;
rôles de projet ;
oc auth can-i ;
HTPasswd côté cluster si l’environnement le permet.
Vérifications
rôle attribué ;
test can-i réussi ;
groupe visible ;
user autorisé ou refusé selon le besoin.
Lab05 — ServiceAccounts, SCC, Secrets
Objectif

Comprendre l’identité runtime et les contraintes de sécurité des pods.

Contenu
création de ServiceAccount ;
association à un deployment ;
lecture de la SCC effective ;
diagnostic d’un blocage simple ;
gestion simple de secrets techniques.
Vérifications
SA visible dans le pod ;
SCC identifiée ;
correction d’un cas simple de blocage.
Lab06 — Routes et TLS
Objectif

Exposer proprement une application et lire les paramètres TLS.

Contenu
route HTTP ;
route TLS edge ;
lecture de la spec TLS ;
diagnostic service / route / endpoints.
Vérifications
route créée ;
accès fonctionnel ;
compréhension du chemin Route → Service → Endpoints → Pod.
Lab07 — NetworkPolicies
Objectif

Isoler un namespace ou une application puis réautoriser seulement le nécessaire.

Contenu
deny-all ingress ;
autorisation ciblée ;
test depuis un pod de debug ;
lecture des policies.
Vérifications
communication bloquée quand attendu ;
communication rétablie quand attendu.
Lab08 — Quotas, LimitRange, scaling simple
Objectif

Contrôler la consommation de ressources d’un projet.

Contenu
ResourceQuota ;
LimitRange ;
dépassement volontaire ;
scaling simple ;
lecture de Used et Hard.
Vérifications
quota visible ;
dépassement détecté ;
lecture correcte du diagnostic.
Lab09 — Logs, events, describe, troubleshooting
Objectif

Construire la routine de diagnostic.

Contenu
oc get events ;
oc describe ;
oc logs ;
lecture d’un pod bloqué ;
lecture d’un problème image / quota / route / SCC simple.
Vérifications
routine maîtrisée ;
diagnostic structuré ;
correction minimale appliquée.
Lab10 — Templates OpenShift
Objectif

Déployer un paquet paramétrable simple.

Contenu
template ;
parameters ;
oc process ;
oc apply -f -.
Vérifications
objets générés ;
paramètres injectés ;
déploiement fonctionnel.
Lab11 — Helm et Kustomize
Objectif

Pratiquer deux modes d’automatisation utiles à l’examen.

Contenu
installation Helm simple ;
upgrade ;
rollback ;
structure Kustomize ;
oc apply -k.
Vérifications
release Helm visible ;
rollback compris ;
overlay Kustomize appliqué.
Lab12 — Operators / OLM
Objectif

Installer, vérifier et supprimer proprement un operator.

Contenu
OperatorGroup ;
Subscription ;
CSV ;
lecture CRD ;
création d’une CR simple si possible.
Vérifications
operator installé ;
CSV lue ;
ressource custom comprise.
Lab13 — Jobs et CronJobs
Objectif

Pratiquer l’exécution batch dans OpenShift.

Contenu
Job ;
CronJob ;
exécution ;
historique ;
lecture des pods associés.
Vérifications
job exécuté ;
cronjob visible ;
logs consultables.
Lab14 — Mini-exam 90 minutes
Objectif

Enchaîner plusieurs briques sans support.

Contenu possible
projet ;
déploiement ;
service ;
route ;
ConfigMap / Secret ;
PVC ;
quota ;
RBAC ;
SA / SCC ;
troubleshooting ;
un objet d’automatisation.
Critère principal

Être capable de garder une méthode stable sous contrainte de temps.

Extensions possibles

Ces sujets peuvent exister, mais ne doivent pas polluer le parcours principal :

variantes de troubleshooting ;
variantes CRC vs cluster plus complet ;
ponts vers EX288 ;
scénarios d’industrialisation ;
réflexion architecture / gouvernance.
Trace attendue pour chaque lab

Pour chaque lab, noter :

commandes exécutées ;
captures utiles si nécessaire ;
erreurs rencontrées ;
correctifs ;
synthèse finale ;
niveau de fluidité.
Règle de passage

On ne passe pas au bloc suivant tant que le précédent n’est pas rejouable sans hésitation majeure.

Résultat attendu

À la fin du parcours, le candidat doit être capable de :

déployer ;
exposer ;
sécuriser ;
diagnostiquer ;
corriger ;
rejouer les gestes essentiels d’administration OpenShift sur CRC.