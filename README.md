## Docker Explanation

## 1. What is Docker?
    Containerization Platform: Docker is a platform that allows developers to package applications and their dependencies into isolated environments called containers...

    Lightweight Virtualization: Docker containers are much lighter than traditional virtual machines because they share the host OS’s kernel...

    Portable Application Packaging: Docker allows developers to bundle their application, along with all necessary libraries...


## 2. Why We Use Docker?
    Portability: Docker containers package the application with all its dependencies, libraries, and environment settings...

    Efficiency: Unlike traditional virtual machines that require a full OS, Docker containers share the host OS’s kernel...

    Fast Deployment: Docker enables rapid application deployment by packaging code and its environment together...
   
    Isolation:Each Docker container runs in its own isolated environment with its own file system, network, and process space. This ensures that applications won’t interfere with each other, providing security and stability, especially when multiple apps run on the same host.

    Scalability:Docker integrates well with container orchestration tools like Kubernetes, making it easy to scale applications horizontally. You can quickly spin up multiple replicas of containers to handle increased traffic or workload, enabling seamless scaling

    Consistency:Docker eliminates the "works on my machine" problem by bundling the app and its dependencies into a single image. This ensures that the application behaves the same across all environments (development, testing, and production)







## Docker-installation

```
https://docs.docker.com/engine/install/
```

follow the official Docker document


## Docker-Hub

```
docker login -u [username]
```

Login into Docker

```
docker push [username]/[image_name]
```

Publish an image to Docker Hub

```
docker search [image_name]
```

Search Hub for an image

```
docker pull [image_name]
```

Pull an image from a Docker Hub

```
docker --help
```

Get help with Docker. Can also use –help on all subcommands

```
docker info
```

Display system-wide information



## Basic Commands

```
docker ps
```

List running containers

```
docker ps --all
```

List all docker containers (running and stopped)

```
docker build -t [image_name]
```

Build an Image from a Dockerfile

```
docker build -t <image_name> . --no-cache
```

Build an image from a Dockerfile without the cache

```
docker build --tag myimage:01 .
```

Build an image from Dockerfile in the current directory (first tag)

```
docker images
```

List local images

```
docker start|stop [container_name] or [container-id]
```

Start or stop an existing container

```
docker rmi [image_name]
```

Delete an Image

```
docker restart [container_name]
```

Restart a container

```
docker rm <container_name>
```

Remove a stopped container

```
docker kill <container_name>
```

Kill the container

```
docker rm -f <container_name>
```

Destroy the container

```
docker pause <container_name>
```

Suspend a container

```
docker unpause <container_name>
```

Resume a container

```
docker image prune
```

Remove all unused images

```
docker rmi $(docker images -q -f "dangling=true")
```

Remove dangling images

```
docker run -d <image_name>
```

Run a container in the background

```
docker exec -it <container_name> sh
```

Open a shell inside a running container

```
docker run -it ubuntu bash
```

Run a container from the Ubuntu image and open a bash shell inside it

```
docker run -p <host_port>:<container_port> -d <image_name>
```

Run a container and publish a container’s port(s) to the host

```
docker run --name <container_name> <image_name>
```

Create and run a container from an image with a custom name

```
docker -d
```

Start the Docker daemon

```
docker history <image_name>
```

View the history of an image, showing layers and commands used to build it

```
docker save -o my_redis_image.tar redis
```

Save an image to a tar file

```
docker load -i my_redis_image.tar
```

Load an image from a tar file

```
docker network ls
```

List all Docker networks

```
docker run \
```

```
docker run \
```

— Starts the Docker run command.

```
--name my-container \
```

— Sets the container name to my-container.

```
--network my-network \
```

— Connects the container to the my-network network.

```
-d \
```

— Runs the container in detached mode (in the background).

```
-p 8080:80 \
```

— Maps port 8080 on the host to port 80 on the container.

```
-e MYSQL_ROOT_PASSWORD=rootpassword \
```

— Sets the environment variable MYSQL_ROOT_PASSWORD with the value rootpassword.

```
-e MYSQL_DATABASE=mydb \
```

— Sets another environment variable MYSQL_DATABASE with the value mydb.

```
-v /my/local/data:/var/lib/mysql \
```

— Mounts a volume from the host (/my/local/data) to the container (/var/lib/mysql).

```
--restart always \
```

— Configures the container to always restart if it stops.

```
mysql:5.7
```

— Specifies the Docker image and version to run (mysql:5.7).


## Inspect Container

```
docker logs -f <container_name>
```

Fetch and follow the logs of a container (live logs)

```
docker port <container_id>
```

Show exposed ports of a container

```
docker inspect <container_name>
```

Inspect a running container

```
docker container stats
```

View resource usage stats

