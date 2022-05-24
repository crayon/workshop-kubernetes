# Build Container Image
This excercise focuses on basics on container image building.

## Building of an Image
Multiple container engines are available, which support building container image. Engine that is used by most people is Docker. This tutorial will use `docker` CLI for examples.

Container image that will be built is a simple image, which will print "Hello World" to output using Python script added to image (`hello-world.py`)

Let's check instructions on how to build container image, which are available in `Dockerfile`:
* first we specify base image with `FROM` command
* after that we define default path where we will be working within container using `WORKDIR` command
* we add `hello-world.py` script to image using `ADD` command
* with `RUN` command we change permissions on newly added script file
* in last step we define what should happen when container image is run using `ENTRYPOINT` command

With `Dockerfile` in place, we can build our first image by running `docker build -t <image_name>:<image_tag> .` command.

Once build process is complete, you can test your image by running `docker run -e HELLO_USER=<your_name> <image_name>:<image_tag>`.


## Publishing an Image
With image built, we want to store it in container repository, so that it will be available to be fetch outside of our local environment. For this, we need to make sure that container registry name is part if image name. Following example represents image "Hello World" in "bostjanbozic" registry on Azure: `bostjanbozic.azurecr.io/hello-world:0.0.1`.

Before pushing image to registry, we need to rename the image. This can be done using following command: `docker tag <image_name>:<image_tag> <repository_name>/<image_name>:<image_tag>`.

Once this is done, there is one step that we still have to do before pushing an image - logging into container image registry. This is done using command `docker login <repository_name>` and entering credentials.

Once we are logged it, last thing that we still have to do it push an image. This is performed simply by writing following command: `docker push <repository_name>/<image_name>:<image_tag>`.
