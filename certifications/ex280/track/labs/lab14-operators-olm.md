# Lab14 — Operators & OLM

## Objectif

Pratiquer :

- exploration des Operators ;
- OperatorGroup ;
- Subscription ;
- CSV ;
- désinstallation propre.

## Pré-requis

- droits suffisants
- OperatorHub / OLM actifs

```bash
export LAB=14
export NS=ex280-lab${LAB}-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

## Tâches

### 1) Lister les Operators
```bash
oc get packagemanifests -n openshift-marketplace | head
```

### 2) Choisir un Operator
Noter :
- package ;
- channel ;
- source.

### 3) OperatorGroup
```bash
cat <<'YAML' | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: ex280-operatorgroup
  namespace: ex280-lab14-zidane
spec:
  targetNamespaces:
  - ex280-lab14-zidane
YAML

oc get operatorgroup -n "$NS"
```

### 4) Subscription
```bash
cat <<'YAML' | oc apply -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: ex280-operator-sub
  namespace: ex280-lab14-zidane
spec:
  channel: "<CHANNEL>"
  name: "<PACKAGE_NAME>"
  source: "<CATALOG_SOURCE>"
  sourceNamespace: "openshift-marketplace"
YAML
```

### 5) Vérifier
```bash
oc get subscription -n "$NS"
oc get csv -n "$NS"
oc describe subscription ex280-operator-sub -n "$NS" | sed -n '1,220p'
```

## Vérifications

- CSV `Succeeded` si installation correcte
- pods de l’Operator présents si applicable

## Nettoyage
```bash
oc delete project "$NS"
```
