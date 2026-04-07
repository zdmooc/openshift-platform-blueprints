#!/usr/bin/env bash
set -euo pipefail
PROJECT="${1:-ex288-reset}"
oc delete project "$PROJECT" --ignore-not-found=true
oc new-project "$PROJECT"
echo "[OK] projet recréé : $PROJECT"
