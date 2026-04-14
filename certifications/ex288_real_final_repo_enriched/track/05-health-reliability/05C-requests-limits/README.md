# 05C — Requests and limits

## Objectif
Configurer requests et limits pour un conteneur.

## Commandes
```bash

oc new-project ex288-05c || oc project ex288-05c

cat <<'EOF' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rl-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rl-app
  template:
    metadata:
      labels:
        app: rl-app
    spec:
      containers:
        - name: app
          image: registry.access.redhat.com/ubi9/ubi-minimal
          command: ["sh", "-c", "sleep 3600"]
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 256Mi
EOF

oc describe deploy rl-app

```

## Vérifications
- requests/limits visibles
