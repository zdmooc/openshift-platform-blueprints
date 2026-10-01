# Dependency Classification

**Date:** 2026-10-01

Every technical dependency referenced by this repository or by a consuming product should be classified before a new local instance is added.

| Classification | Meaning | Example |
|---|---|---|
| `CONSUME_SHARED` | consume an approved shared capability | shared OTel collector, shared GitOps governance |
| `DEDICATED_FOR_TEST` | dedicated because the component itself is under HA/recovery/security/performance test | Kafka HA lab, PostgreSQL PITR lab |
| `SPECIALIZED_PLATFORM` | owned by a specialist platform repository | IBM MQ Native HA, Data Lakehouse |
| `PRODUCT_OWNED` | legitimately part of product runtime and SLO ownership | application schemas, product topics, business API |
| `REFERENCE_ONLY` | documented architecture/pattern, not deployed by this repository | Rancher/RKE2 placement pattern in an architecture view |

## Decision sequence

```text
Need a capability
      |
      v
Existing canonical owner?
      | yes
      v
Consume/link it
      |
      +--> Is the component itself under test?
              | yes -> DEDICATED_FOR_TEST
              | no  -> CONSUME_SHARED / SPECIALIZED_PLATFORM
      |
      no
      v
Can an existing owner reasonably absorb it?
      | yes -> extend existing repository
      | no  -> only then consider a new repository
```

This rule prevents `one POC = one complete technical platform`.
