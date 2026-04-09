# Lab01 — Projects, Context, Query & Images

## Objectif

Pratiquer :

- création / suppression de projets ;
- manipulation du contexte `oc` ;
- requêtes utiles (`jsonpath`, `custom-columns`, tri) ;
- lecture d’images (tags / digests) ;
- export d’objets YAML.

## Pré-requis

```bash
export LAB=01
export NS=ex280-lab${LAB}-zidane
```

## Tâches

### 1) Créer un projet
```bash
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
oc get project "$NS" -o yaml | head -n 30
```

### 2) Pod minimal et inspection
```bash
oc run lab${LAB}-pod --image=registry.access.redhat.com/ubi9/ubi-minimal --restart=Never -- sleep 3600
oc get pod -o wide
oc describe pod lab${LAB}-pod | sed -n '1,140p'
```

### 3) Requêtes et formats
```bash
oc get pod lab${LAB}-pod -o jsonpath='{.metadata.name}{"  "}{.status.phase}{"  "}{.spec.nodeName}{"\n"}'
oc get pods -o custom-columns=NAME:.metadata.name,PHASE:.status.phase,NODE:.spec.nodeName,IMAGE:.spec.containers[0].image
oc get pods --sort-by=.metadata.creationTimestamp
```

### 4) Images : tag et digest
```bash
oc create imagestream hello || true
oc import-image hello:latest --from=quay.io/libpod/hello --confirm
oc get is hello -o yaml | sed -n '1,120p'
oc get is hello -o jsonpath='{.status.tags[0].items[0].image}{"\n"}'
```

### 5) Export YAML
```bash
oc get pod lab${LAB}-pod -o yaml > /tmp/lab${LAB}-pod.yaml
head -n 40 /tmp/lab${LAB}-pod.yaml
```

## Vérifications

- projet créé ;
- pod `lab01-pod` présent ;
- une requête `jsonpath` fonctionne ;
- l’ImageStream `hello` possède un digest.

## Nettoyage
```bash
oc delete project "$NS"
```
