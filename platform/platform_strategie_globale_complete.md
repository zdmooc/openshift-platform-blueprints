# Stratégie globale du dépôt `rh-openshift-architect-lab` – Version complète

## 1. Ce qui a été fait (état actuel)

### 1.1. Documentation d’architecture (`docs/`)

- `docs/ARCHITECTURE.md`
  - Vue globale du lab OpenShift (CRC comme cluster unique).
  - Rôle des namespaces, flux utilisateur → route → service → pod → stockage.
- `docs/gitops-platform.md`
  - Modèle GitOps de la plateforme : séparation `cluster-config/` vs `argocd-apps/`.
  - Principe app-of-apps pour la plateforme.
- `docs/observability-sre.md`
  - Concepts SRE : 4 signaux d’or, SLO/SLA.
  - Stack observabilité cible (Prometheus, Alertmanager, logs, Grafana).
- `docs/security-architecture.md`
  - Modèle RBAC (lab-admin, lab-dev, lab-ops).
  - NetworkPolicies (deny-by-default, same-namespace, egress contrôlé).
  - Gestion des secrets, notions de PodSecurity / SCC.
- `docs/multi-cluster.md`
  - Projection multi-cluster avec RHACM/OCM (hub + clusters workload).
  - Concepts : ManagedCluster, ClusterSet, Placement, Policy.
- `docs/portfolio-architect.md`
  - Synthèse pour CV / LinkedIn.
  - Bullets réutilisables pour prouver le niveau Architecte OpenShift.

### 1.2. GitOps plateforme – configuration cluster (`platform/gitops/cluster-config/`)

- `namespaces/namespaces-ex-labs.yaml`
  - Namespaces de lab : `ex280-lab`, `ex288-lab`, `ex370-lab`, `ex380-lab`, `ex480-lab`, `ex482-lab`, `sandbox-lab`.
  - Labels : `env`, `track`, `owner`.

- `quotas/quotas-ex-labs.yaml`
  - Pour chaque namespace de lab :
    - `ResourceQuota` (requests/limits CPU & mémoire, nombre de pods).
    - `LimitRange` (default / defaultRequest / min / max par container).

- `rbac/lab-rbac-ex-labs.yaml`
  - `ClusterRole` :
    - `lab-admin` – droits complets sur les ressources principales.
    - `lab-dev` – droits forts sur les ressources applicatives, lecture logs/events.
    - `lab-ops` – lecture + update/patch sur certains workloads.
  - `RoleBinding` dans chaque namespace de lab vers les groupes :
    - `ocp-lab-admins`, `ocp-lab-devs`, `ocp-lab-ops`.

- `networkpolicies/networkpolicies-ex-labs.yaml`
  - Par namespace de lab :
    - `default-deny-all` – deny all ingress/egress par défaut.
    - `allow-same-namespace` – autorise le trafic intra-namespace.
    - `allow-egress-dns-http` – autorise DNS (vers `openshift-dns`) + HTTP/HTTPS vers Internet.

### 1.3. Observabilité GitOps (`platform/observability/`)

- `servicemonitors/servicemonitor-ex280-demo-metrics.yaml`
  - `ServiceMonitor` dans `ex280-lab` pour un service `demo-metrics` :
    - `selector.matchLabels.app=demo-metrics`.
    - `endpoint` : port `http-metrics`, path `/metrics`, interval `30s`.

### 1.4. Applications Argo CD (`platform/gitops/argocd-apps/`)

- `application-platform-namespaces.yaml`
  - Application `platform-namespaces` (repo `rh-openshift-architect-lab`, path `platform/gitops/cluster-config/namespaces`).
- `application-platform-quotas.yaml`
  - Application `platform-quotas` (path `platform/gitops/cluster-config/quotas`).
- `application-platform-rbac.yaml`
  - Application `platform-rbac` (path `platform/gitops/cluster-config/rbac`).
