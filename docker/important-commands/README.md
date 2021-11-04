# Docker - important commands

A couple of important commands:
1. `docker build -t <image_name:tag> .` - build a docker image and give it a name
1. `docker build -t <image_name:tag> -f <non_standard_dockerfile_name> .` - build a docker image using dockerfile with non-standard name.
1. `docker run <image_name:tag>` - create and start a container
1. `docker run -d <image_name:tag>` - run a container in the background (detached)
1. `docker run -it <image_name:tag>` - interact with the process inside a running container
1. `docker run --rm -it $(docker build -q .)` - build, run container, and remove it immediately
1. `docker logs <container_id>` - display logs for a given container
1. `docker exec -it <container_id> bash` - get inside a running container and launch a shell
1. `docker history <image_name>` - show the history of an image - layers and their sizes
1. `watch -n 5 docker ps` - monitor containers by executing the `docker ps` command every 5 seconds
1. `docker container inspect <container_id>` - display detailed information on container