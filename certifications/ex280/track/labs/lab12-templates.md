# Lab12 — Templates

## Objectif

Pratiquer :

- Template OpenShift ;
- paramètres ;
- `oc process` ;
- instanciation d’un Deployment + Service + Route.

## Pré-requis

```bash
export LAB=12
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) Créer un Template
```bash
cat <<'YAML' | oc apply -f -
apiVersion: template.openshift.io/v1
kind: Template
metadata:
  name: simple-web-template
objects:
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: ${APP_NAME}
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: ${APP_NAME}
    template:
      metadata:
        labels:
          app: ${APP_NAME}
      spec:
        containers:
        - name: ${APP_NAME}
          image: registry.access.redhat.com/ubi8/httpd-24
          ports:
          - containerPort: 8080
- apiVersion: v1
  kind: Service
  metadata:
    name: ${APP_NAME}
  spec:
    selector:
      app: ${APP_NAME}
    ports:
    - port: 8080
      targetPort: 8080
- apiVersion: route.openshift.io/v1
  kind: Route
  metadata:
    name: ${APP_NAME}
  spec:
    to:
      kind: Service
      name: ${APP_NAME}
parameters:
- name: APP_NAME
  required: true
YAML
```

### 2) Instancier
```bash
oc process simple-web-template -p APP_NAME=tpl-web | oc apply -f -
oc get all
oc get route tpl-web
```

## Vérifications

- `tpl-web` existe en Deployment/Service/Route

## Nettoyage
```bash
oc delete project "$NS"
```
