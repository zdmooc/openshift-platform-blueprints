# 05D — Probe troubleshooting quickfix

## Objectif
Identifier et corriger rapidement des probes erronées.

## Commandes
```bash

oc new-project ex288-05d || oc project ex288-05d

cat <<'EOF' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bad-probe-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: bad-probe-app
  template:
    metadata:
      labels:
        app: bad-probe-app
    spec:
      containers:
        - name: app
          image: registry.access.redhat.com/ubi9/httpd-24
          ports:
            - containerPort: 8080
          readinessProbe:
            httpGet:
              path: /wrong
              port: 8080
            initialDelaySeconds: 1
EOF

oc get pods
oc describe pod -l app=bad-probe-app

```

## Vérifications
- erreur de probe repérée
- correction appliquée
