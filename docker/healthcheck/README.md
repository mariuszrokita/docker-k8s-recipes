# Health checks

Open up two terminals.
1. In the first one - run the `watch -n 1 docker ps` command to observe state of running containers.
1. In the second one - use the `docker-compose up --build` command start the containerized application

Initially, the status should look like:
```
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                            PORTS                                      NAMES
a0c0641dcb7e   flask-webapp   "pipenv run python .…"   5 seconds ago   Up 3 seconds (health: starting)   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp  flask-webapp
```

After 10 seconds, the first healthcheck is made. The container status changes to 'healthy':
```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                    PORTS                                       NAMES
a0c0641dcb7e   flask-webapp   "pipenv run python .…"   45 seconds ago   Up 43 seconds (healthy)   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   flask-webapp
```

The healthcheck runs periodically and the container state is still the same: 'healthy'.

We can change it by opening up the web browser and accessing the `http://localhost:5000/start-failing` address. This will change the application, it will start crashing.

Very quickly, the container state will change to 'unhealthy':
```
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS                          PORTS                                       NAMES
a0c0641dcb7e   flask-webapp   "pipenv run python .…"   About a minute ago   Up About a minute (unhealthy)   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   flask-webapp
```

There is a 'restart' option ([link](https://docs.docker.com/compose/compose-file/compose-file-v3/#restart)), but it doesn't restart unhealthy containers :(

Reference:
- https://docs.docker.com/engine/reference/builder/#healthcheck
- https://docs.docker.com/compose/compose-file/compose-file-v3/#healthcheck
- https://scoutapm.com/blog/how-to-use-docker-healthcheck
- https://medium.com/@skywalkerhunter/docker-compose-healthcheck-the-1-minute-trick-the-better-example-3f5c05b92689