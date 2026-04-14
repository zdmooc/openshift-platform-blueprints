# 03D — Hooks and triggers

## Objectif
Créer un build avec postCommit et un déploiement déclenché sur changement d’image.

## Commandes
```bash

export GIT_REPO_URL=https://github.com/<owner>/<repo>.git

oc new-project ex288-03d || oc project ex288-03d

cat <<EOF | oc apply -f -
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: basic-node
---
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: basic-node-hooked
spec:
  source:
    git:
      uri: ${GIT_REPO_URL}
  strategy:
    dockerStrategy:
      dockerfilePath: Containerfile
  postCommit:
    script: |
      echo "postCommit hook executed"
      test -f /opt/app-root/src/server.js
  output:
    to:
      kind: ImageStreamTag
      name: basic-node:latest
  triggers:
    - type: ConfigChange
---
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: basic-node
spec:
  replicas: 1
  selector:
    app: basic-node
  template:
    metadata:
      labels:
        app: basic-node
    spec:
      containers:
        - name: app
          image: image-registry.openshift-image-registry.svc:5000/ex288-03d/basic-node:latest
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
          name: basic-node:latest
EOF

oc start-build basic-node-hooked --follow
oc logs build/basic-node-hooked-1 || true
oc describe dc basic-node

```

## Vérifications
- postCommit visible dans les logs
- image trigger visible
