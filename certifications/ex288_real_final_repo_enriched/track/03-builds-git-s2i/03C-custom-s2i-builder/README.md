# 03C — Custom S2I builder

## Objectif
Construire une image avec `.s2i/bin` personnalisé.

## Commandes
```bash

oc new-project ex288-03c || oc project ex288-03c

cat <<'EOF' | oc apply -f -
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: basic-node-custom-s2i
---
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: basic-node-custom-s2i
spec:
  source:
    type: Binary
  strategy:
    sourceStrategy:
      from:
        kind: DockerImage
        name: registry.access.redhat.com/ubi9/nodejs-20:latest
  output:
    to:
      kind: ImageStreamTag
      name: basic-node-custom-s2i:latest
EOF

oc start-build basic-node-custom-s2i --from-dir=shared/apps/basic-node --follow
oc get build,is

```

## Vérifications
- build custom S2I réussi
