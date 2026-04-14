# 04C — Secret env

## Objectif
Injecter un Secret en variable d’environnement.

## Commandes
```bash

oc new-project ex288-04c || oc project ex288-04c

cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
stringData:
  APP_TOKEN: s3cr3t-token
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secret-env-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: secret-env-app
  template:
    metadata:
      labels:
        app: secret-env-app
    spec:
      containers:
        - name: app
          image: registry.access.redhat.com/ubi9/ubi-minimal
          command: ["sh", "-c", "env; sleep 3600"]
          env:
            - name: APP_TOKEN
              valueFrom:
                secretKeyRef:
                  name: app-secret
                  key: APP_TOKEN
EOF

oc get secret
oc describe pod -l app=secret-env-app

```

## Vérifications
- Secret présent
- env injectée
