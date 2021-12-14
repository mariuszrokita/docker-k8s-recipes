# Namespaces
In Kubernetes, namespaces provides a mechanism for isolating groups of resources within a single cluster.

# Demo

Let's start off with building docker image:
```bash
$ docker build -t flask-webapp .
```

Create two namespaces called `development` and `production`:
```
kubectl apply -f namespace-dev.yml
kubectl apply -f namespace-prod.yml
```

We can check if we really created two namespaces by executing the `kubectl get namespace` command. There we can likely see:
```
NAME              STATUS   AGE
default           Active   14d
development       Active   22s
kube-node-lease   Active   14d
kube-public       Active   14d
kube-system       Active   14d
production        Active   17s
```

Now we can deploy our pods to both environments/namespaces:
```
kubectl apply -f pod-1.yml -n development
kubectl apply -f pod-2.yml -n production
```

We can verify both pods are working:
```
NAMESPACE     NAME                               READY   STATUS    RESTARTS      AGE
development   flask-webapp                       1/1     Running   0             45s
...
production    flask-webapp                       0/1     Pending   0             17s
```

Just to double check... By visiting the `localhost:7000` address you can see:
```
Welcome to the restaurant!
Today, a dish of the day is: PIZZA 1
```

And by visiting the `localhost:8000` address you can see:
```
Welcome to the restaurant!
Today, a dish of the day is: PIZZA 2
```


Inspirations:
* https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
* https://alesnosek.com/blog/2017/02/14/accessing-kubernetes-pods-from-outside-of-the-cluster/