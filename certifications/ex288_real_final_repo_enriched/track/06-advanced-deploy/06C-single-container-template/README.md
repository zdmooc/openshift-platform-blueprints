# 06C — Single container template

## Objectif
Déployer via template mono-conteneur.

## Commandes
```bash

oc new-project ex288-06c || oc project ex288-06c

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

mkdir -p rendered/ex288-06c
sed 's/CHANGE_ME/ex288-06c/g' shared/templates/basic-node-template.yaml > rendered/ex288-06c/basic-node-template.yaml

oc process -f rendered/ex288-06c/basic-node-template.yaml -p APP_NAME=tplapp | oc apply -f -

```

## Vérifications
- objets créés via template
