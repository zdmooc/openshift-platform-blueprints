# Lab00 — Env Bootstrap CRC

## Objectif

Valider un point de départ propre :

- CRC démarré ;
- `oc` connecté ;
- cluster lisible ;
- projet de test + pod de test ;
- dépôt Git accessible.

## Pré-requis

- Windows 11 / Git Bash
- CRC installé
- `oc` disponible
- dépôt cloné localement

## Steps

### 1) Vérifier / démarrer CRC
```bash
crc status
# si nécessaire
crc start
crc status
```

### 2) Connexion `oc`
```bash
crc console --credentials
oc login -u kubeadmin -p '<KUBEADMIN_PWD>' https://api.crc.testing:6443
```

### 3) Vérifier le cluster
```bash
oc whoami
oc whoami --show-context
oc get nodes -o wide
oc get co
```

### 4) Vérifier le workspace Git
```bash
cd /c/workspaces/openshift2026
ls
cd rh-openshift-architect-lab
pwd
git status
```

### 5) Projet et pod de test
```bash
oc get project ex280-lab00-zidane || oc new-project ex280-lab00-zidane
oc project ex280-lab00-zidane

oc delete pod lab00-test --ignore-not-found
oc run lab00-test --image=registry.access.redhat.com/ubi9/ubi-minimal --restart=Never -- sleep 300
oc get pods -o wide
```

## Vérifications

```bash
oc whoami
oc get nodes -o wide
oc get co
oc project
oc get pods -o wide
```

Critères :

- `oc whoami` retourne un utilisateur valide
- les `ClusterOperator` sont stables
- le projet courant est `ex280-lab00-zidane`
- `lab00-test` est `Running` ou `Completed`

## Cleanup (optionnel)

```bash
oc delete pod lab00-test --ignore-not-found
oc delete project ex280-lab00-zidane --ignore-not-found
```

## Pièges fréquents

- CRC arrêté
- mauvais mot de passe `kubeadmin`
- mauvais contexte `oc`
- cluster non complètement stabilisé après démarrage
