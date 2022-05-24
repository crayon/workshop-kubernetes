# Run Roles and RoleBindings on Kubernetes
They contain rules that represent a set of permissions, which are purely additive (no “deny” option). Role object defines set of permissions within particular namespace, while ClusterRole defines it on cluster level and can be used across namespaces. Permissions on cluster-scoped resources can only be granted with ClusterRole.

Binding grants the permissions defined in a role to user. It holds list of subjects (users, groups, service accounts) and a reference to the role being granted. RoleBinding can reference Role in same namespace or ClusterRole, which permissions will only apply in specified namespace. ClusterRoleBinding can reference only ClusterRole and grants permission across all namespaces.


## How to deploy
Creating new objects on Kubernetes cluster means interacting with Kubernetes API using `kubectl` CLI.

In majority of cases, object is deployed using "YAML manifest", which includes all required information for creating an object.

ALL MANIFESTS AND THEIR SPECIFICATIONS CAN BE FOUND ONLINE OR USING `kubectl explain` command, e.g. `kubectl explain pod`.

To deploy, we need to create YAML manifest and then run `kubectl create (or apply) -f <file>`. It is also possible to create a Cronjob without YAML manifest by using `kubectl create service` (use `--help` flag for all options).

## How to test
Application is now available externaly using hostname provided within Ingress object YAML specification.

## Cleanup
Do not cleanup resources, they will be used in future examples.
