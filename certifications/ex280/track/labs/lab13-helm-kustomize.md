# Lab13 — Helm & Kustomize

## Objectif

Pratiquer :

- installation d’une release Helm simple ;
- application d’un overlay Kustomize ;
- vérification des objets.

## Pré-requis

- `helm` et `kustomize` disponibles

```bash
export LAB=13
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) Helm
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install my-nginx bitnami/nginx -n "$NS"
oc get pods -n "$NS"
```

### 2) Kustomize
```bash
mkdir -p /tmp/kustomize-lab13/base
cd /tmp/kustomize-lab13/base

cat > deployment.yaml <<'YAML'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kustom-web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: kustom-web
  template:
    metadata:
      labels:
        app: kustom-web
    spec:
      containers:
      - name: kustom-web
        image: registry.access.redhat.com/ubi8/httpd-24
YAML

cat > kustomization.yaml <<'YAML'
resources:
- deployment.yaml
YAML

kustomize build . | oc apply -f - -n "$NS"
oc get all -n "$NS"
```

## Vérifications

- release Helm présente
- Deployment `kustom-web` présent

## Nettoyage
```bash
helm uninstall my-nginx -n "$NS" || true
oc delete project "$NS"
rm -rf /tmp/kustomize-lab13
```
