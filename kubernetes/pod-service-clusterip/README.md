# ClusterIP

## Intro
A ClusterIP provides network connectivity within your cluster.

## Demo

### Docker Compose
Usually web applications consist of a front app and backend, and front app is calling backend to get some data. We could simulate such thing by running two containers:
```bash
$ docker-compose up --build
```

When opening up the `http://localhost:8080` address in your web browser, you could see something like:
```
Hi there!
Quote of the day: Move your honourable arse!
```
In that case, the exact quote of the day was pulled from the backed.

### Kubernetes
We can also simulate such scenario in Kubernetes. Run the following command to run pods for the frontapp and two backends:
```bash
$ kubectl apply -f k8s-app.yaml
```

When opening up the `http://localhost:8080` address in your web browser, you could see something like:
```
Hi there!
Quote of the day: Move your honourable arse!
```

or

```
Hi there!
Quote of the day: Stop whining and get to work!
```

The content of the web page depends on which backend pod that was randomly selected to handle HTTP request coming from the front app.

Note, internal communication between frontend and backend pods is made possible by the `backend` ClusterIP service. The purpose of this service is to expose `backend` pods (filtering by label!) to other pods in the cluster. If you don't believe, comment out the definition of the ClusterIP service in the yaml file and run the `kubectl apply` command again :)