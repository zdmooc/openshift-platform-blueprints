# D-098 — SQY OpenShift CaaS Reference Architecture

**Status:** REFERENCE / MISSION-ALIGNED  
**Owner:** OpenShift architecture and standards

## Scope

This reference architecture translates the SQY Expert Kubernetes/OpenShift mission into OpenShift-specific
architecture requirements. Runtime lifecycle remains owned by `k8s-openshift-cluster-factory`.

## Platform layers

~~~text
Infrastructure
  compute / network / DNS / LB / firewall / storage / PKI
        |
OpenShift CaaS
  control plane / workers / OVN-Kubernetes / CSI / ingress
        |
Platform controls
  Projects / RBAC / SCC / quotas / NetworkPolicy / OLM
        |
GitOps + shared capabilities
  OpenShift GitOps / IAM / observability / policy / secrets
        |
Specialized workloads
  payments / data / messaging / AI
~~~

## OpenShift standards for D-098

### Projects and tenancy
- dedicated projects/namespaces by ownership and environment;
- owner/environment/criticality labels;
- ResourceQuota + LimitRange;
- least-privilege RoleBindings;
- platform and product ownership separated.

### Workload security
- default target: restricted workload posture;
- SCC choice must be explicit;
- service account per workload class;
- no privilege escalation by default;
- rootless where compatible;
- policy exceptions require owner, reason and expiry.

### Network
- default-deny where operationally appropriate;
- DNS egress explicitly preserved;
- cross-namespace flows documented;
- north-south path separated from east-west service flows;
- F5/BGP integration treated as infrastructure contract, not embedded application logic.

### Exposure
- Route for OpenShift-native HTTP exposure;
- TLS termination strategy explicit;
- admin interfaces separately protected;
- external DNS/LB/firewall dependencies owned outside product namespaces.

### OLM / Operators
- Subscription/channel/version strategy documented;
- automatic vs manual InstallPlan decision explicit;
- CRD compatibility assessed before upgrades;
- Operator ownership and support boundaries recorded.

### Storage
- StorageClass and CSI driver are platform contracts;
- reclaim policy, snapshots and backup are distinct decisions;
- stateful workload recovery must be tested independently.

### GitOps
- Git is desired-state source;
- Argo CD/OpenShift GitOps reconciles approved configuration;
- platform configuration and product workloads remain separated;
- drift, self-heal, prune and rollback are evidence-gated.

### Observability
Minimum platform signals:
- control-plane/operator health;
- node/resource saturation;
- ingress/route errors;
- storage/PVC failures;
- DNS/network failures;
- policy/admission denials;
- GitOps sync health.

## CRC evidence boundary

CRC proves OpenShift API and control behavior on a single local node.
It can validate Projects, Routes, SCC, OLM, Operators, GitOps and policy behavior.

It does not prove:
- production control-plane HA;
- worker failure domains;
- multi-AZ/site resilience;
- production capacity.

## Relationship to Data Lakehouse

The 3-node Kind Data Lakehouse is a workload proof for Kubernetes portability and multi-node scheduling.
It is not moved to CRC solely to make the mission demo look OpenShift-centric.

## Gate

This document contributes to `CAAS_ARCHITECTURE_PACK_READY`.
