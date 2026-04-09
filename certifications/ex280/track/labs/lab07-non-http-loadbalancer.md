# Lab07 — Non-HTTP / LoadBalancer

## Objectif

Pratiquer l’exposition d’un service non-HTTP :

- Service `LoadBalancer` ;
- test externe si disponible ;
- branche CRC via `port-forward`.

## Pré-requis

```bash
export LAB=07
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) Déployer un serveur TCP simple
```bash
cat <<'YAML' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tcp-echo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tcp-echo
  template:
    metadata:
      labels:
        app: tcp-echo
    spec:
      containers:
      - name: tcp-echo
        image: registry.access.redhat.com/ubi9/ubi-minimal
        command: ["/bin/sh","-c"]
        args:
          - |
            while true; do nc -lk -p 8080 -e /bin/cat; done
YAML

oc rollout status deploy/tcp-echo || true
```

> Si `nc -e` n’est pas disponible dans ton image locale, remplace cette partie par une image echo TCP valide de ton environnement.

### 2) Service LoadBalancer
```bash
cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: Service
metadata:
  name: tcp-echo-lb
spec:
  type: LoadBalancer
  selector:
    app: tcp-echo
  ports:
  - name: tcp
    port: 9000
    targetPort: 8080
YAML

oc get svc tcp-echo-lb -o wide
oc describe svc tcp-echo-lb | sed -n '1,200p'
```

### 3) Test
#### Branche A — cluster avec LB
```bash
oc get svc tcp-echo-lb -o jsonpath='{.status.loadBalancer.ingress[0].ip}{"\n"}{.status.loadBalancer.ingress[0].hostname}{"\n"}'
```

#### Branche B — CRC / local
```bash
oc port-forward svc/tcp-echo-lb 9000:9000
# dans un second terminal
nc -vz 127.0.0.1 9000
```

## Vérifications

- Service en `type: LoadBalancer`
- selector correct
- test réseau via LB externe ou `port-forward`

## Nettoyage
```bash
oc delete project "$NS"
```
