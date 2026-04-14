# 03B — Docker strategy BuildConfig

## Objectif
Créer un BuildConfig Docker strategy depuis Git.

## Commandes
```bash

export GIT_REPO_URL=https://github.com/<owner>/<repo>.git

oc new-project ex288-03b || oc project ex288-03b

cat <<EOF | oc apply -f -
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: basic-node
---
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: basic-node-docker
spec:
  source:
    git:
      uri: ${GIT_REPO_URL}
  strategy:
    dockerStrategy:
      dockerfilePath: Containerfile
  output:
    to:
      kind: ImageStreamTag
      name: basic-node:latest
EOF

oc start-build basic-node-docker --follow
oc get build,is

```

## Vérifications
- build docker strategy réussi

## À retenir
- dockerStrategy utilise le Containerfile
- ce n’est pas du S2I
