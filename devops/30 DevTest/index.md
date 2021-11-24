# Your first container

After setting up your development environment it's time to spin up your first container. Start out with Docker's [hello world](https://hub.docker.com/_/hello-world) image. It's a great starting point for figuring out whether your installation was successful. Once you've confirmed that your local environment can manage and run containerized applications, do the same for your remote environment.

Need help? Check out [this](https://docker-curriculum.com/) for docker, or [this](https://podman.io/getting-started/) for Podman.

## Your first App

Now that you can manage containers on your machines, let's see if we can make it a bit more interesting. Go find an 'image' of an application that is served over a webserver (a http server for example).

One place you can find images is on [Docker Hub](https://hub.docker.com/search?type=image), but a google search for 'docker image ...' can also net you some good results depending on what image you are looking for. A mail client for example, or even snake can be found!

After settling on an application that suits you, try and get it running on your local machine. Follow the localhost port and see if it works in your browser. Be sure to inspect the container as well! See what the logs look like and you might even want to browse the files inside of the container.

After verifying that the image is functioning correctly in your development environment, it's time to see how it fares on your remote environment. 