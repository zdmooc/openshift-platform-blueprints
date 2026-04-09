# Lab09 — ServiceAccounts, RBAC & API Access

## Objectif

Pratiquer :

- ServiceAccount ;
- Role + RoleBinding ;
- accès API Kubernetes en lecture seule ;
- vérification d’un refus `403`.

## Pré-requis

```bash
export LAB=09
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) SA + Role + RoleBinding
```bash
oc create sa api-reader

cat <<'YAML' | oc apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get","list","watch"]
YAML

oc create rolebinding api-reader-binding --role=pod-reader --serviceaccount="$NS":api-reader
oc get rolebinding api-reader-binding -o yaml | sed -n '1,200p'
```

### 2) Pod client API
```bash
cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: api-client
spec:
  serviceAccountName: api-reader
  containers:
  - name: api-client
    image: registry.access.redhat.com/ubi9/ubi-minimal
    command: ["/bin/sh","-c"]
    args:
      - |
        TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
        CACERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        NS=$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace)
        curl -sS --cacert "$CACERT" -H "Authorization: Bearer $TOKEN" \
          "https://kubernetes.default.svc/api/v1/namespaces/$NS/pods" | head -c 400
        echo
        sleep 3600
YAML
oc wait --for=condition=Ready pod/api-client --timeout=120s
oc logs api-client | head -n 30
```

### 3) Action interdite
```bash
oc exec api-client -- sh -c '
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
CACERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
NS=$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace)
curl -sS -o /dev/null -w "%{http_code}\n" --cacert "$CACERT" -H "Authorization: Bearer $TOKEN" \
  -X DELETE "https://kubernetes.default.svc/api/v1/namespaces/$NS/pods/somepod"
'
```

## Vérifications

- lecture OK
- DELETE retourne `403`

## Nettoyage
```bash
oc delete project "$NS"
```
