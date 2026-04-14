# 02A — ImageStream basics

## Objectif
Créer un ImageStream simple et l’inspecter.

## Commandes
```bash

oc new-project ex288-02a || oc project ex288-02a

cat <<'EOF' | oc apply -f -
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: basic-node
EOF

oc get is
oc describe is basic-node

```

## Vérifications
- imagestream présent
