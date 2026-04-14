# 01D — Scaling, env, resources

## Objectif
Configurer variables d’environnement, scaling, requests et limits.

## Commandes
```bash

oc new-project ex288-01d || oc project ex288-01d

cat <<'EOF' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: res-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: res-app
  template:
    metadata:
      labels:
        app: res-app
    spec:
      containers:
        - name: app
          image: registry.access.redhat.com/ubi9/ubi-minimal
          command: ["sh", "-c", "sleep 3600"]
          env:
            - name: APP_MODE
              value: test
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 300m
              memory: 256Mi
EOF

oc scale deploy/res-app --replicas=2
oc describe deploy res-app

```

## Vérifications
- replicas à 2
- env visible
- requests/limits visibles
