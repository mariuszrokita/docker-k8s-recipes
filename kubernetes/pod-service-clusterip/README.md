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