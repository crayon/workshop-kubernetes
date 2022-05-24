# Run Pod on Kubernetes
Pods are the smallest deployable units of computing that you can create and manage in Kubernetes. Pod is a group of one or more containers with shared storage, network resources, lifecycle and specification for how to run the containers.

## How to deploy
Creating new objects on Kubernetes cluster means interacting with Kubernetes API using `kubectl` CLI.

In majority of cases, object is deployed using "YAML manifest", which includes all required information for creating an object.

ALL MANIFESTS AND THEIR SPECIFICATIONS CAN BE FOUND ONLINE OR USING `kubectl explain` command, e.g. `kubectl explain pod`.

To deploy, we need to create YAML manifest and then run `kubectl create (or apply) -f <file>`. It is also possible to deploy a Pod without YAML manifest by using `kubectl run <pod_name> <image>`.

## Cleanup
Once you are done, perform cleanup by running `kubectl delete -f ./`
