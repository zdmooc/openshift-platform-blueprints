# Day-2 and Platform Lifecycle Reference Architecture

**Status:** REFERENCE

## Day-2 domains

- cluster health and capacity;
- upgrades and compatibility;
- node maintenance and drain;
- certificate and identity lifecycle;
- backup/restore;
- storage health;
- network and DNS diagnostics;
- policy drift;
- observability and alerting;
- incident/RCA evidence;
- change and rollback planning.

## Upgrade principle

OpenShift lifecycle must follow supported upgrade paths and explicit prechecks. A generic "rollback" statement is not sufficient: rollback/recovery options depend on the component and platform operation being performed.

## Change gate

Before a platform change:
1. record current state;
2. validate support/compatibility;
3. confirm capacity and failure-domain impact;
4. define success/failure criteria;
5. define recovery path;
6. execute in controlled scope;
7. verify workloads and platform signals;
8. capture evidence.

## Capacity

Capacity reasoning should include:
- allocatable CPU/memory;
- requests/limits and overcommit;
- pod density;
- storage growth;
- control-plane and operator overhead;
- failure reserve / N+1 where applicable.

## Evidence boundary

This repository documents the architecture.
Executable upgrade, health-check and N2/N3 runbooks belong in `k8s-openshift-cluster-factory`.
