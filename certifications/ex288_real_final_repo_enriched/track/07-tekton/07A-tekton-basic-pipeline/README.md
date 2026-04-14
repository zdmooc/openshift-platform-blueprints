# 07A — Tekton basic pipeline

## Objectif
Créer une Task, un Pipeline et un PipelineRun.

## Commandes
```bash

oc new-project ex288-07a || oc project ex288-07a
oc apply -f shared/tekton/task-echo.yaml
oc apply -f shared/tekton/pipeline-basic.yaml
oc apply -f shared/tekton/pipelinerun-basic.yaml
oc get task,pipeline,pipelinerun

```

## Vérifications
- PipelineRun visible

## Notes
Nécessite Tekton installé.
