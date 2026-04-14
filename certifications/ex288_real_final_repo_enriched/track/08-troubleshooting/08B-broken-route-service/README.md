# 08B — Broken route service

## Objectif
Corriger une exposition Service / Route qui ne fonctionne pas.

## Commandes
```bash

oc new-project ex288-08b || oc project ex288-08b

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
---
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: wrong
  ports:
    - port: 8080
      targetPort: 8080
---
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: web
spec:
  to:
    kind: Service
    name: web
  port:
    targetPort: 8080
EOF

oc get svc,route,endpoints
oc describe svc web

```

## Vérifications
- selector erroné identifié puis corrigé

## À retenir
- route -> service -> endpoints -> pod
- regarder d’abord `oc get endpoints`
