# 08D — Broken selector

## Objectif
Corriger un Service qui ne cible pas le bon label.

## Commandes
```bash

oc new-project ex288-08d || oc project ex288-08d

cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: good-pod
  labels:
    app: good-label
spec:
  containers:
    - name: app
      image: registry.access.redhat.com/ubi9/ubi-minimal
      command: ["sh", "-c", "sleep 3600"]
---
apiVersion: v1
kind: Service
metadata:
  name: broken-service
spec:
  selector:
    app: wrong-label
  ports:
    - port: 8080
      targetPort: 8080
EOF

oc get svc,endpoints,pods --show-labels
oc describe svc broken-service

```

## Vérifications
- selector corrigé
- endpoints visibles
