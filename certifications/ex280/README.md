EX280 — Red Hat Certified OpenShift Administrator
Objectif de ce dossier

Ce dossier sert de parcours de préparation pratique à la certification EX280 avec un environnement local basé sur CRC (CodeReady Containers / OpenShift Local).

Le but n’est pas de construire une documentation théorique lourde, mais un cockpit simple, exécutable et révisable :

un point d’entrée unique ;
un ordre clair de labs ;
une checklist de progression ;
des notes personnelles de terrain ;
une archive PDF légère du contenu long supprimé du dépôt actif.
Positionnement
Famille : certification officielle OpenShift
Parcours principal : administration OpenShift
Profil visé : administrateur OpenShift, SRE, ingénieur plateforme, architecte technique
Approche de ce dossier : CLI-first, CRC-first, pratique orientée examen
Pourquoi cette certification compte

EX280 est une certification socle pour administrer un cluster OpenShift de manière opérationnelle :

gestion des projets et des ressources ;
exposition réseau ;
stockage ;
RBAC et sécurité ;
troubleshooting ;
objets OpenShift spécifiques ;
automatisation utile sans dériver vers une plateforme complète.

Cette certification sert aussi de base pour la suite du parcours OpenShift.

Environnement cible pour cette préparation

Environnement principal retenu :

CRC / OpenShift Local
usage local sur poste de travail
pratique en CLI avec oc
console web utilisée en complément si utile, mais la priorité reste la maîtrise des commandes
Principes de travail
toujours vérifier le contexte et le projet courant ;
pratiquer d’abord sur un chemin simple et reproductible ;
documenter les erreurs réelles rencontrées ;
privilégier des labs courts, réexécutables et nettoyables ;
distinguer ce qui relève de l’EX280 strict et ce qui relève d’un pont vers EX288 / industrialisation.
Contenu de ce dossier

Ce dossier doit accueillir :

README.md : point d’entrée ;
PREPARATION.md : feuille de route ;
LABS.md : parcours des labs ;
CHECKLIST.md : checklist de progression ;
NOTES.md : journal personnel de préparation ;
docs/EX280-book-archive-v1.pdf : archive PDF du livre source supprimé du tronc principal ;
track/ : labs actifs, variantes et supports opérationnels.
Archive PDF

Le contenu long anciennement maintenu dans book-v1/ a été remplacé par une archive PDF :

docs/EX280-book-archive-v1.pdf

Ce PDF sert de support de révision. Le pilotage quotidien de la préparation doit désormais passer par :

LABS.md
PREPARATION.md
CHECKLIST.md
NOTES.md
Parcours recommandé

Ordre conseillé :

cadrage de l’examen ;
validation de l’environnement CRC ;
labs fondamentaux ;
labs sécurité / réseau ;
labs quotas / troubleshooting ;
labs d’automatisation utiles à EX280 ;
mini-exam chronométré ;
répétitions.
Parcours de labs actif

Le parcours actif visé est le suivant :

Lab00 — environnement CRC, login, santé cluster, projet de travail
Lab01 — projets, contextes, vues de base
Lab02 — déploiement, service, route, ConfigMap, Secret
Lab03 — PVC, probes, resources
Lab04 — users, groups, RBAC, HTPasswd
Lab05 — ServiceAccounts, SCC, Secrets
Lab06 — routes et TLS
Lab07 — NetworkPolicies
Lab08 — quotas, LimitRange, scaling simple
Lab09 — logs, events, troubleshooting
Lab10 — Templates OpenShift
Lab11 — Helm et Kustomize
Lab12 — Operators / OLM
Lab13 — Jobs et CronJobs
Lab14 — mini-exam 90 minutes
Règles de travail
1. CLI-first

Toutes les manipulations importantes doivent être faisables en ligne de commande.

2. Vérification systématique

Avant chaque lab :

oc whoami
oc project
oc get nodes
oc get co
3. Méthode de diagnostic unique

En cas de problème :

oc get events --sort-by=.lastTimestamp | tail -n 30
oc describe <ressource>
oc logs <pod> --all-containers --tail=200
4. Trace de progression

Pour chaque lab, noter :

date ;
commandes clés ;
erreurs rencontrées ;
correctifs ;
ce qu’il reste à revoir.
Ce que ce dossier n’a pas vocation à devenir

Ce dossier ne doit pas redevenir :

un livre source complexe à maintenir ;
un dépôt de théorie redondante ;
un fourre-tout mélangeant EX280, EX288, GitOps, observabilité avancée et architecture globale.

Les sujets hors périmètre strict peuvent être conservés comme ponts ou extensions, mais ne doivent pas brouiller le chemin principal.

Suite logique après EX280

Après validation d’un socle solide sur EX280, les suites possibles sont notamment :

EX288
EX380
EX430
EX432
EX370
EX316
Mode d’utilisation conseillé
Début de séance
ouvrir README.md
regarder PREPARATION.md
choisir un lab dans LABS.md
Pendant la séance
exécuter le lab
noter les incidents dans NOTES.md
Fin de séance
cocher CHECKLIST.md
noter le niveau de fluidité
décider si le lab doit être refait à froid
Résultat attendu

À la fin de cette préparation, ce dossier doit permettre :

de rejouer rapidement un parcours EX280 local ;
de réviser sans bruit documentaire ;
de disposer d’une trace crédible pour portfolio et entretiens ;
de faire le pont entre certification et cas d’usage réel d’administration OpenShift.