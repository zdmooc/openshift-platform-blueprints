# Platform Layers Reference Architecture

**Status:** REFERENCE

## Layer model

| Layer | Responsibility | Canonical owner in portfolio |
|---|---|---|
| L0 Infrastructure | compute, network, DNS, LB, firewall, storage, backup, PKI | infrastructure/cloud repositories |
| L1 Execution platform | OpenShift/Kubernetes cluster lifecycle, CNI, CSI, ingress, operators | `k8s-openshift-cluster-factory` |
| L2 Shared platform services | GitOps, identity contracts, observability, quality, policy, secrets | `shared-platform-services-openshift` |
| L3 Shared technical platforms | Kafka, MQ, DB, S3, API/MFT | specialist repositories |
| L4 Specialized platforms | Data, AI, Decision, Integration | specialist repositories |
| L5 Products | business workloads and SLOs | product repositories |

## Architecture rule

A product consumes lower-layer contracts rather than embedding a full private copy of every lower-layer capability.

Exceptions must be explicit:
`DEDICATED_FOR_TEST` when the component itself is under HA, security, recovery or performance test.

## Blueprints responsibility

This repository documents standards across the layers but owns runtime implementation only for small reference examples.
