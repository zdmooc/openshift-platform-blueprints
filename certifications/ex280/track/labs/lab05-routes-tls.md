# Lab05 — Routes & TLS

## Objectif

Pratiquer :

- route HTTP simple ;
- certificat auto-signé ;
- route edge TLS ;
- lecture de la configuration TLS.

## Pré-requis

- `openssl` disponible

```bash
export LAB=05
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) App + Service
```bash
oc create deployment tls-web --image=registry.access.redhat.com/ubi8/httpd-24 --port=8080
oc expose deployment/tls-web --name=tls-web-svc
```

### 2) Route HTTP
```bash
oc expose svc/tls-web-svc
oc get route
ROUTE_HTTP="http://$(oc get route tls-web-svc -o jsonpath='{.spec.host}')"
curl -k "$ROUTE_HTTP" || true
```

### 3) Certificat
```bash
mkdir -p /tmp/ex280-certs
cd /tmp/ex280-certs

openssl req -x509 -newkey rsa:2048 -keyout tls.key -out tls.crt -days 365 -nodes \
  -subj "/CN=tls-web.apps-crc.testing"

oc project "$NS"
oc create secret tls tls-web-secret --cert=tls.crt --key=tls.key
```

### 4) Route TLS edge
```bash
oc create route edge tls-web-tls --service=tls-web-svc --cert=tls.crt --key=tls.key
oc get route
ROUTE_HTTPS="https://$(oc get route tls-web-tls -o jsonpath='{.spec.host}')"
curl -k "$ROUTE_HTTPS" || true
```

## Vérifications

- route HTTP présente ;
- route TLS présente ;
- `curl -k` fonctionne sur la route TLS.

## Nettoyage
```bash
oc delete project "$NS"
rm -rf /tmp/ex280-certs
```
