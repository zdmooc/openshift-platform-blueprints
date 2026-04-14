# 08C — Broken probes

## Objectif
Corriger des probes mal configurées.

## Commandes
```bash

oc new-project ex288-08c || oc project ex288-08c

cat <<'EOF' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: probe-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: probe-app
  template:
    metadata:
      labels:
        app: probe-app
    spec:
      containers:
        - name: app
          image: registry.access.redhat.com/ubi9/httpd-24
          ports:
            - containerPort: 8080
          livenessProbe:
            httpGet:
              path: /wrong
              port: 8080
            initialDelaySeconds: 1
          readinessProbe:
            httpGet:
              path: /wrong
              port: 8080
            initialDelaySeconds: 1
EOF

oc get pods
oc describe pod -l app=probe-app

```

## Vérifications
- mauvaise configuration de probe identifiée puis corrigée
