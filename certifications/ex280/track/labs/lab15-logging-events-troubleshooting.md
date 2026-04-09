# Lab15 — Logging, Events & Troubleshooting

## Objectif

Installer une routine de diagnostic stable :

- image invalide ;
- probe cassée ;
- Service sans Endpoints ;
- quota dépassé.

## Pré-requis

```bash
export LAB=15
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Routine

```bash
oc project
oc get pods -o wide
oc get events --sort-by=.lastTimestamp | tail -n 30
oc describe <ressource>
oc logs <pod> --all-containers --tail=200
```

## Scénario A — Image invalide
```bash
oc create deployment bad-image --image=doesnotexist.invalid/foo:latest
oc get pods
oc describe pod -l app=bad-image
oc get events --sort-by=.lastTimestamp | tail -n 30
oc set image deployment/bad-image bad-image=registry.access.redhat.com/ubi8/httpd-24
oc rollout status deployment/bad-image
```

## Scénario B — Mauvaise probe
```bash
cat <<'YAML' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bad-probe
spec:
  replicas: 1
  selector:
    matchLabels:
      app: bad-probe
  template:
    metadata:
      labels:
        app: bad-probe
    spec:
      containers:
      - name: httpd
        image: registry.access.redhat.com/ubi8/httpd-24
        ports:
        - containerPort: 8080
        readinessProbe:
          httpGet:
            path: /does-not-exist
            port: 8080
          initialDelaySeconds: 5
        livenessProbe:
          httpGet:
            path: /does-not-exist
            port: 8080
          initialDelaySeconds: 10
YAML

oc get pods
oc describe pod -l app=bad-probe
oc patch deployment bad-probe --type='json' -p='[
  {"op":"replace","path":"/spec/template/spec/containers/0/readinessProbe/httpGet/path","value":"/"},
  {"op":"replace","path":"/spec/template/spec/containers/0/livenessProbe/httpGet/path","value":"/"}
]'
oc rollout status deployment/bad-probe
```

## Scénario C — Service sans Endpoints
```bash
oc create deployment selector-demo --image=registry.access.redhat.com/ubi8/httpd-24 --port=8080
oc rollout status deployment/selector-demo

cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: Service
metadata:
  name: selector-demo-svc
spec:
  selector:
    app: wrong-label
  ports:
  - port: 8080
    targetPort: 8080
YAML

oc get svc,endpoints
oc describe svc selector-demo-svc
oc patch svc selector-demo-svc -p '{"spec":{"selector":{"app":"selector-demo"}}}'
oc get endpoints selector-demo-svc
```

## Scénario D — Quota dépassé
```bash
cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: ResourceQuota
metadata:
  name: rq-trouble
spec:
  hard:
    pods: "1"
YAML

oc run quota-pod-1 --image=registry.access.redhat.com/ubi8/ubi-minimal --restart=Never -- sleep 300
oc run quota-pod-2 --image=registry.access.redhat.com/ubi8/ubi-minimal --restart=Never -- sleep 300 || true
oc describe quota rq-trouble
oc delete pod quota-pod-1
```

## Vérifications

- `ImagePullBackOff` observé puis corrigé
- probe cassée observée puis corrigée
- Service sans endpoints observé puis corrigé
- quota dépassé observé

## Nettoyage
```bash
oc delete all --all
oc delete quota rq-trouble --ignore-not-found
oc delete project "$NS"
```
