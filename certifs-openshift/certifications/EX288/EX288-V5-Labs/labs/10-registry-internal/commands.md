# Commandes type — registry interne

```bash
REGISTRY=$(oc registry info)
TOKEN=$(oc whoami -t)

echo $TOKEN | podman login --username $(oc whoami) --password-stdin $REGISTRY
podman build -t $REGISTRY/$(oc project -q)/basic-node:manual ../../shared/apps/basic-node
podman push $REGISTRY/$(oc project -q)/basic-node:manual
oc get is
```
