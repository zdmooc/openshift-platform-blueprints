# Lab02 — Declarative Deploy, Service, Route & Rollout

## Objectif

Pratiquer le déploiement déclaratif :

- manifests YAML ;
- `oc apply` ;
- Service + Route ;
- update contrôlé ;
- rollback.

## Pré-requis

```bash
export LAB=02
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) Créer un Deployment + Service en YAML
```bash
cat <<'YAML' > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: registry.access.redhat.com/ubi9/httpd-24
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
  - name: http
    port: 8080
    targetPort: 8080
YAML

oc apply -f deployment.yaml
oc rollout status deploy/web
oc get pods -l app=web -o wide
oc get svc web
```

### 2) Créer une Route
```bash
oc expose svc/web
oc get route web
HOST=$(oc get route web -o jsonpath='{.spec.host}')
echo "$HOST"
curl -k "http://$HOST" || true
```

### 3) Patch et rollout
```bash
oc patch deploy/web -p '{"spec":{"replicas":3}}'
oc rollout status deploy/web
oc get rs -l app=web
```

### 4) Casser l’image puis rollback
```bash
oc set image deploy/web web=registry.access.redhat.com/ubi9/httpd-24:does-not-exist
oc rollout status deploy/web || true
oc rollout history deploy/web
oc rollout undo deploy/web
oc rollout status deploy/web
```

## Vérifications

- `web` déployé ;
- Service présent ;
- Route présente ;
- rollback réussi.

## Nettoyage
```bash
oc delete project "$NS"
rm -f deployment.yaml
```
