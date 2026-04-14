# 05A — Liveness and readiness

## Objectif
Configurer liveness et readiness sur une application simple.

## Commandes
```bash

oc new-project ex288-05a || oc project ex288-05a

cat <<'EOF' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: health-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: health-app
  template:
    metadata:
      labels:
        app: health-app
    spec:
      containers:
        - name: app
          image: image-registry.openshift-image-registry.svc:5000/ex288-05a/basic-node:latest
          ports:
            - containerPort: 8080
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 10
          readinessProbe:
            httpGet:
              path: /readyz
              port: 8080
            initialDelaySeconds: 5
EOF

# si l'image n'existe pas encore, la construire d'abord via BuildConfig binaire
oc describe deploy health-app

```

## Vérifications
- probes visibles
- pod Ready quand l’image est disponible

## Notes
Réutiliser une image déjà construite dans le namespace ou créer le BuildConfig binaire avant.
