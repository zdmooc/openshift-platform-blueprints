# Support de cours corrigé — Lab 01 EX280
**Projets, contexte, requêtes et images dans OpenShift (CRC / Git Bash)**

## Objectif
Ce lab permet de pratiquer, en conditions proches de l’examen EX280 :
- la création et la sélection d’un projet OpenShift ;
- la manipulation du contexte avec `oc` ;
- des requêtes utiles avec `jsonpath`, `custom-columns` et `--sort-by` ;
- la lecture d’images via `ImageStream`, tags et digests ;
- l’export d’objets YAML.

---

## 1. Contexte et prérequis

### Environnement visé
- Poste : Windows 11
- Terminal : Git Bash
- Cluster : CRC / OpenShift Local
- CLI : `oc`

### Point important sur CRC + Git Bash
Sur cet environnement, la variable `KUBECONFIG` peut être perdue entre deux manipulations.  
Avant les commandes importantes, il est prudent de la réexporter.

### Variables du lab
```bash
# Numéro du lab
export LAB=01

# Namespace / projet de travail
export NS=ex280-lab${LAB}-zidane
```

### Vérification minimale du contexte `oc`
```bash
# Reconnecte explicitement oc au kubeconfig CRC
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"

# Vérifie l'utilisateur courant
oc whoami

# Vérifie le projet courant
oc project
```

### Vérification du kubeconfig si `oc` échoue
```bash
# Affiche la variable d'environnement
 echo "$KUBECONFIG"

# Vérifie que le fichier existe bien
ls -l "$HOME/.kube/crc-kubeconfig"
```

### Ce qu’il faut retenir
- Si `oc` renvoie `Missing or incomplete configuration info`, vérifier d’abord `KUBECONFIG`.
- En examen, commencer par rétablir le contexte avant d’aller plus loin.

---

## 2. Rappel : projet, contexte et commande `oc`

OpenShift est construit sur Kubernetes. L’outil en ligne de commande principal est `oc`.

Le **contexte** indique :
- sur quel cluster on travaille ;
- avec quel utilisateur ;
- dans quel projet.

### Commande de base
```bash
# Bascule le contexte sur un projet donné
oc project <nom-du-projet>
```

Un **projet OpenShift** est un namespace enrichi, avec notamment :
- isolation logique des ressources ;
- sécurité et RBAC ;
- quotas et limites ;
- meilleure lisibilité dans la console.

---

## 3. Étape 1 — Créer et sélectionner le projet du lab

### Commandes
```bash
# Réexport du kubeconfig CRC
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"

# Crée le projet s'il n'existe pas déjà
oc get project "$NS" || oc new-project "$NS"

# Se place explicitement sur le projet du lab
oc project "$NS"

# Affiche le YAML du projet pour inspection
oc get project "$NS" -o yaml | head -n 30
```

### Explication
- `oc get project "$NS" || oc new-project "$NS"` : tente de lire le projet ; s’il n’existe pas, il le crée.
- `oc project "$NS"` : verrouille le contexte sur le bon namespace.
- `-o yaml` : utile pour lire rapidement les métadonnées d’un objet.

### Points observables
Dans le YAML du projet, on doit retrouver au minimum :
- `kind: Project`
- `metadata.name: ex280-lab01-zidane`
- `status.phase: Active`

### Point examen
Toujours vérifier dans quel projet on travaille avant de créer des ressources.

---

## 4. Étape 2 — Créer un pod minimal et l’inspecter

### Commande de création
```bash
# Réexport du kubeconfig CRC
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"

# Crée un pod simple qui lance un sleep 3600
oc run lab${LAB}-pod \
  --image=registry.access.redhat.com/ubi9/ubi-minimal \
  --restart=Never \
  -- sleep 3600
```

### Explication
- `oc run` permet de créer rapidement un pod simple.
- `--restart=Never` garantit la création d’un **Pod** et non d’un Deployment.
- `sleep 3600` maintient le conteneur vivant pendant 1 heure.

### Vérification rapide
```bash
# Affiche le pod avec nœud, IP, statut
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc get pod -o wide
```

### Inspection détaillée
```bash
# Décrit le pod : image, état, événements, security context, etc.
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc describe pod lab${LAB}-pod | sed -n '1,140p'
```

### Interprétation utile
Deux cas sont normaux :
- `Running` : le `sleep 3600` est encore en cours ;
- `Completed` / `Succeeded` : le `sleep 3600` s’est terminé normalement.

### Ce que nous avons observé en pratique
Le pod était en `Succeeded` avec :
- `Exit Code: 0`
- `Reason: Completed`

Cela signifie :
- pas d’échec ;
- le processus s’est terminé normalement.

