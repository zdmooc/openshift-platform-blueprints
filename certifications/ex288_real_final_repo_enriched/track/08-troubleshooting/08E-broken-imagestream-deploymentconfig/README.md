# 08E — Broken ImageStream DeploymentConfig

## Objectif
Diagnostiquer un DeploymentConfig lié à un ImageStreamTag introuvable.

## Commandes
```bash

oc new-project ex288-08e || oc project ex288-08e

cat <<'EOF' | oc apply -f -
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: broken-dc
spec:
  replicas: 1
  selector:
    app: broken-dc
  template:
    metadata:
      labels:
        app: broken-dc
    spec:
      containers:
        - name: app
          image: image-registry.openshift-image-registry.svc:5000/ex288-08e/missing:latest
          ports:
            - containerPort: 8080
  triggers:
    - type: ConfigChange
    - type: ImageChange
      imageChangeParams:
        automatic: true
        containerNames: [app]
        from:
          kind: ImageStreamTag
          name: missing:latest
EOF

oc describe dc broken-dc
oc get is

```

## Vérifications
- ImageStreamTag manquant identifié
