#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] Vérification de l'environnement"
command -v oc >/dev/null 2>&1 || { echo "[ERROR] oc introuvable"; exit 1; }
oc whoami >/dev/null 2>&1 || { echo "[ERROR] pas connecté à un cluster"; exit 1; }

echo "[OK] utilisateur : $(oc whoami)"
echo "[OK] projet courant : $(oc project -q 2>/dev/null || echo 'aucun')"

if command -v helm >/dev/null 2>&1; then
  echo "[OK] helm trouvé"
else
  echo "[WARN] helm non trouvé"
fi

echo "[INFO] Vérification terminée"
