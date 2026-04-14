# 01B — Single container, service, route

## Objectif
Déployer une application mono-conteneur et l’exposer.

## Commandes
```bash

oc new-project ex288-01b || oc project ex288-01b

cat <<'EOF' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 1
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
EOF

oc expose deploy/web --port=8080 --name=web
oc expose svc/web
oc get all
oc get route

```

## Vérifications
- deployment présent
- service présent
- route présente
