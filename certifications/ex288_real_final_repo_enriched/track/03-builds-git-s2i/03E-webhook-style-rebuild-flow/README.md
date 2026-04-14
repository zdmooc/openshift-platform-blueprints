# 03E — Webhook style rebuild flow

## Objectif
Rejouer le flux logique d’un rebuild piloté par Git/config change.

## Commandes
```bash

export GIT_REPO_URL=https://github.com/<owner>/<repo>.git

oc new-project ex288-03e || oc project ex288-03e

cat <<EOF | oc apply -f -
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: webhook-demo
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
      name: webhook-demo:latest
  triggers:
    - type: ConfigChange
EOF

oc start-build webhook-demo --follow
oc patch bc webhook-demo -p '{"spec":{"runPolicy":"Serial"}}'
oc describe bc webhook-demo

```

## Vérifications
- build déclenché
- logique de redéclenchement comprise

## Notes
Ce lab travaille le geste BuildConfig + redéclenchement.
