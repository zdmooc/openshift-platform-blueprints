# Labs — EX370

**Repository track : structured.**  
**ODF runtime proof : requires an adapted OpenShift/storage environment and is not inferred from CRC mono-node.**

## Existing practical path

| Lab | Scope | Assets |
|---|---|---|
| 01 | OpenShift refresh | README + commands |
| 02 | Install ODF internal mode | README, commands, Subscription, StorageCluster sample |
| 03 | File / Block / NFS | deployments, PVC, StorageClass |
| 04 | Registry / Monitoring / LokiStack | configuration examples |
| 05 | Capacity / extensions | PVC expansion, quotas |
| 06 | Snapshots / clones | VolumeSnapshot assets |
| 07 | Object storage / OBC / S3 | OBC and s3cmd config |
| 08 | RBAC / SCC / secrets | role, rolebinding, S3 secret example |
| 09 | Mock exam | scenario |

A lightweight `track/` also contains ODF installation and a stateful DB backup lab.

## Runtime gate

A valid ODF runtime claim requires an environment that can actually satisfy the storage topology and resource requirements. Documentation, YAML and a single-node CRC instance are insufficient to claim production ODF resilience.
