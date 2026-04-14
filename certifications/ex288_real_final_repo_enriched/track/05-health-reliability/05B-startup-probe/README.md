# 05B — Startup probe

## Objectif
Configurer une startupProbe.

## Commandes
```bash

oc new-project ex288-05b || oc project ex288-05b

cat <<'EOF' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: startup-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: startup-app
  template:
    metadata:
      labels:
        app: startup-app
    spec:
      containers:
        - name: app
          image: image-registry.openshift-image-registry.svc:5000/ex288-05b/basic-node:latest
          ports:
            - containerPort: 8080
          startupProbe:
            httpGet:
              path: /startupz
              port: 8080
            failureThreshold: 30
            periodSeconds: 5
EOF

oc describe deploy startup-app

```

## Vérifications
- startup probe visible
