# Lab10 — SCC, Privileged & Runtime Security

## Objectif

Pratiquer :

- ServiceAccount dédiée ;
- pod privilégié ;
- erreur SCC ;
- binding de SCC ;
- validation du démarrage.

## Pré-requis

- cluster OpenShift avec SCC actives
- droits admin recommandés

```bash
export LAB=10
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) ServiceAccount
```bash
oc create sa privileged-sa
```

### 2) Pod privilégié
```bash
cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: privileged-test
spec:
  serviceAccountName: privileged-sa
  containers:
  - name: privileged-test
    image: registry.access.redhat.com/ubi9/ubi-minimal
    securityContext:
      privileged: true
    command: ["/bin/sh","-c"]
    args:
      - |
        id
        sleep 3600
YAML

oc get pod privileged-test -w
```

### 3) Diagnostic
```bash
oc describe pod privileged-test | sed -n '1,220p'
oc get events --sort-by=.metadata.creationTimestamp | tail -n 30
```

### 4) Appliquer la SCC
```bash
oc adm policy add-scc-to-user privileged -z privileged-sa -n "$NS"
oc get pod privileged-test -w
```

### 5) Vérifier
```bash
oc exec privileged-test -- id
oc get pod privileged-test -o jsonpath='{.metadata.annotations.openshift\.io/scc}{"\n"}'
```

## Nettoyage
```bash
oc delete project "$NS"
```
