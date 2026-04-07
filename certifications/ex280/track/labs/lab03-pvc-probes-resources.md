# Lab03 — PVC, Probes & Resources

## Objectif
- Créer un PVC.
- Monter le PVC dans un pod httpd.
- Configurer requests/limits CPU/mémoire.
- Ajouter liveness/readiness probes.

## Pré-requis
- Lab02 OK.

## Steps

### Step 1 — Projet
    oc get project ex280-lab03-pvc-zidane || oc new-project ex280-lab03-pvc-zidane
    oc project ex280-lab03-pvc-zidane

### Step 2 — PVC
    cat << 'YAML' | oc apply -f -
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

### Step 3 — Deployment avec PVC + probes + ressources
    cat << 'YAML' | oc apply -f -
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

## Vérifications
    oc get pvc
    oc get pods
    oc describe pod -l app=web-pvc
    oc logs -l app=web-pvc || true

Critères :
- PVC `Bound`
- Pod `Running`
- Pas de redémarrages répétés (probes OK)

## Cleanup (optionnel)
    oc delete project ex280-lab03-pvc-zidane --ignore-not-found

## Pièges fréquents
- PVC `Pending` → `oc describe pvc web-pvc`
- Probes trop agressives → augmenter `initialDelaySeconds`
