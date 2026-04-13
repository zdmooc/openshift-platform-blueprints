# EX288 — Book consolidé (book-v1)

Version consolidée en un seul fichier Markdown à partir du contenu utile de `certifications/ex288/book-v1`.

## Sommaire

1. Positionnement du book  
2. Structure initiale  
3. Préparation de l’environnement  
4. Labs consolidés  
   - Lab 00 — Setup projet  
   - Lab 01 — Build S2I depuis Git  
   - Lab 02 — Déployer DC + Service + Route + ConfigMap  
   - Lab 03 — Variables d’environnement, probes et rollouts  
   - Lab 04 — Template paramétré  
   - Lab 05 — PVC / stockage  
5. Manifests de référence  
6. Concepts OpenShift — synthèse MAIF  
7. Conseils d’usage  
8. Ce que tu peux supprimer ensuite

---

## 1) Positionnement du book

Ce book a pour objectif de pratiquer les gestes utiles pour la préparation de l’EX288 sur CRC ou OpenShift :
- builds et déploiements
- exposition réseau
- configuration applicative
- templates
- vérifications rapides
- enchaînement de commandes terrain

---

## 2) Structure initiale

Le `book-v1` était organisé autour des éléments suivants :

- `apps/` : code d’application exemple
- `labs/` : travaux pratiques pas à pas
- `manifests/` : YAML OpenShift
- `cheatsheets/` : commandes utiles
- `scripts/` : vérifs et nettoyage
- `qcm/` : questions type examen
- `refs/` : plan et liens
- `mermaid/` : schémas et notes de concepts

L’objectif de ce fichier est de conserver le contenu utile en un seul endroit, sans garder l’arborescence historique.

---

## 3) Préparation de l’environnement

### Création du projet

```bash
oc new-project ex288 || oc project ex288
```

### Vérifications de base

```bash
oc whoami
oc project
oc get all -n ex288
```

### Vue complète utile

```bash
oc get deploy,dc,rs,rc,po,svc,route,cm,secret -n ex288 -o wide
```

### Chaîne d’images

```bash
oc get bc,is,istag -n ex288
oc describe bc -n ex288
oc describe is -n ex288
```

### Événements récents

```bash
oc get events -n ex288 --sort-by=.lastTimestamp
```

### Détails d’un workload

```bash
oc describe dc/<name> -n ex288
oc describe deploy/<name> -n ex288
```

---

## 4) Labs consolidés

## Lab 00 — Setup projet

### Objectif
Préparer le namespace de travail et disposer d’une batterie minimale de vérification.

### Commandes

```bash
oc new-project ex288 || oc project ex288
oc whoami
oc project
oc get all -n ex288
oc get deploy,dc,rs,rc,po,svc,route,cm,secret -n ex288 -o wide
oc get bc,is,istag -n ex288
oc describe bc -n ex288
oc describe is -n ex288
oc get events -n ex288 --sort-by=.lastTimestamp
oc describe dc/<name> -n ex288
oc describe deploy/<name> -n ex288
```

### Résultat attendu
- le projet `ex288` existe
- l’utilisateur courant est bien authentifié
- la vue des objets du namespace est accessible

---

## Lab 01 — Build S2I depuis Git

### Objectif
Construire une image via BuildConfig / ImageStream à partir d’un dépôt Git.

### Étapes

1. Remplacer l’URL Git dans le manifest.
2. Appliquer le manifest de build.
3. Lancer le build et suivre son exécution.
4. Vérifier les objets de build/image.

### Commandes

```bash
sed -i 's#REPLACE_WITH_YOUR_REPO_URL#https://github.com/zdmooc/openshift-ex288.git#g' manifests/bc-is.yaml
oc apply -n ex288 -f manifests/bc-is.yaml
oc start-build ex288 -n ex288 --follow
oc get is,bc,build -n ex288
```

### Vérifications
- le `BuildConfig` existe
- le build aboutit
- l’`ImageStream` reçoit un tag exploitable

---

## Lab 02 — Déployer DC + Service + Route + ConfigMap

### Objectif
Déployer une application via DeploymentConfig, l’exposer par Service et Route, puis vérifier l’accès.

### Commandes

```bash
oc apply -n ex288 -f manifests/cm-secret-pvc.yaml
oc apply -n ex288 -f manifests/dc-svc-route.yaml
oc rollout status dc/ex288 -n ex288
oc get dc,svc,route,pod -n ex288
curl -k https://$(oc get route ex288 -n ex288 -o jsonpath='{.spec.host}')
```

### Résultat attendu
- le `DeploymentConfig` est déployé
- le `Service` et la `Route` sont créés
- l’application répond via le hostname de la route

---

## Lab 03 — Variables d’environnement, probes et rollouts

### Objectif
Modifier la configuration d’un déploiement, ajouter des probes et maîtriser le cycle de rollout.

