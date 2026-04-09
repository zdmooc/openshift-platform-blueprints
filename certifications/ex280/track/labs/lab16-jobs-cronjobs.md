# Lab16 — Jobs & CronJobs

## Objectif

Pratiquer :

- Job one-shot ;
- CronJob périodique ;
- secret consommé par un Job ;
- ServiceAccount dédiée.

## Pré-requis

```bash
export LAB=16
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) Secret et ServiceAccount
```bash
oc create secret generic job-secret --from-literal=TARGET_URL=https://example.org
oc create serviceaccount batch-sa
```

### 2) Job
```bash
cat <<'YAML' | oc apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: fetch-once
spec:
  template:
    spec:
      serviceAccountName: batch-sa
      restartPolicy: Never
      containers:
      - name: fetch
        image: registry.access.redhat.com/ubi9/ubi-minimal
        command: ["/bin/sh","-c"]
        args:
          - |
            echo "URL=$TARGET_URL"
            echo "Done"
        env:
        - name: TARGET_URL
          valueFrom:
            secretKeyRef:
              name: job-secret
              key: TARGET_URL
YAML

oc get job fetch-once -w
oc logs -l job-name=fetch-once
```

### 3) CronJob
```bash
cat <<'YAML' | oc apply -f -
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello-cron
spec:
  schedule: "*/1 * * * *"
  successfulJobsHistoryLimit: 2
  failedJobsHistoryLimit: 2
  jobTemplate:
    spec:
      template:
        spec:
          serviceAccountName: batch-sa
          restartPolicy: Never
          containers:
          - name: hello
            image: registry.access.redhat.com/ubi9/ubi-minimal
            command: ["/bin/sh","-c"]
            args:
              - |
                date
                echo "cron hello"
YAML

oc get cronjob hello-cron -o wide
```

### 4) Suspendre
```bash
oc patch cronjob hello-cron -p '{"spec":{"suspend":true}}'
oc get cronjob hello-cron -o jsonpath='{.spec.suspend}{"\n"}'
```

## Vérifications

- Job `Complete`
- CronJob présent
- `suspend: true` après patch

## Nettoyage
```bash
oc delete project "$NS"
```
