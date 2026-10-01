# Storage Reference Architecture

**Status:** REFERENCE

## Scope

OpenShift storage architecture must separate workload persistence requirements from cluster storage implementation.

## Core concepts

- `StorageClass` expresses a consumable storage service class.
- `PersistentVolumeClaim` expresses workload demand.
- CSI provides the storage integration contract.
- Access mode, topology, latency, throughput, durability and recovery requirements must be explicit.
- Stateful application HA is not equivalent to storage replication.

## Reference patterns

### Stateless workload
Prefer ephemeral filesystem and external durable services. Do not introduce PVCs without a state requirement.

### RWO stateful workload
Use one persistent volume per replica when the application/operator owns data replication.

### RWX shared files
Use only for workloads that genuinely require shared filesystem semantics. Avoid using RWX to preserve legacy coupling by default.

### Object storage
Use S3-compatible contracts for artifacts, evidence, backups and data products when object semantics are appropriate.

## OpenShift Data Foundation

ODF/Ceph is treated here as a reference architecture topic. Detailed learning material remains in the EX370 track.

## Backup / restore

Backup design must define:
- protected objects and data;
- consistency mechanism;
- backup location outside the failure domain;
- restore sequence;
- RPO/RTO target;
- restore evidence.

A PVC alone is not a backup.

## Ownership

Cluster/CSI lifecycle belongs to `k8s-openshift-cluster-factory`.
Shared object/data services belong to `shared-platform-services-openshift` or a specialist platform.
