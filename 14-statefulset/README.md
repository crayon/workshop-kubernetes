# Run PersistentVolumes and PersistentVolumeClaims on Kubernetes
Used to manage stateful applications. It manages the deployment and scaling of set of Pods and provides guarantees about ordering and uniqueness of these Pods. It maintains sticky identity for each Pod. Each has a persistent identifier that it maintains across any rescheduling. StatefulSet also takes care of creation of volume. Each created PersistentVolume matches single Pod sticky identity.

## How to deploy
Creating new objects on Kubernetes cluster means interacting with Kubernetes API using `kubectl` CLI.

In majority of cases, object is deployed using "YAML manifest", which includes all required information for creating an object.

ALL MANIFESTS AND THEIR SPECIFICATIONS CAN BE FOUND ONLINE OR USING `kubectl explain` command, e.g. `kubectl explain pod`.

To deploy, we need to create YAML manifest and then run `kubectl create (or apply) -f <file>`. It is also possible to create a Cronjob without YAML manifest by using `kubectl create service` (use `--help` flag for all options).

## How to test
Application is now available externaly using hostname provided within Ingress object YAML specification.

## Cleanup
Once you are done, perform cleanup by running `kubectl delete namespace <namespace_name>`
