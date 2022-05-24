# Run Service accounts on Kubernetes
It provides an identity for processes that run in a Pod. Processes in pods can contact k8s API server (just like regular users). They are authenticated using ServiceAccount. If pod does not specify it, default ServiceAccount of Namespace is used.
Credentials are automatically mounted into running Pod using Secret object.

## How to deploy
Creating new objects on Kubernetes cluster means interacting with Kubernetes API using `kubectl` CLI.

In majority of cases, object is deployed using "YAML manifest", which includes all required information for creating an object.

ALL MANIFESTS AND THEIR SPECIFICATIONS CAN BE FOUND ONLINE OR USING `kubectl explain` command, e.g. `kubectl explain pod`.

To deploy, we need to create YAML manifest and then run `kubectl create (or apply) -f <file>`. It is also possible to create a Cronjob without YAML manifest by using `kubectl create service` (use `--help` flag for all options).

## How to test
Application is now available externaly using hostname provided within Ingress object YAML specification.

## Cleanup
Do not cleanup resources, they will be used in future examples.
