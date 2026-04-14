# 08A — Broken BuildConfig

## Objectif
Diagnostiquer un BuildConfig erroné.

## Commandes
```bash

oc new-project ex288-08a || oc project ex288-08a

cat <<'EOF' | oc apply -f -
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: broken-bc
spec:
  source:
    git:
      uri: https://github.com/owner/does-not-exist.git
  strategy:
    dockerStrategy:
      dockerfilePath: Containerfile
  output:
    to:
      kind: ImageStreamTag
      name: broken:latest
EOF

oc start-build broken-bc --follow
oc logs build/broken-bc-1 || true

```

## Vérifications
- cause d’échec identifiée