- `application-platform-network.yaml`
  - Application `platform-network` (path `platform/gitops/cluster-config/networkpolicies`).
- `application-platform-observability.yaml`
  - Application `platform-observability` (path `platform/observability/servicemonitors`).

En résumé : la **plateforme de lab** (namespaces, quotas, RBAC, NetworkPolicy, ServiceMonitor) est entièrement pilotable via Argo CD.

---

## 2. Ce qu’il reste à faire – Roadmap globale

### 2.1. Niveau plateforme

1. Ajouter une **Application Argo CD racine** `platform-root` (pattern app-of-apps) pour regrouper :
   - `platform-namespaces`
   - `platform-quotas`
   - `platform-rbac`
   - `platform-network`
   - `platform-observability`
   - (plus tard) d’autres blocs : dashboards, policies, etc.

2. Ajouter une **application de démo instrumentée** dans `ex280-lab` :
   - `Deployment` + `Service` `demo-metrics` exposant `/metrics`.
   - GitOps pour cette appli (Application Argo CD dédiée).

3. Ajouter plus tard une **intégration dashboards Grafana** :
   - JSON de dashboards dans `platform/observability/dashboards/`.
   - Intégration dépendante de la stack Grafana (operator, kube-prometheus-stack, etc.).

### 2.2. Niveau multi-cluster / conformité (plus tard)

1. Dans `ex480-multicluster/` :
   - Exemples de policies RHACM (GRC), placements, apps multi-cluster.
2. Ajout éventuel d’un volet **policies de conformité** (Kyverno / Gatekeeper) :
   - aligné avec ce qui est déjà modélisé (quotas, limits, NetworkPolicy, images, etc.).

---

## 3. Artefacts supplémentaires proposés

Les sections ci-dessous contiennent tout le YAML suggéré pour couvrir ce qui manque encore côté GitOps plateforme (niveau lab), à copier dans les chemins indiqués.

### 3.1. Application Argo CD racine `platform-root`

_Fichier suggéré_ : `platform/gitops/argocd-apps/application-platform-root.yaml`

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: platform-root
  namespace: openshift-gitops
spec:
  project: default
  source:
    repoURL: https://github.com/zdmooc/rh-openshift-architect-lab.git
    targetRevision: main
    # On pointe sur le dossier qui contient les CRD Application enfant
    path: platform/gitops/argocd-apps
  destination:
    server: https://kubernetes.default.svc
    namespace: openshift-gitops
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

Usage :

- Cette Application va gérer les autres Applications `platform-*` comme ressources K8s.
- Dans la pratique, tu pourras soit :
  - appliquer directement tous les `application-platform-*.yaml` à la main,
  - ou n’appliquer que `application-platform-root.yaml` et laisser Argo déployer les autres.

---

### 3.2. Application de démo instrumentée dans `ex280-lab`

Objectif : disposer d’une petite appli qui :

- tourne dans `ex280-lab`,
- expose un endpoint `/metrics` compatible Prometheus,
- est supervisée par le `ServiceMonitor` déjà en place.

On utilise l’image **`quay.io/brancz/prometheus-example-app`** qui expose nativement des métriques Prometheus.

#### 3.2.1. Manifests de l’app `demo-metrics`

_Fichier suggéré_ : `apps/ex280/demo-metrics/deployment-service.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-metrics
  namespace: ex280-lab
  labels:
    app: demo-metrics
spec:
  replicas: 1
  selector:
    matchLabels:
      app: demo-metrics
  template:
    metadata:
      labels:
        app: demo-metrics
    spec:
      containers:
        - name: demo-metrics
          image: quay.io/brancz/prometheus-example-app:v0.5.0
          imagePullPolicy: IfNotPresent
          ports:
            - name: http-metrics
              containerPort: 8080
          readinessProbe:
            httpGet:
              path: /
              port: http-metrics
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /
              port: http-metrics
            initialDelaySeconds: 15
            periodSeconds: 20
---
apiVersion: v1
kind: Service
metadata:
  name: demo-metrics
  namespace: ex280-lab
  labels:
    app: demo-metrics
spec:
  selector:
    app: demo-metrics
  ports:
    - name: http-metrics
      port: 8080
      targetPort: http-metrics
      protocol: TCP
```

