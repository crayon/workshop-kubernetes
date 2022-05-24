# Run Cronjobs on Kubernetes
Jobs represent a template to run Pod once and stop it once process running within Pod is finished.
CronJob represents Job instance with addition of periodically triggering that Job on a given schedule.

## How to deploy
Creating new objects on Kubernetes cluster means interacting with Kubernetes API using `kubectl` CLI.

In majority of cases, object is deployed using "YAML manifest", which includes all required information for creating an object.

ALL MANIFESTS AND THEIR SPECIFICATIONS CAN BE FOUND ONLINE OR USING `kubectl explain` command, e.g. `kubectl explain pod`.

To deploy, we need to create YAML manifest and then run `kubectl create (or apply) -f <file>`. It is also possible to create a Cronjob without YAML manifest by using `kubectl create cronjob` (use `--help` flag for all options).

## Cleanup
Once you are done, perform cleanup by running `kubectl delete -f ./`
