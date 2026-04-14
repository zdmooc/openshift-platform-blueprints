# 02B — Containerfile custom image

## Objectif
Construire une image personnalisée depuis un Containerfile local.

## Commandes
```bash

oc new-project ex288-02b || oc project ex288-02b

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
oc get is,build

```

## Vérifications
- build réussi
- imagestream tagué
