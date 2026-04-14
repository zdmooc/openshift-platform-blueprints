# 06D — Multi-container template

## Objectif
Déployer via template multi-conteneurs.

## Commandes
```bash

oc new-project ex288-06d || oc project ex288-06d

# construire l'image si nécessaire
cat <<'EOF' | oc apply -f -
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: basic-node
---
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: basic-node-binary
spec:
  source:
    type: Binary
  strategy:
    dockerStrategy:
      dockerfilePath: Containerfile
  output:
    to:
      kind: ImageStreamTag
      name: basic-node:latest
EOF

oc start-build basic-node-binary --from-dir=shared/apps/basic-node --follow

mkdir -p rendered/ex288-06d
sed 's/CHANGE_ME/ex288-06d/g' shared/templates/multi-container-template.yaml > rendered/ex288-06d/multi-container-template.yaml

oc process -f rendered/ex288-06d/multi-container-template.yaml -p APP_NAME=tplmulti | oc apply -f -
oc get pods

```

## Vérifications
- pod multi-conteneurs créé
