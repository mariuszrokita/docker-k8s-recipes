# Docker Image Layering

## Non-optimized image
To build an image with non-optimized layering run the following command:
```bash
$ time docker image build -t layering-non-optimized -f non-optimized.Dockerfile .
```

### Statistics
#### Image build time
The summary of the build process may look like:
```
Step 12/12 : CMD ["python", "--version"]
 ---> Running in bfd573ab6647
Removing intermediate container bfd573ab6647
 ---> 9df409dce77a
Successfully built 9df409dce77a
Successfully tagged layering-non-optimized:latest

real    0m52.081s
user    0m0.039s
sys     0m0.154s

```

#### Image size
By running the `docker images` command we can inspect image sizes. There we can see:
```
REPOSITORY                                  TAG           IMAGE ID       CREATED         SIZE
layering-non-optimized                      latest        9df409dce77a   4 minutes ago   429MB
python                                      3.7-slim      3e12d0db6381   46 hours ago    120MB
```

Moreover, by running the `docker history layering-non-optimized` we can inspect all layers. In particular, those created by executing commands from our Dockerfile:
```
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
9df409dce77a   40 seconds ago       /bin/sh -c #(nop)  CMD ["python" "--version"]   0B
269445fae75d   40 seconds ago       |1 DEBIAN_FRONTEND=noninteractive /bin/sh -c…   0B
590a18b3bb46   41 seconds ago       |1 DEBIAN_FRONTEND=noninteractive /bin/sh -c…   0B
7dc3947903d7   42 seconds ago       |1 DEBIAN_FRONTEND=noninteractive /bin/sh -c…   0B
36e2e08ea846   44 seconds ago       |1 DEBIAN_FRONTEND=noninteractive /bin/sh -c…   4.71MB
19be6788232d   47 seconds ago       |1 DEBIAN_FRONTEND=noninteractive /bin/sh -c…   537kB
e724d04116f9   49 seconds ago       |1 DEBIAN_FRONTEND=noninteractive /bin/sh -c…   75B
465730d229f2   50 seconds ago       |1 DEBIAN_FRONTEND=noninteractive /bin/sh -c…   641B
253139c7bb43   53 seconds ago       |1 DEBIAN_FRONTEND=noninteractive /bin/sh -c…   303MB
```

## Optimized image
To build an image with optimized layering run the following command:
```bash
$ time docker image build -t layering-optimized -f optimized.Dockerfile .
```

### Statistics
#### Image build time
The summary of the build process may look like:
```
Step 5/5 : CMD ["python", "--version"]
 ---> Running in 5a718618988b
Removing intermediate container 5a718618988b
 ---> 4849d1d29a4f
Successfully built 4849d1d29a4f
Successfully tagged layering-optimized:latest

real    0m45.420s
user    0m0.043s
sys     0m0.114s

```

#### Image size
By running the `docker images` command we can inspect image sizes. There we can see:
```
REPOSITORY                                  TAG           IMAGE ID       CREATED          SIZE
layering-optimized                          latest        4849d1d29a4f   52 seconds ago   408MB
python                                      3.7-slim      3e12d0db6381   46 hours ago     120MB
```

Moreover, by running the `docker history layering-optimized` we can inspect all layers. In particular, those created by executing commands from our Dockerfile:
```
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
4849d1d29a4f   36 seconds ago       /bin/sh -c #(nop)  CMD ["python" "--version"]   0B
e688fe76f985   37 seconds ago       |1 DEBIAN_FRONTEND=noninteractive /bin/sh -c…   288MB
4392af19d4bd   About a minute ago   /bin/sh -c #(nop)  ARG DEBIAN_FRONTEND=nonin…   0B
a0c800891929   About a minute ago   /bin/sh -c #(nop)  LABEL maintainer=mariusz.…   0B
```

## Conclusions

1. Optimized docker images with smaller number of layers are built faster.
1. Optimized docker images are smaller.
1. Images cannot have more than [42 layers](https://github.com/shykes/docker/pull/50).