# Runbook de dépannage rapide

## 1. Pod en CrashLoopBackOff
- Vérifier la commande / args
- Vérifier les variables d'environnement
- Vérifier le montage ConfigMap / Secret
- Lire les logs du conteneur concerné

## 2. ImagePullBackOff
- Vérifier le tag
- Vérifier le nom ImageStream / image externe
- Vérifier l'authentification registry

## 3. Build en échec
- `oc logs -f build/<build-name>`
- Vérifier source Git, contextDir, Containerfile, scripts S2I
- Vérifier permissions sur les fichiers copiés

## 4. Route OK mais application KO
- Vérifier le Service
- Vérifier le `targetPort`
- Vérifier que le Pod écoute bien sur ce port

## 5. Pipeline Tekton échoue
- Vérifier la TaskRun / PipelineRun
- Vérifier paramètres, workspaces, références aux Tasks

## 6. Forbidden / Unauthorized
- `oc auth can-i`
- Vérifier RoleBinding / ServiceAccount / namespace
