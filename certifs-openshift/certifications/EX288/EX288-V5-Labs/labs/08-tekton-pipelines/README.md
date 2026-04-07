# Lab 08 — Pipelines Tekton

## Temps cible
25 minutes

## Objectif
Créer une Task, un Pipeline et un PipelineRun, puis corriger une Task cassée.

## Préparation
```bash
oc new-project ex288-lab08
oc apply -f ../../shared/tekton/task-echo.yaml
oc apply -f ../../shared/tekton/pipeline-basic.yaml
oc apply -f ../../shared/tekton/pipelinerun-basic.yaml
```
