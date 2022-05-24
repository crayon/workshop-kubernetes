# Run Ingresses on Kubernetes
API object that manages external access to the service in a cluster. It exposes HTTP and HTTPS routes from outside the cluster to service within the cluster. Traffic is controlled by rules defined within Ingress.
Path types can be Prefix, Exact or ImplementationSpecific.

## How to deploy
Creating new objects on Kubernetes cluster means interacting with Kubernetes API using `kubectl` CLI.

In majority of cases, object is deployed using "YAML manifest", which includes all required information for creating an object.

ALL MANIFESTS AND THEIR SPECIFICATIONS CAN BE FOUND ONLINE OR USING `kubectl explain` command, e.g. `kubectl explain pod`.

To deploy, we need to create YAML manifest and then run `kubectl create (or apply) -f <file>`. It is also possible to create a Cronjob without YAML manifest by using `kubectl create service` (use `--help` flag for all options).

## How to test
Application is now available externaly using hostname provided within Ingress object YAML specification.

## Cleanup
Do not cleanup resources, they will be used in future examples.
