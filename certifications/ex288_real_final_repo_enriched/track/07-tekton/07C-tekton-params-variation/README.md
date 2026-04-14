# 07C — Tekton params variation

## Objectif
Modifier les paramètres d’un PipelineRun Tekton.

## Commandes
```bash

oc new-project ex288-07c || oc project ex288-07c
oc apply -f shared/tekton/task-echo.yaml
oc apply -f shared/tekton/pipeline-basic.yaml

cat <<'EOF' | oc apply -f -
apiVersion: tekton.dev/v1
kind: PipelineRun
metadata:
  name: basic-pipelinerun-custom
spec:
  pipelineRef:
    name: basic-pipeline
  params:
    - name: message
      value: hello custom param
EOF

oc get pipelinerun

```

## Vérifications
- paramètre visible dans le PipelineRun

## Notes
Nécessite Tekton installé.
