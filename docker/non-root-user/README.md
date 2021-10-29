# Running Docker container as a non-root user

## Local development

### Virtual environment
When starting development of your application you would most likely do following:
1. Execute the `pipenv shell` command to spawn a shell in a virtual environment to isolate the development.
1. Execute the `pipenv install <package>` command to install any kind of Python packages.
1. Execute the `pipenv install <package> --dev` command to install development packages.

If you wanted to just recreate your development environment, you would remove your previous environment and then execute the `pipenv sync` or `pipenv sync --dev` command to recreate it from scratch.


### Development
A couple of useful commands to be executed many times during development:
1. `pipenv run pytest` - to run unit tests
1. `pipenv run python ./app` - to run your custom application
1. `pipenv check` - to check for security vulnerabilities in your development

## Container
Execute following to build image, run the container and then remove it immediately:
```bash
$ docker run --rm -it $(docker build -q .)
```

## Observations & Conclusions

By running the containerized app you would see the following logs in your console:
```
Running python application...
CWD: /home/appuser
UID: 999
GID: 999
UserName: appuser
```

However, if creation of non-root user was omitted, you would see:
```
Running python application...
CWD: /
UID: 0
GID: 0
UserName: root
```

When you run an application inside a Docker container, by default it has access to all the root privileges. This may be a major concern in terms of security of the application.


Appendix:
- https://www.tutorialspoint.com/running-docker-container-as-a-non-root-user