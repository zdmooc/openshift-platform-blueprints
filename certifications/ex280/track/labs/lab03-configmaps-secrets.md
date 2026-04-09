# Lab03 — ConfigMaps & Secrets

## Objectif

Pratiquer :

- ConfigMap depuis literals et fichier ;
- Secret générique ;
- injection par variables d’environnement ;
- montage en volume ;
- effet d’une mise à jour.

## Pré-requis

```bash
export LAB=03
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) ConfigMap depuis literals
```bash
oc create configmap app-config \
  --from-literal=APP_MODE=dev \
  --from-literal=APP_COLOR=blue
oc get cm app-config -o yaml | sed -n '1,120p'
```

### 2) ConfigMap depuis fichier
```bash
echo "Bonjour EX280" > message.txt
oc create configmap app-message --from-file=message.txt
oc get cm app-message -o yaml | sed -n '1,120p'
```

### 3) Secret
```bash
oc create secret generic app-secret \
  --from-literal=DB_USER=odmuser \
  --from-literal=DB_PASS='devsecops'
oc get secret app-secret -o yaml | sed -n '1,80p'
```

### 4) Pod lisant `envFrom`
```bash
cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: env-printer
spec:
  containers:
  - name: env-printer
    image: registry.access.redhat.com/ubi9/ubi-minimal
    command: ["/bin/sh","-c"]
    args:
      - |
        env | sort
        sleep 3600
    envFrom:
      - configMapRef:
          name: app-config
      - secretRef:
          name: app-secret
YAML
oc wait --for=condition=Ready pod/env-printer --timeout=120s
oc logs env-printer | head -n 60
```

### 5) ConfigMap montée en volume
```bash
cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: cm-volume
spec:
  containers:
  - name: cm-volume
    image: registry.access.redhat.com/ubi9/ubi-minimal
    command: ["/bin/sh","-c"]
    args:
      - |
        cat /etc/config/message.txt
        sleep 3600
    volumeMounts:
      - name: cfg
        mountPath: /etc/config
  volumes:
    - name: cfg
      configMap:
        name: app-message
YAML
oc wait --for=condition=Ready pod/cm-volume --timeout=120s
oc logs cm-volume
```

## Vérifications

- `env-printer` lit ConfigMap et Secret ;
- `cm-volume` lit `message.txt`.

## Nettoyage
```bash
oc delete project "$NS"
rm -f message.txt
```