Remarques :

- Le label `app: demo-metrics` et le port nommé `http-metrics` correspondent exactement au `ServiceMonitor` que tu as déjà créé.
- Le namespace `ex280-lab` est géré par GitOps via `platform-namespaces`.

#### 3.2.2. Application Argo CD pour `demo-metrics`

_Fichier suggéré_ : `platform/gitops/argocd-apps/application-ex280-demo-metrics.yaml`

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: ex280-demo-metrics
  namespace: openshift-gitops
spec:
  project: default
  source:
    repoURL: https://github.com/zdmooc/rh-openshift-architect-lab.git
    targetRevision: main
    path: apps/ex280/demo-metrics
  destination:
    server: https://kubernetes.default.svc
    namespace: ex280-lab
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

Usage :

- Tu crées le dossier `apps/ex280/demo-metrics/` et tu ajoutes `deployment-service.yaml` dedans.
- Tu appliques ensuite `application-ex280-demo-metrics.yaml` dans `openshift-gitops`.
- Argo CD déploiera la charge de travail dans `ex280-lab`. Le `ServiceMonitor` existant commencera à scraper `/metrics`.

---

## 4. Commandes récapitulatives (Git côté repo)

Quand tu intégreras ces nouveaux fichiers dans ton dépôt :

```bash
cd /c/workspaces/openshift2026/rh-openshift-architect-lab

# App-of-apps plateforme
mkdir -p platform/gitops/argocd-apps
# (coller le YAML dans platform/gitops/argocd-apps/application-platform-root.yaml)

# App demo-metrics
mkdir -p apps/ex280/demo-metrics
# (coller le YAML dans apps/ex280/demo-metrics/deployment-service.yaml)
# (coller l’Application Argo dans platform/gitops/argocd-apps/application-ex280-demo-metrics.yaml)

git status

git add \
  platform/gitops/argocd-apps/application-platform-root.yaml \
  apps/ex280/demo-metrics/deployment-service.yaml \
  platform/gitops/argocd-apps/application-ex280-demo-metrics.yaml

git commit -m "Add platform root app and ex280 demo-metrics app with GitOps"

git push origin main

git status
```

---

## 5. Commandes récapitulatives (activation côté cluster)

Sur ton cluster OpenShift (CRC ou autre), une fois Argo CD installé :

```bash
oc whoami
oc get nodes

oc project openshift-gitops

# Applications plateforme (si pas déjà appliquées)
oc apply -f platform/gitops/argocd-apps/application-platform-namespaces.yaml
oc apply -f platform/gitops/argocd-apps/application-platform-quotas.yaml
oc apply -f platform/gitops/argocd-apps/application-platform-rbac.yaml
oc apply -f platform/gitops/argocd-apps/application-platform-network.yaml
oc apply -f platform/gitops/argocd-apps/application-platform-observability.yaml

# Application racine (optionnel, si tu veux l’app-of-apps)
oc apply -f platform/gitops/argocd-apps/application-platform-root.yaml

# Application demo-metrics\ noc apply -f platform/gitops/argocd-apps/application-ex280-demo-metrics.yaml

# Vérification\ noc get applications.argoproj.io -n openshift-gitops
```

Ce document réunit :

- le **récapitulatif complet** de ce qui est déjà en place,
- la **roadmap** de ce qui restait à faire au niveau GitOps plateforme,
- et les **artefacts manquants** (Application racine, app demo-metrics + Application Argo associée) dans un seul endroit, prêt à être copié dans ton dépôt ou adapté selon tes besoins.

