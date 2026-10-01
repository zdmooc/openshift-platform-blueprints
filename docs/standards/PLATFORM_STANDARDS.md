# OpenShift Platform Standards

**Status:** REFERENCE

## Namespace / project

- one clear workload or team ownership model;
- standard labels for owner, environment and purpose;
- quotas and default limits for shared clusters;
- no default privileged posture.

## Workload resources

- requests defined for production-like workloads;
- limits used with workload-aware sizing;
- readiness and liveness probes where meaningful;
- startup probes for slow-starting services;
- PDB for replicated services when voluntary disruptions matter;
- HPA only when the workload and metric semantics support horizontal scaling.

## Security

- least privilege RBAC;
- OpenShift SCC / Kubernetes Pod Security considered explicitly;
- default-deny NetworkPolicy pattern where application flows are understood;
- credentials never committed as real secrets;
- identity integrated through OIDC/OAuth2 contracts when applicable.

## Networking

- service-to-service flows documented;
- Routes/Ingress terminate or pass TLS according to explicit architecture;
- egress requirements declared rather than silently unrestricted in enterprise targets.

## GitOps

- Git is desired-state source for standardized platform configuration;
- changes pass review and validation;
- Argo CD ownership is separated from product source repositories;
- drift/self-heal policies are deliberate.

## Observability

- standard metrics/logs/traces interfaces;
- ServiceMonitor or equivalent integration contract;
- SLO/KPI ownership remains with the relevant platform/product;
- telemetry is emitted once and routed to approved backends.

## Stateful workloads

- operator-managed patterns preferred where lifecycle complexity warrants it;
- backup and restore designed separately from persistence;
- HA claims require runtime failure evidence.

## Truth rule

These standards are architecture guidance. Runtime compliance must be proven by the owning implementation repository.
