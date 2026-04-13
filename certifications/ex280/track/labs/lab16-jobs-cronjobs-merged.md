# Lab16 — Jobs & CronJobs

## Objectif

Pratiquer :

- Job one-shot ;
- suivi d’exécution d’un Job ;
- lecture des pods et des logs ;
- Secret consommé par un Job ;
- ServiceAccount dédiée ;
- CronJob périodique ;
- déclenchement manuel depuis un CronJob ;
- suspension d’un CronJob.

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

### 2) Job one-shot consommant un Secret
```bash
cat <<'YAML' | oc apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: fetch-once
spec:
  backoffLimit: 1
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
            echo "Hello from Job"
            date
            echo "Done"
        env:
        - name: TARGET_URL
          valueFrom:
            secretKeyRef:
              name: job-secret
              key: TARGET_URL
YAML

oc get job fetch-once
oc wait --for=condition=complete job/fetch-once --timeout=120s
oc get jobs
```

### 3) Lire les pods et logs du Job
```bash
oc get pods -l job-name=fetch-once -o wide
JOB_POD=$(oc get pods -l job-name=fetch-once -o jsonpath='{.items[0].metadata.name}')
echo "$JOB_POD"
oc logs "$JOB_POD"
oc describe job fetch-once | sed -n '1,220p'
```

### 4) Créer un CronJob
```bash
cat <<'YAML' | oc apply -f -
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello-cron
spec:
  schedule: "*/1 * * * *"
  concurrencyPolicy: Forbid
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
                echo "Hello from CronJob"
                date
                echo "cron hello"
YAML

oc get cronjob hello-cron -o wide
oc describe cronjob hello-cron | sed -n '1,220p'
```

### 5) Déclencher immédiatement un Job depuis le CronJob
```bash
oc create job --from=cronjob/hello-cron hello-cron-manual
oc wait --for=condition=complete job/hello-cron-manual --timeout=120s
oc get jobs
oc get pods -l job-name=hello-cron-manual -o wide
MANUAL_POD=$(oc get pods -l job-name=hello-cron-manual -o jsonpath='{.items[0].metadata.name}')
echo "$MANUAL_POD"
oc logs "$MANUAL_POD"
```

### 6) Suspendre le CronJob
```bash
oc patch cronjob hello-cron -p '{"spec":{"suspend":true}}'
oc get cronjob hello-cron -o jsonpath='{.spec.suspend}{"\n"}'
```

### 7) Vérifier l’état complet du CronJob
```bash
oc get cronjob hello-cron -o yaml | sed -n '1,220p'
```

## Vérifications

- le `Job` `fetch-once` passe en `Complete` ;
- les logs du pod du Job affichent :
  - l’URL du secret ;
  - le message ;
  - la date ;
- le `CronJob` `hello-cron` existe ;
- le Job manuel `hello-cron-manual` passe en `Complete` ;
- `suspend: true` après patch.

## Nettoyage
```bash
oc delete project "$NS"
```
