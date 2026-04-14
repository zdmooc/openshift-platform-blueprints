# 04B — ConfigMap volume

## Objectif
Monter une ConfigMap comme volume.

## Commandes
```bash

oc new-project ex288-04b || oc project ex288-04b

cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  app.properties: |
    mode=test
    feature=true
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cm-vol-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cm-vol-app
  template:
    metadata:
      labels:
        app: cm-vol-app
    spec:
      volumes:
        - name: cfg
          configMap:
            name: app-config
      containers:
        - name: app
          image: registry.access.redhat.com/ubi9/ubi-minimal
          command: ["sh", "-c", "cat /etc/app/app.properties; sleep 3600"]
          volumeMounts:
            - name: cfg
              mountPath: /etc/app
EOF

oc describe pod -l app=cm-vol-app

```

## Vérifications
- ConfigMap montée comme volume
