# Health checks

# Intro
Healthchecks, aka liveness check, is a mechanism used to verify whether a container can be considered healthy.

# Few words about the demo

Kubernetes knows how to pull docker images and how to run them. It doesn't know, however, how to build images. We need to build Docker images "in a standard way", then push it to image registry, and finally, we can deploy such image to Kubernetes.

Let's start off with building docker image:
```bash
$ docker build -t flask-webapp .
```

Now we can try to deploy that image to Kubernetes:
```bash
$ kubectl apply -f pod-healthcheck.yaml
```

Unfortunately, there's an error:
```bash
NAME                                READY   STATUS         RESTARTS   AGE
pod/flask-webapp-healthcheck-test   0/1     ErrImagePull   0          18s
```

Why? That's simple. Kubernetes/Minikube uses its own Docker daemon that's not connected to the one on the local machine. All local docker images are not visible to Kubernetes, nor images with such names can be found in the global registry (Docker Hub).

There is a way, however, to reuse the Docker daemon from Minikube to build docker image. All is perfectly described on https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube. In other words, docker images will be built not on the host, but on Minikube VM.

```bash
$ eval $(minikube docker-env)
$ docker build -t flask-webapp .
```

Now we can finally deploy image to Kubernetes:
```bash
$ kubectl apply -f pod-healthcheck.yaml
```

# Liveness Probe

Initially, the pod's status looks like:
```
NAME                            READY   STATUS    RESTARTS   AGE
flask-webapp-healthcheck-test   1/1     Running   0          2m2s
```

The healthcheck (liveness probe) runs periodically and the pod status is still the same: Running.

Let's mess up a bit... Open terminal and type:
```bash
$ minikube docker-env
$ # or
$ minikube ip
```
Take note of the IP address.

We'll modify the application state and it will start crashing. We will do that by opening up the web browser and accessing the `http://<DOCKER_HOST_IP>:5000/start-failing` address.

Very quickly, the healthcheck will detect that the container is 'unhealthy' and the entire pod will be restarted:
```
NAME                            READY   STATUS    RESTARTS      AGE
flask-webapp-healthcheck-test   1/1     Running   1 (77s ago)   11m
```

The pod has been automatically restarted, and the web app is up and running.


References:
* [Creating Docker Image & Deploying it into Kubernetes](https://www.youtube.com/watch?v=z8U2x1TCPis)
* [How to Run Locally Built Docker Images in Kubernetes](https://medium.com/swlh/how-to-run-locally-built-docker-images-in-kubernetes-b28fbc32cc1d)
* [Use local docker images with Minikube](https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube)