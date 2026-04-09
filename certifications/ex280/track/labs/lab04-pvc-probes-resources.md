# Lab04 — PVC, Probes & Resources

## Objectif

Pratiquer :

- PVC ;
- montage dans un Deployment ;
- requests / limits ;
- probes ;
- compréhension du binding.

## Pré-requis

```bash
export LAB=04
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) PVC
```bash
cat <<'YAML' | oc apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: web-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
YAML

oc get pvc
oc describe pvc web-pvc
```

### 2) Deployment avec volume + probes + resources
```bash
cat <<'YAML' | oc apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-pvc
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web-pvc
  template:
    metadata:
      labels:
        app: web-pvc
    spec:
      containers:
      - name: httpd
        image: registry.access.redhat.com/ubi8/httpd-24
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"
        livenessProbe:
          httpGet:
            path: /
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
        volumeMounts:
        - name: web-data
          mountPath: /var/www/html
      volumes:
      - name: web-data
        persistentVolumeClaim:
          claimName: web-pvc
YAML

oc get pods
oc describe pod -l app=web-pvc | sed -n '1,220p'
```

### 3) Vérifier le stockage
```bash
POD=$(oc get pod -l app=web-pvc -o jsonpath='{.items[0].metadata.name}')
oc exec "$POD" -- sh -c 'echo VOLUME_OK > /var/www/html/check.txt && cat /var/www/html/check.txt'
```

## Vérifications

- PVC `Bound`
- pod `Running`
- probes présentes
- ressources visibles

## Nettoyage
```bash
oc delete project "$NS"
```