### Commandes

```bash
oc set env dc/ex288 MSG=updated -n ex288 --overwrite
oc rollout status dc/ex288 -n ex288

oc set probes dc/ex288 --liveness --get-url=http://:8080/ --initial-delay-seconds=10 -n ex288
oc set probes dc/ex288 --readiness --get-url=http://:8080/ --initial-delay-seconds=5 -n ex288

ochg=$(oc rollout history dc/ex288 -n ex288 | awk 'NR==2{print $1}')
# Pour annuler au précédent :
oc rollout undo dc/ex288 -n ex288
```

### Points à retenir
- `oc set env` déclenche un nouveau déploiement
- les probes doivent être cohérentes avec le port et le endpoint exposés
- `oc rollout undo` permet de revenir rapidement à l’état précédent

---

## Lab 04 — Template paramétré

### Objectif
Instancier un template OpenShift paramétrable pour créer une nouvelle application.

### Commandes

```bash
oc process -n ex288 -f manifests/template-ex288.yaml -p APP_NAME=app2 -p MSG=from-template | oc apply -f -
oc get all -n ex288 | grep app2
```

### Résultat attendu
- une nouvelle application `app2` est créée
- les objets générés (ConfigMap, DC, Service, Route) sont visibles

---

## Lab 05 — PVC / stockage

### Objectif
Vérifier ou préparer un montage de volume persistant pour l’application.

### Commande minimale

```bash
oc get pvc -n ex288
```

### Remarque
Le lab d’origine était très court. Pour le rendre réellement exploitable, il faut :
- créer ou réutiliser un PVC
- l’ajouter au `Deployment` ou `DeploymentConfig`
- monter le volume dans le conteneur
- vérifier le montage depuis un shell dans le pod

### Extension conseillée

```bash
oc set volume dc/ex288 --add --name=app-data --type=persistentVolumeClaim --claim-name=ex288-pvc --mount-path=/opt/app-root/data -n ex288
oc rollout status dc/ex288 -n ex288
oc rsh dc/ex288
```

---

## 5) Manifests de référence

## 5.1 DeploymentConfig + Service + Route

```yaml
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: ex288
spec:
  replicas: 1
  selector:
    app: ex288
  strategy:
    type: Rolling
  triggers:
  - type: ConfigChange
  - type: ImageChange
    imageChangeParams:
      automatic: true
      containerNames: [ex288]
      from:
        kind: ImageStreamTag
        name: ex288:latest
  template:
    metadata:
      labels:
        app: ex288
    spec:
      containers:
      - name: ex288
        image: ""
        ports:
        - containerPort: 8080
        env:
        - name: APP_NAME
          value: ex288
        - name: MSG
          valueFrom:
            configMapKeyRef:
              name: ex288-config
              key: msg
        readinessProbe:
          httpGet: { path: /, port: 8080 }
          initialDelaySeconds: 5
        livenessProbe:
          httpGet: { path: /, port: 8080 }
          initialDelaySeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: ex288
spec:
  selector: { app: ex288 }
  ports: [{ port: 8080, targetPort: 8080 }]
---
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: ex288
spec:
  to: { kind: Service, name: ex288 }
  port: { targetPort: 8080 }
```

### Lecture rapide
Ce manifest couvre en une seule base :
- le déploiement applicatif
- le branchement sur un `ImageStreamTag`
- l’injection d’une valeur depuis `ConfigMap`
- la publication via `Service` et `Route`
- les probes liveness/readiness

---

## 5.2 Template OpenShift paramétrable

```yaml
apiVersion: template.openshift.io/v1
kind: Template
metadata:
  name: ex288-template
parameters:
- name: APP_NAME
  value: ex288
- name: MSG
  value: hello-template
objects:
- apiVersion: v1
  kind: ConfigMap
  metadata: { name: ex288-config }
  data: { msg: '' }
- apiVersion: apps.openshift.io/v1
  kind: DeploymentConfig
  metadata: { name:  }
  spec:
    replicas: 1
    selector: { app:  }
    triggers:
    - type: ConfigChange
    - type: ImageChange
      imageChangeParams:
        automatic: true
        containerNames: []
        from: { kind: ImageStreamTag, name: :latest }
    template:
      metadata: { labels: { app:  } }
      spec:
        containers:
        - name:
          image: ""
          ports: [{ containerPort: 8080 }]
          env: [{ name: APP_NAME, value:  }]
- apiVersion: v1
  kind: Service
  metadata: { name:  }
  spec: { selector: { app:  }, ports: [{ port: 8080, targetPort: 8080 }] }
- apiVersion: route.openshift.io/v1
  kind: Route
  metadata: { name:  }
  spec: { to: { kind: Service, name:  }, port: { targetPort: 8080 } }
```

