# Lab11 — Quotas, LimitRange, ProjectTemplate & Scaling

## Objectif

Pratiquer :

- ResourceQuota ;
- LimitRange ;
- effet des defaults ;
- dépassement de quota ;
- scaling ;
- HPA si métriques disponibles ;
- template de projet en option.

## Pré-requis

- certains points demandent des droits admin

```bash
export LAB=11
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Partie A — ResourceQuota et LimitRange

### 1) ResourceQuota
```bash
cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: ResourceQuota
metadata:
  name: rq-small
spec:
  hard:
    pods: "5"
    requests.cpu: "500m"
    requests.memory: 512Mi
    limits.cpu: "1"
    limits.memory: 1Gi
YAML
oc describe quota rq-small
```

### 2) LimitRange
```bash
cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: LimitRange
metadata:
  name: lr-defaults
spec:
  limits:
  - type: Container
    default:
      cpu: "200m"
      memory: "256Mi"
    defaultRequest:
      cpu: "50m"
      memory: "64Mi"
    max:
      cpu: "500m"
      memory: "512Mi"
YAML
oc describe limitrange lr-defaults
```

### 3) Pod sans resources
```bash
oc run lr-test --image=registry.access.redhat.com/ubi9/ubi-minimal --restart=Never -- sleep 3600
oc wait --for=condition=Ready pod/lr-test --timeout=120s
oc get pod lr-test -o jsonpath='{.spec.containers[0].resources}{"\n"}'
```

### 4) Dépassement quota
```bash
for i in $(seq 1 10); do oc run p$i --image=registry.access.redhat.com/ubi9/ubi-minimal --restart=Never -- sleep 3600 || true; done
oc get pods
oc describe quota rq-small | sed -n '1,180p'
```

## Partie B — Scaling et HPA (option)

### 5) Deployment + scaling
```bash
oc create deployment quota-web --image=registry.access.redhat.com/ubi8/httpd-24
oc scale deployment quota-web --replicas=3
oc get pods
```

### 6) HPA (si métriques disponibles)
```bash
oc autoscale deployment quota-web --min=1 --max=5 --cpu-percent=50 || true
oc get hpa
```

## Partie C — Project Request Template (option cluster)

### 7) Exemple minimal
Créer un template de projet par défaut si ton cluster et tes droits le permettent.

## Vérifications

- quota lisible ;
- defaults injectés ;
- dépassement observable ;
- HPA visible si supporté.

## Nettoyage
```bash
oc delete project "$NS"
```
