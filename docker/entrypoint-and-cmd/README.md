# ENTRYPOINT and CMD

ENTRYPOINT and CMD enable to specify the default executable for the image and provide default arguments.
Arguments can be overridden by the user.

By executing the command:
```bash
$ docker build -t entrypoint-and-cmd .
$ docker run --rm entrypoint-and-cmd
```
you will execute the application inside a container with the selected default application argument.
In the terminal you should see the `About to move in the right direction` message.

The default argument can be easily overridden. By running the command:
```bash
$ docker run --rm entrypoint-and-cmd left
```
we can change application argument. In that case, the output message should look like `About to move in the left direction`.


Reference:
- https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd