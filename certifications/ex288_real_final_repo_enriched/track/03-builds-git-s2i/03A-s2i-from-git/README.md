# 03A — S2I from Git

## Objectif
Créer un BuildConfig S2I depuis un dépôt Git.

## Commandes
```bash

export GIT_REPO_URL=https://github.com/<owner>/<repo>.git

oc new-project ex288-03a || oc project ex288-03a

cat <<EOF | oc apply -f -
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: basic-node-s2i
---
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: basic-node-s2i
spec:
  source:
    git:
      uri: ${GIT_REPO_URL}
  strategy:
    sourceStrategy:
      from:
        kind: DockerImage
        name: registry.access.redhat.com/ubi9/nodejs-20:latest
  output:
    to:
      kind: ImageStreamTag
      name: basic-node-s2i:latest
EOF

oc start-build basic-node-s2i --follow
oc get build,is

```

## Vérifications
- build S2I réussi
- ImageStreamTag mis à jour

## À retenir
- sourceStrategy = S2I
- Git URL valide obligatoire
- vérifier `oc get build` et `oc logs build/...`
