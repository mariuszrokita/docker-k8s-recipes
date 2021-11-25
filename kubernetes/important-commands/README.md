# Kubernetes - important commands

A couple of important commands for Minikube:
1. `minikube start` - start your cluster
1. `minikube stop` - stop your cluster
1. `minikube status` - check status of your cluster
1. `minikube ip`

A couple of important commands for the `kubectl` command line tool, which is a primary tool to interact with any Kubernetes cluster:
1. `kubectl get all` - list all resources in the default namespace
1. `kubectl get all --all-namespaces` or `kubectl get all -A` - list all resources in all namespaces
1. `kubectl get nodes` - list all nodes (in a default namespace)
1. `kubectl get pods` - list all pods (in a default namespace)
1. `kubectl get pods -n <namespace_name>` - list all pods in a specific namespace
1. `kubectl describe service <service_name>` - display more detailed info about specific resource (e.g. service)
1. `kubectl apply` - create or update resource
1. `kubectl delete` - remove resource
1. `kubectl logs` - print the logs for a container in a pod or specified resource.
1. `kubectl exec <pod> -it sh` - get inside default container in your pod and launch shell in an interactive mode
1. `kubectl exec <pod> -c <container> -it sh` - useful when pod contains more than 1 container

Utilities:
1. `k9s` - run a terminal based UI to interact with your Kubernetes cluster