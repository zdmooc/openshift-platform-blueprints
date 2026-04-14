# 04E — ConfigMap and Secret combined

## Objectif
Injecter simultanément ConfigMap et Secret dans une même application.

## Commandes
```bash

oc new-project ex288-04e || oc project ex288-04e

cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_MESSAGE: hello-combined
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
stringData:
  APP_TOKEN: combo-secret
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: combo-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: combo-app
  template:
    metadata:
      labels:
        app: combo-app
    spec:
      containers:
        - name: app
          image: registry.access.redhat.com/ubi9/ubi-minimal
          command: ["sh", "-c", "env; sleep 3600"]
          env:
            - name: APP_MESSAGE
              valueFrom:
                configMapKeyRef:
                  name: app-config
                  key: APP_MESSAGE
            - name: APP_TOKEN
              valueFrom:
                secretKeyRef:
                  name: app-secret
                  key: APP_TOKEN
EOF

oc describe pod -l app=combo-app

```

## Vérifications
- ConfigMap et Secret consommés
