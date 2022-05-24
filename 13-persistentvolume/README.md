# Run PersistentVolumes and PersistentVolumeClaims on Kubernetes
PersistentVolume is a piece of storage in cluster that has been provisioned by user or cluster (using StorageClass). It’s lifecycle is independent from Pods using them. PersistentVolumeClaim is a request for storage from user or running Pod. Claims can request different volume sizes and access modes.

## How to deploy
Creating new objects on Kubernetes cluster means interacting with Kubernetes API using `kubectl` CLI.

In majority of cases, object is deployed using "YAML manifest", which includes all required information for creating an object.

ALL MANIFESTS AND THEIR SPECIFICATIONS CAN BE FOUND ONLINE OR USING `kubectl explain` command, e.g. `kubectl explain pod`.

To deploy, we need to create YAML manifest and then run `kubectl create (or apply) -f <file>`. It is also possible to create a Cronjob without YAML manifest by using `kubectl create service` (use `--help` flag for all options).

## How to test
Application is now available externaly using hostname provided within Ingress object YAML specification.

## Cleanup
Once you are done, perform cleanup by running `kubectl delete -f ./`
