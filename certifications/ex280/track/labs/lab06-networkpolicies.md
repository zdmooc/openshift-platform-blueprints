# Lab06 — NetworkPolicies

## Objectif

Pratiquer :

- isolation réseau ;
- règle d’autorisation ciblée ;
- tests client / intruder ;
- lecture des policies.

## Pré-requis

```bash
export LAB=06
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) Déployer backend + frontend + intruder
```bash
oc new-app --name=backend --image=registry.access.redhat.com/ubi9/httpd-24
oc rollout status deploy/backend
oc expose svc/backend --port=8080 --target-port=8080 --name=backend

oc run frontend --image=registry.access.redhat.com/ubi9/ubi-minimal --restart=Never -- sleep 3600
oc run intruder --image=registry.access.redhat.com/ubi9/ubi-minimal --restart=Never -- sleep 3600
oc wait --for=condition=Ready pod/frontend --timeout=120s
oc wait --for=condition=Ready pod/intruder --timeout=120s
```

### 2) Vérifier l’accès avant policy
```bash
oc exec frontend -- sh -c "curl -sS -m 2 http://backend:8080/ >/dev/null && echo OK || echo FAIL"
oc exec intruder -- sh -c "curl -sS -m 2 http://backend:8080/ >/dev/null && echo OK || echo FAIL"
```

### 3) Deny-all sur backend
```bash
cat <<'YAML' | oc apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-deny-all
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
YAML
```

### 4) Autoriser uniquement frontend
```bash
oc label pod frontend role=frontend --overwrite

cat <<'YAML' | oc apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-allow-frontend
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
YAML
```

### 5) Tester
```bash
oc exec frontend -- sh -c "curl -sS -m 2 http://backend:8080/ >/dev/null && echo OK || echo FAIL"
oc exec intruder -- sh -c "curl -sS -m 2 http://backend:8080/ >/dev/null && echo OK || echo FAIL"
oc get networkpolicy
oc describe networkpolicy backend-allow-frontend | sed -n '1,200p'
```

## Nettoyage
```bash
oc delete project "$NS"
```
