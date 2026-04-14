# 01E — DeploymentConfig basics

## Objectif
Créer un DeploymentConfig simple et lire ses triggers.

## Commandes
```bash

oc new-project ex288-01e || oc project ex288-01e

cat <<'EOF' | oc apply -f -
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: dc-app
spec:
  replicas: 1
  selector:
    app: dc-app
  template:
    metadata:
      labels:
        app: dc-app
    spec:
      containers:
        - name: app
          image: registry.access.redhat.com/ubi9/httpd-24
          ports:
            - containerPort: 8080
  triggers:
    - type: ConfigChange
EOF

oc get dc
oc describe dc dc-app

```

## Vérifications
- DeploymentConfig présent
- trigger ConfigChange visible