### Point examen
Ne jamais considérer automatiquement `Completed` comme une erreur.  
Vérifier toujours :
- `State`
- `Reason`
- `Exit Code`
- `Events`

---

## 5. Étape 3 — Requêtes utiles avec `jsonpath`, `custom-columns` et tri

### 5.1 Extraire nom, phase et nœud avec `jsonpath`
```bash
# Extrait précisément trois champs depuis le JSON du pod
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc get pod lab${LAB}-pod \
  -o jsonpath='{.metadata.name}{"  "}{.status.phase}{"  "}{.spec.nodeName}{"\n"}'
```

### Exemple de sortie attendue
```text
lab01-pod  Succeeded  crc
```

### Explication
`jsonpath` est très utile à l’examen pour lire vite une information sans noyer la sortie.

---

### 5.2 Afficher les pods en colonnes lisibles
```bash
# Crée un tableau lisible avec des colonnes choisies
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc get pods \
  -o custom-columns=NAME:.metadata.name,PHASE:.status.phase,NODE:.spec.nodeName,IMAGE:.spec.containers[0].image
```

### Exemple de sortie attendue
```text
NAME        PHASE       NODE   IMAGE
lab01-pod   Succeeded   crc    registry.access.redhat.com/ubi9/ubi-minimal
```

### Explication
`custom-columns` est pratique quand on veut une sortie tabulaire claire.

---

### 5.3 Trier par date de création
```bash
# Trie les pods par date de création
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc get pods --sort-by=.metadata.creationTimestamp
```

### Explication
Très utile dans un namespace où plusieurs objets existent déjà.

### Point examen
- `jsonpath` : extraction précise
- `custom-columns` : lecture rapide
- `--sort-by` : ordre utile pour diagnostiquer

---

## 6. Étape 4 — Images, ImageStreams, tags et digests

OpenShift introduit la notion d’**ImageStream**.

### Rappels utiles
- **Tag** : nom lisible, par exemple `latest`
- **Digest** : identifiant immuable de l’image, par exemple `sha256:...`

Le digest est fondamental pour :
- la reproductibilité ;
- la traçabilité ;
- la sécurité.

---

### 6.1 Créer un ImageStream
```bash
# Crée un ImageStream nommé hello
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc create imagestream hello || true
```

### Explication
- si l’ImageStream existe déjà, `|| true` évite de bloquer.

---

### 6.2 Import initial prévu par le lab
```bash
# Commande prévue initialement dans le lab
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc import-image hello:latest --from=quay.io/libpod/hello --confirm
```

### Problème rencontré en pratique
Sur cet environnement, l’import a échoué avec un message de type :
- `Unauthorized`
- ou accès impossible à `quay.io/libpod/hello:latest`

Dans ce cas, le YAML montre :
- `ImportSuccess=False`
- `items: null`

### Vérification de l’ImageStream
```bash
# Affiche le YAML de l'ImageStream pour voir spec.tags et status.tags
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc get is hello -o yaml | sed -n '1,120p'
```

### Ce qu’il faut lire
- `spec.tags` : source déclarée
- `status.tags` : état réel de l’import
- `status.tags[].items[0].image` : digest si l’import a réussi

---

### 6.3 Correction appliquée sur CRC
Comme la source `quay.io/libpod/hello` a posé problème, nous avons redirigé le tag vers une image déjà accessible dans l’environnement.

```bash
# Remplace la source du tag hello:latest par une image Red Hat accessible
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc tag --source=docker registry.access.redhat.com/ubi9/ubi-minimal hello:latest
```

### Pourquoi `oc tag` et non `oc import-image`
Quand un tag existe déjà, `oc import-image` peut refuser de changer sa source.  
`oc tag --source=docker ...` est alors la bonne commande pour le retargeting.

### Vérification après correction
```bash
# Vérifie que l'ImageStream pointe bien vers la nouvelle image et qu'un digest existe
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc get is hello -o yaml | sed -n '1,120p'
```

On doit maintenant voir :
- `from.name: registry.access.redhat.com/ubi9/ubi-minimal`
- `status.tags[].items[0].image: sha256:...`

---

### 6.4 Extraire le digest avec `jsonpath`
```bash
# Extrait directement le digest de l'ImageStream
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc get is hello -o jsonpath='{.status.tags[0].items[0].image}{"\n"}'
```

### Exemple de sortie attendue
```text
sha256:5c8d55e845e14343bb84994a4d0a09002621ac0393f1f2bafc8aa219606ae451
```

### Point examen
Quand un import d’image échoue :
1. lire le message d’erreur ;
2. inspecter l’ImageStream en YAML ;
3. corriger la source si nécessaire ;
4. vérifier à nouveau le digest.