### Remarque importante
Le template conservé dans `book-v1` semble partiellement inachevé sur certaines substitutions. En pratique, il faut vérifier et compléter les champs vides avant usage réel.

---

## 6) Concepts OpenShift — synthèse MAIF

Cette partie reprend le mémo conceptuel présent dans `mermaid/maif`.

## 6.1 Cluster, nodes et environnements

Un cluster OpenShift comprend généralement :
- des nœuds de pilotage
- des nœuds d’infrastructure
- des nœuds workers
- plusieurs environnements logiques hébergés

### Commandes utiles

```bash
oc whoami
oc status
oc get nodes -o wide
oc describe node <node>
oc label node <node> node-role.kubernetes.io/infra=""
oc label node <node> node-role.kubernetes.io/worker=""
oc get nodes --show-labels
oc taint node <node> role=ingress:NoSchedule
oc get events -A --sort-by=.lastTimestamp | tail -n 50
```

## 6.2 Projet, namespace, labels, ConfigMap

Un namespace est un contexte d’exécution et de gouvernance.

```bash
oc new-project ex288
oc label ns ex288 env=TDV1 produit=NORA --overwrite
oc -n ex288 create configmap app-cfg --from-literal=PROFILE=recx
oc -n ex288 get cm
oc -n ex288 describe cm app-cfg
oc -n ex288 create secret generic app-secret --from-literal=API_KEY=changeme
oc -n ex288 get secret
```

## 6.3 Pod, conteneur et Deployment

Le pod est l’unité de base d’exécution. Il peut embarquer un conteneur principal et éventuellement des sidecars.

```bash
oc -n ex288 create deployment web --image=registry.k8s.io/echoserver:1.10
oc -n ex288 set resources deploy/web --requests=cpu=100m,memory=128Mi --limits=cpu=500m,memory=256Mi
oc -n ex288 scale deploy/web --replicas=3
oc -n ex288 set env deploy/web --from=configmap/app-cfg
oc -n ex288 get deploy,rs,pod -o wide
oc -n ex288 describe deploy web
oc -n ex288 logs deploy/web -f
oc -n ex288 rsh deploy/web sh
oc -n ex288 get events --sort-by=.lastTimestamp | tail -n 30
```

## 6.4 Service et Route

Le service sélectionne les pods par labels. La route publie le service en externe.

```bash
oc -n ex288 expose deploy/web --port=8080 --name=web
oc -n ex288 get svc web -o wide
oc -n ex288 get endpoints web
oc -n ex288 expose svc/web
oc -n ex288 get route web -o wide
oc -n ex288 rsh deploy/web curl -s http://web:8080 || true
```

## 6.5 Séquence complète de déploiement

1. appliquer un Deployment ou DeploymentConfig  
2. laisser OpenShift créer les réplicas / pods  
3. exposer par Service  
4. publier par Route  
5. tester via le hostname généré  

## 6.6 Vérifications et nettoyage

```bash
oc -n ex288 get all -o wide
oc -n ex288 get deploy web -o jsonpath='{.status.availableReplicas}{"\n"}'
oc -n ex288 get route web -o jsonpath='{.spec.host}{"\n"}'
oc -n ex288 delete route web || true
oc -n ex288 delete svc web || true
oc -n ex288 delete deploy web || true
```

### Note
La note d’origine rappelle que `DeploymentConfig` est déprécié à partir des versions récentes d’OpenShift et qu’il vaut mieux privilégier `Deployment` lorsque l’objectif d’examen ou la plateforme le permettent.

---

## 7) Conseils d’usage

Ce fichier consolidé doit être utilisé comme :
- mémo de révision
- base de labs manuels
- support rapide en session CRC / OpenShift
- point d’entrée avant de basculer sur le track plus moderne `certifications/ex288/track/`

Ordre conseillé :
1. Lab 00
2. Lab 01
3. Lab 02
4. Lab 03
5. Lab 04
6. Lab 05
7. reprise des concepts et commandes utiles

---

## 8) Ce que tu peux supprimer ensuite

Après validation de ce fichier, tu peux supprimer :
- `certifications/ex288/book-v1/`
- `certifications/ex288/archive/`

Je te conseille seulement de conserver séparément, ailleurs si besoin :
- les manifests YAML réellement réutilisables
- les éventuels schémas Mermaid que tu voudrais retravailler
- pas l’historique de commandes brut, qui mélange plusieurs sujets et plusieurs périodes

---

## Annexe — remarque sur l’historique de commandes

Le fichier `commandehistory.sh` présent dans `book-v1` ne correspond pas à un chapitre propre de préparation EX288. Il contient un historique très large mêlant ODM, Keycloak, Kind, Argo CD, IBM Licensing, CRC et autres travaux. Il n’est donc pas intégré comme section du guide consolidé.
