PREPARATION.md
Feuille de route de préparation — EX280
Objectif

Mettre en place une préparation pratique, progressive et répétable de la certification EX280 sur CRC, avec une priorité donnée à :

la compréhension du périmètre ;
la répétition des gestes CLI ;
la résolution d’incidents réalistes ;
la montée en fluidité avant mini-exam.
Vue d’ensemble

La préparation est découpée en 4 phases :

cadrage ;
lab ;
révision ;
consolidation.
Phase 1 — cadrage
But

Comprendre exactement ce que l’on cherche à maîtriser avant d’enchaîner les labs.

À faire
comprendre le positionnement de l’examen ;
repérer les briques techniques réellement utiles ;
identifier les objets OpenShift à pratiquer en priorité ;
vérifier les prérequis manquants ;
clarifier les limites de CRC par rapport à un cluster plus complet.
Vérifications minimales
je sais à quoi sert EX280 ;
je sais distinguer EX280 de sujets plus larges type GitOps / CI/CD avancée ;
je sais quelles briques doivent être pratiquées en premier.
Sortie attendue
environnement cible choisi ;
parcours de labs clarifié ;
zones faibles identifiées.
Phase 2 — lab
But

Pratiquer les tâches de manière répétable sur CRC.

Règle principale

Tant que les fondamentaux ne sont pas fluides, on ne monte pas vers les labs avancés.

Bloc A — environnement et socle
Lab00 — environnement CRC
Lab01 — projets et contextes
Lab02 — déploiement / exposition / configuration
Lab03 — stockage / probes / ressources
Bloc B — sécurité et réseau
Lab04 — users / groups / RBAC / HTPasswd
Lab05 — ServiceAccounts / SCC / Secrets
Lab06 — routes / TLS
Lab07 — NetworkPolicies
Bloc C — contrôle et diagnostic
Lab08 — quotas / LimitRange / scaling
Lab09 — logs / events / troubleshooting
Bloc D — automatisation utile
Lab10 — Templates
Lab11 — Helm / Kustomize
Lab12 — Operators / OLM
Lab13 — Jobs / CronJobs
Bloc E — synthèse
Lab14 — mini-exam 90 min
Phase 2.1 — règle d’exécution d’un lab

Pour chaque lab :

lire l’objectif ;
exécuter sans aide si possible ;
vérifier le résultat ;
noter les erreurs ;
nettoyer ;
refaire à froid plus tard.
Informations à noter dans NOTES.md
commandes importantes ;
erreurs réelles ;
commandes de diagnostic utiles ;
points à revoir ;
niveau de fluidité.
Phase 2.2 — validation minimale avant passage au bloc suivant
Avant de passer au bloc B

Je dois être capable de refaire sans hésitation :

création de projet ;
déploiement d’une application simple ;
création de service ;
création de route ;
injection ConfigMap / Secret ;
PVC ;
probes ;
resources requests/limits.
Avant de passer au bloc C

Je dois être capable de refaire sans hésitation :

RBAC simple ;
SA ;
SCC ;
route TLS ;
deny-all NetworkPolicy ;
policy d’ouverture ciblée.
Avant de passer au bloc D

Je dois être capable de refaire sans hésitation :

lecture d’events ;
describe ;
logs ;
interprétation d’un quota ou d’un blocage simple.
Phase 3 — révision
But

Transformer les labs en réflexes d’examen.

À faire
faire une checklist par thème ;
chronométrer certains labs ;
refaire les labs sans regarder les notes ;
simplifier les commandes à retenir ;
distinguer les commandes “à connaître” des commandes “à relire”.
Rythme conseillé
1 lab simple non chronométré ;
1 lab de révision à froid ;
1 séance de troubleshooting ;
1 mini-bloc chronométré chaque semaine.
Exercices chronométrés recommandés
déploiement + service + route + config ;
quota + LimitRange ;
RBAC simple ;
SCC / SA ;
route TLS ;
troubleshooting complet ;
mini-exam.
Phase 4 — consolidation
But

Faire le lien entre la certification, le terrain et le portfolio.

À faire
relier les briques EX280 à des cas d’usage réels ;
extraire les commandes les plus utiles ;
transformer les erreurs rencontrées en fiches de révision ;
mettre à jour le dépôt de notes ;
relier la certif à un besoin métier ou mission.
Questions de consolidation
Comment j’utilise cela dans un cluster de mission ?
Quelles commandes sont vraiment devenues fluides ?
Où est-ce que je perds encore du temps ?
Quelles différences CRC / cluster réel dois-je garder en tête ?
Routine de début de séance
oc whoami
oc project
oc get nodes
oc get co
Si un problème apparaît
oc get events --sort-by=.lastTimestamp | tail -n 30
oc describe <ressource>
oc logs <pod> --all-containers --tail=200
Critères de progression
Niveau 1 — découverte
je comprends les objets ;
je réussis les labs avec support.
Niveau 2 — pratique
je réussis les labs avec peu d’aide ;
je sais où chercher quand ça casse.
Niveau 3 — examen
je refais les labs sans support ;
je vais vite ;
je garde une méthode stable.
Objectif final

Être capable de rejouer un parcours EX280 local cohérent sur CRC, avec :

compréhension des objets ;
exécution CLI fluide ;
méthode de troubleshooting stable ;
mini-exam refait plusieurs fois ;
notes de terrain exploitables.