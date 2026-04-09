# Lab08 — HTPasswd, Users, Groups & RBAC

## Objectif

Pratiquer :

- HTPasswd IdP (si environnement adapté) ;
- création de groupes ;
- binding RBAC ;
- vérification de permissions.

## Pré-requis

- droits cluster-admin
- outil `htpasswd` si tu fais la partie IdP
- CRC recommandé pour la partie IdP

## Partie A — RBAC projet

```bash
export LAB=08
export NS=ex280-lab${LAB}-rbac-zidane
oc get project "$NS" || oc new-project "$NS"
oc project "$NS"
```

### 1) Groupe logique
```bash
oc adm groups new ex280-devs zidane-dev1 zidane-dev2 || true
oc get groups
oc describe group ex280-devs
```

### 2) Lier le rôle `edit`
```bash
oc policy add-role-to-group edit ex280-devs -n "$NS"
oc get rolebindings -n "$NS"
```

### 3) Vérifier
```bash
oc auth can-i get pods --as=zidane-dev1 -n "$NS" || true
oc auth can-i create deployment --as=zidane-dev1 -n "$NS" || true
oc auth can-i delete project --as=zidane-dev1 -n "$NS" || true
```

## Partie B — HTPasswd (option CRC avancée)

### 4) Fichier local
```bash
htpasswd -c -B -b htpasswd.users ex280-user1 Passw0rd!
htpasswd -B -b htpasswd.users ex280-user2 Passw0rd!
```

### 5) Secret
```bash
oc create secret generic htpass-secret \
  --from-file=htpasswd=htpasswd.users \
  -n openshift-config --dry-run=client -o yaml | oc apply -f -
oc get secret htpass-secret -n openshift-config
```

### 6) OAuth cluster
```bash
cat <<'YAML' | oc apply -f -
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: htpasswd
    mappingMethod: claim
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret
YAML
```

## Vérifications

- groupe `ex280-devs`
- rolebinding présent
- partie HTPasswd visible dans `oauth/cluster` si appliquée

## Nettoyage
```bash
oc delete project "$NS" --ignore-not-found
rm -f htpasswd.users
```
