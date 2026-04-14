# 02D — ImageStream consumption by DeploymentConfig

## Objectif
Consommer un ImageStreamTag dans un DeploymentConfig.

## Commandes
```bash

oc new-project ex288-02d || oc project ex288-02d

cat <<'EOF' | oc apply -f -
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: demo
---
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: demo
spec:
  replicas: 1
  selector:
    app: demo
  template:
    metadata:
      labels:
        app: demo
    spec:
      containers:
        - name: app
          image: image-registry.openshift-image-registry.svc:5000/ex288-02d/demo:latest
          ports:
            - containerPort: 8080
  triggers:
    - type: ConfigChange
    - type: ImageChange
      imageChangeParams:
        automatic: true
        containerNames: [app]
        from:
          kind: ImageStreamTag
          name: demo:latest
EOF

oc describe dc demo
oc get is

```

## Vérifications
- lien DC -> ImageStream visible
