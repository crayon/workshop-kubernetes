# Run Services on Kubernetes
Provides abstract way to expose application running on a set of Pods as network service. Pods are nonpermanent resources with everchanging IPs. Service is an abstraction which defines a logical set of Pods and a policy by which to access them.
Pods are defined as Service targets by using a selector. 3 types of Services are available – ClusterIP, NodePort and LoadBalancer.

## How to deploy
Creating new objects on Kubernetes cluster means interacting with Kubernetes API using `kubectl` CLI.

In majority of cases, object is deployed using "YAML manifest", which includes all required information for creating an object.

ALL MANIFESTS AND THEIR SPECIFICATIONS CAN BE FOUND ONLINE OR USING `kubectl explain` command, e.g. `kubectl explain pod`.

To deploy, we need to create YAML manifest and then run `kubectl create (or apply) -f <file>`. It is also possible to create a Cronjob without YAML manifest by using `kubectl create service` (use `--help` flag for all options).

## How to test
As we did not cover external access of Kubernetes yet, we can use following command to allow connectivity toward service: `kubectl port-forward service/<service_name> <local_port>:<service_port>`. This command allows specific pod port to be available on local machine. To test application just run following command after: `curl localhost:<local_port>/<random_string>`.

## Cleanup
Do not cleanup resources, they will be used in future examples.
