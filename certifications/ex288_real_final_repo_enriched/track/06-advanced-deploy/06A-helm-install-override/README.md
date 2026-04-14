# 06A — Helm install override

## Objectif
Déployer avec Helm et surcharger les valeurs.

## Commandes
```bash

oc new-project ex288-06a || oc project ex288-06a

# construire l'image si nécessaire dans le namespace
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

mkdir -p rendered/ex288-06a
sed 's/CHANGE_ME/ex288-06a/g' shared/charts/basic-node/values.yaml > rendered/ex288-06a/values.yaml

helm template basic-node shared/charts/basic-node -f rendered/ex288-06a/values.yaml
helm upgrade --install basic-node shared/charts/basic-node -f rendered/ex288-06a/values.yaml -n ex288-06a

```

## Vérifications
- release Helm présente
- objets créés

## À retenir
- `helm template` pour lire le rendu
- `helm upgrade --install` pour déployer
