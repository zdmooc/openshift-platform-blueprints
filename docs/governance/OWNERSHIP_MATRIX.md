# OpenShift Portfolio Ownership Matrix

**Date:** 2026-10-01

| Domain | Canonical owner | Blueprints role |
|---|---|---|
| OpenShift architecture and standards | `openshift-platform-blueprints` | **OWNER** |
| Cluster lifecycle / CaaS / Day-2 | `k8s-openshift-cluster-factory` | reference/link |
| Common platform services | `shared-platform-services-openshift` | architecture contract |
| Argo CD / OpenShift GitOps expertise | `argocd-expert-pack` | GitOps architecture reference |
| Keycloak / IAM expertise | `keycloak-enterprise-roadmap-v7` | IAM architecture reference |
| OpenShift migration | `openshift-migration-framework` | migration principles only |
| Kubernetes internals | `kubernetes-the-hard-way-vagrant-architect-v29` | conceptual dependency |
| Multi-cloud KTHW providers | `kubernetes-the-hard-way-multicloud` | conceptual dependency |
| WAS -> OpenShift assessment | `assessment-was-openshift` | modernization reference |
| Data platform | `enterprise-data-lakehouse-kubernetes-openshift` | consumer/specialized platform |
| IBM MQ platform | `mayabank-ibm-mq-native-ha-openshift-eda-platform` | consumer/specialized platform |
| Payments products | payment repositories | consumers |

## Design rule

```text
Architecture standards
        |
        v
Cluster Factory
        |
        v
Shared Platform Services
        |
        v
Specialized Platforms
        |
        v
Business/Data/AI Products
```

This repository owns the **standards and architectural reference**, not every implementation in the stack.