```
docker system df
```

Check Docker daemon disk space usage

```
docker system prune -af
```

Remove images, networks, containers, and volumes

```
docker diff <container_name>
```

Show differences with the images (modified files)

```
docker top <container_name>
```

List the processes running on the container


## Docker Volumes

```
docker volume ls
```

List volumes

```
docker volume create --name <volume_name>
```

Create a local volume

```
docker volume inspect my_volume
```

Inspect a volume for detailed information

```
docker run -v <volume_name>:/data <image-name>
```

Mount a volume on container start (e.g., docker run -v /host/path:/container/path nginx)

```
docker run -d --name my_container -v my_volume:/data nginx
```

Use a volume when running a container

```
docker run -d --name my_container -v /my/local/path:/data nginx
```

Mount a volume at a specific path

```
docker volume rm <volume_name>
```

Destroy a volume

```
docker run -d --name my_container -v my_volume:/data -v /my/local/path:/config nginx
```

Run a container with multiple volumes


## Docker copy-commands

```
docker cp <source-path-on-host> <container-name-or-id>:<destination-path-in-container>
```

Copy from Host to Container (e.g., docker cp /path/on/host/file.txt my_container:/path/in/container/)

```
docker cp <container-name-or-id>:<source-path-in-container> <destination-path-on-host>
```

Copy from Container to Host (e.g., docker cp my_container:/path/in/container/file.txt /path/on/host/)

```
docker cp /path/on/host/my_directory my_container:/path/in/container/
```

Copy a directory from Host to Container

```
docker cp my_container:/path/in/container/my_directory /path/on/host/
```

Copy a directory from Container to Host


## Docker Export Commands

```
docker export -o container_backup.tar my_container
```

The docker export command is used to export the filesystem of a container as a tarball (archive) without the image layers or history. It creates a snapshot of the container's filesystem at the current state.

```
docker export my_container > container_backup.tar
```

Export the filesystem and view it directly or pipe it to another command.


## Docker Network

```
docker network ls
```

List All Docker Networks

```
docker network create <network_name>
```

Create a local network

```
docker run -d --net <network_name> <image-name>
```

Attach a container to a network on start

```
docker run -d --name my-app --network my-network nginx
```

Create a container and attach it to a specific network

```
docker network connect <network_name> <container_id>
```

Connect a running container to a network

```
docker network connect my-network1 my-container
```

Attach multiple networks to a container

```
docker network create --subnet=172.18.0.0/16 my-static-network
```

This command creates a network with a specific subnet (my-static-network) and runs a container with a static IP address (172.18.0.10) on that network.

```
docker network disconnect <network_name> <container_id>
```

Disconnect a container from a network

```
docker network disconnect -f my-network $(docker ps -q)
```

Disconnect all containers from a network

```
docker inspect -f '{{ .NetworkSettings.IPAddress }}' <container_id>
```

Query a specific metadata of a running container

```
docker network inspect my_network
```

Disconnect a container from a network

```
docker network rm my_network
```

Remove a network


## How to make Dockerfile

Information: A Dockerfile is a text document that contains a series of instructions on how to build a Docker image. Docker reads the Dockerfile to create an image with the environment and configuration you need for your applications.

```
FROM image
```

```
LABEL (Metadata)
```

```
COPY path dst
```

```
ADD path dst
```

```
RUN args
```

```
USER name
```

```
WORKDIR path
```

```
CMD args
```

```
EXPOSE xxxx:xxxx
```

```
VOLUME mp
```


## Dockerfile Example

```
FROM node:14
```

1. Dockerfile for a Node.js Application

```
FROM python:3.9-slim
```

2. Dockerfile for a Python Flask Application

```
FROM openjdk:11-jdk-slim
```

3. Dockerfile for a Java Spring Boot Application

```
FROM nginx:alpine
```

4. Dockerfile for an Nginx-based Static Website

```
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
```

5. Dockerfile for a .NET Core Application

```
FROM php:7.4-apache
```

6. Dockerfile for a PHP and Apache Application

```
FROM ruby:2.7
```

7. Dockerfile for a Ruby on Rails Application

```
FROM node:16 AS build
```

8. Dockerfile for a React.js Frontend Application


## Advanced Examples of Dockerfiles

```
FROM node:16 AS builder
```

1. Dockerfile for Production-Ready Node.js Application

```
FROM python:3.9-slim AS base
```

2. Dockerfile for a Microservice (Python Flask + Gunicorn)

```
FROM maven:3.8.4-openjdk-11 AS build
```

3. Dockerfile for a Java Spring Boot Microservice with Multi-Stage Build

```
FROM node:16-alpine AS builder
```

4. Dockerfile for a CI/CD Pipeline (Node.js + Alpine + Docker)


