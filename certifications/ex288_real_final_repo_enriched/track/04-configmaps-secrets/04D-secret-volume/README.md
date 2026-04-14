# 04D — Secret volume

## Objectif
Monter un Secret comme volume.

## Commandes
```bash

oc new-project ex288-04d || oc project ex288-04d

cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
stringData:
  password.txt: supersecret
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secret-vol-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: secret-vol-app
  template:
    metadata:
      labels:
        app: secret-vol-app
    spec:
      volumes:
        - name: sec
          secret:
            secretName: app-secret
      containers:
        - name: app
          image: registry.access.redhat.com/ubi9/ubi-minimal
          command: ["sh", "-c", "cat /etc/secret/password.txt; sleep 3600"]
          volumeMounts:
            - name: sec
              mountPath: /etc/secret
EOF

oc describe pod -l app=secret-vol-app

```

## Vérifications
- Secret monté comme volume
