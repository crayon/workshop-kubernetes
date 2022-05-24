# Run Daemon sets on Kubernetes
DaemonSet object provides user with capability of deploying running application on every node within K8s cluster. Nodes can be excluded from deployment with `tolerations`.
Example use-case is application that monitors each node within K8s cluster.

## How to deploy
Creating new objects on Kubernetes cluster means interacting with Kubernetes API using `kubectl` CLI.

In majority of cases, object is deployed using "YAML manifest", which includes all required information for creating an object.

ALL MANIFESTS AND THEIR SPECIFICATIONS CAN BE FOUND ONLINE OR USING `kubectl explain` command, e.g. `kubectl explain pod`.

To deploy, we need to create YAML manifest and then run `kubectl create (or apply) -f <file>`. It is also possible to create a Cronjob without YAML manifest by using `kubectl create daemonset` (use `--help` flag for all options).

## How to test
As we did not cover networking part of Kubernetes yet, we can use following command to allow connectivity toward one of the pod: `kubectl port-forward <pod_name> <local_port>:<container_port>`. This command allows specific pod port to be available on local machine. To test application just run following command after: `curl localhost:<local_port>/<random_string>`.

## Cleanup
Once you are done, perform cleanup by running `kubectl delete -f ./`
