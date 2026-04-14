# 04A — ConfigMap env

## Objectif
Injecter une ConfigMap en variables d’environnement.

## Commandes
```bash

oc new-project ex288-04a || oc project ex288-04a

cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_MESSAGE: hello from configmap
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cm-env-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cm-env-app
  template:
    metadata:
      labels:
        app: cm-env-app
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
EOF

oc get cm
oc describe pod -l app=cm-env-app

```

## Vérifications
- ConfigMap présente
- env injectée
