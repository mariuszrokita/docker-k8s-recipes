# ConfigMap

A ConfigMap is an API object used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume.

# Demo
Let's start off with building docker image:
```bash
$ docker build -t flask-configmap .
```

## Docker container

The app is displaying a name of a dish of the day in some restaurant. The dish name is pulled from environment variables.
By executing the command:
```bash
$ docker run --rm -p 5000:5000 flask-configmap
```
the environment variable is not provided, and we can see the "Today, a dish of the day is: -" message in the UI.

We can also provide environment variable when starting the container:
```bash
$ docker run --rm -p 5000:5000 -e DISH_NAME="pizza quattro stagioni" flask-configmap
```
In this situation, the UI is presenting the "Today, a dish of the day is: pizza quattro stagioni" message.

## ConfigMap

We can specify environment variables for a container indicating that values are coming from the ConfigMap object.
We can do it in two ways:

```bash
$ kubectl apply -f pod-configmap-1.yaml
$ kubectl delete -f pod-configmap-1.yaml
```

or 

```bash
$ kubectl apply -f pod-configmap-2.yaml
$ kubectl delete -f pod-configmap-2.yaml
```

References:
* https://kubernetes.io/docs/concepts/configuration/configmap/ 
* https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/