---

## 7. Étape 5 — Export YAML d’un objet

### Export du pod vers un fichier
```bash
# Exporte le YAML complet du pod dans un fichier temporaire
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc get pod lab${LAB}-pod -o yaml > /tmp/lab${LAB}-pod.yaml

# Vérifie que le fichier existe
ls -l /tmp/lab${LAB}-pod.yaml
```

### Affichage partiel du fichier
```bash
# Lit les 40 premières lignes du YAML exporté
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
head -n 40 /tmp/lab${LAB}-pod.yaml
```

### Ce qu’il faut observer
- `apiVersion: v1`
- `kind: Pod`
- `metadata.name: lab01-pod`
- `metadata.namespace: ex280-lab01-zidane`
- l’image du conteneur

### Utilité
Cette pratique est très utile pour :
- analyser un objet ;
- versionner une ressource ;
- préparer une approche déclarative.

---

## 8. Routine simple de diagnostic à retenir

En cas de comportement inattendu pendant un lab, utiliser cette séquence :

```bash
# Vérifie le projet courant
oc project

# Liste les pods avec informations réseau et nœud
oc get pods -o wide

# Affiche les événements récents
oc get events --sort-by=.lastTimestamp | tail -n 30

# Décrit l'objet concerné
oc describe pod <nom-du-pod>

# Lit les logs si le conteneur a démarré
oc logs <nom-du-pod>
```

### But
- vérifier le contexte ;
- identifier les erreurs réseau, image, scheduling ou runtime ;
- aller du plus rapide au plus détaillé.

---

## 9. Vérifications finales du lab 01

Le lab est considéré comme validé si les points suivants sont vrais :
- le projet `ex280-lab01-zidane` existe ;
- le pod `lab01-pod` a été créé ;
- une requête `jsonpath` a fonctionné ;
- une sortie `custom-columns` a fonctionné ;
- le tri `--sort-by` a fonctionné ;
- l’ImageStream `hello` possède un digest ;
- le pod a été exporté en YAML.

### Récapitulatif des commandes essentielles
```bash
# Variables du lab
export LAB=01
export NS=ex280-lab${LAB}-zidane
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"

# Projet
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
oc get project "$NS" -o yaml | head -n 30

# Pod
oc run lab${LAB}-pod --image=registry.access.redhat.com/ubi9/ubi-minimal --restart=Never -- sleep 3600
oc get pod -o wide
oc describe pod lab${LAB}-pod | sed -n '1,140p'

# Requêtes
oc get pod lab${LAB}-pod -o jsonpath='{.metadata.name}{"  "}{.status.phase}{"  "}{.spec.nodeName}{"\n"}'
oc get pods -o custom-columns=NAME:.metadata.name,PHASE:.status.phase,NODE:.spec.nodeName,IMAGE:.spec.containers[0].image
oc get pods --sort-by=.metadata.creationTimestamp

# Images / ImageStream
oc create imagestream hello || true
oc import-image hello:latest --from=quay.io/libpod/hello --confirm
oc get is hello -o yaml | sed -n '1,120p'
oc tag --source=docker registry.access.redhat.com/ubi9/ubi-minimal hello:latest
oc get is hello -o yaml | sed -n '1,120p'
oc get is hello -o jsonpath='{.status.tags[0].items[0].image}{"\n"}'

# Export YAML
oc get pod lab${LAB}-pod -o yaml > /tmp/lab${LAB}-pod.yaml
head -n 40 /tmp/lab${LAB}-pod.yaml
```

---

## 10. Nettoyage

```bash
# Supprime le projet du lab et toutes ses ressources
export KUBECONFIG="$HOME/.kube/crc-kubeconfig"
oc delete project "$NS"
```

---

## 11. Points à retenir pour EX280

- toujours vérifier le projet courant ;
- garder la main sur `KUBECONFIG` en environnement local ;
- savoir lire rapidement un `describe` ;
- distinguer un `Completed` normal d’un échec ;
- savoir extraire une information avec `jsonpath` ;
- savoir rendre une sortie lisible avec `custom-columns` ;
- comprendre la différence entre tag et digest ;
- savoir corriger la source d’un `ImageStreamTag` avec `oc tag`.

---

## 12. Résumé très court

Dans ce lab, on apprend à :
1. créer un projet ;
2. créer un pod ;
3. interroger les objets OpenShift efficacement ;
4. manipuler un ImageStream ;
5. récupérer un digest ;
6. exporter un objet YAML.

C’est un excellent socle pour les labs suivants plus déclaratifs, réseau, sécurité et RBAC.

