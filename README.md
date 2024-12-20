###  What is Docker?

Containerization Platform: Docker is a platform that allows developers to package applications and their dependencies into isolated environments called containers...

Lightweight Virtualization: Docker containers are much lighter than traditional virtual machines because they share the host OS’s kernel...

Portable Application Packaging: Docker allows developers to bundle their application, along with all necessary libraries...

<br/><br/>
### Why We Use Docker?

Portability: Docker containers package the application with all its dependencies, libraries, and environment settings...

Efficiency: Unlike traditional virtual machines that require a full OS, Docker containers share the host OS’s kernel...

Fast Deployment: Docker enables rapid application deployment by packaging code and its environment together...

Isolation: Each Docker container runs in its own isolated environment with its own file system, network, and process space. This ensures that applications won’t interfere with each other, providing security and stability, especially when multiple apps run on the same host.

Scalability: Docker integrates well with container orchestration tools like Kubernetes, making it easy to scale applications horizontally. You can quickly spin up multiple replicas of containers to handle increased traffic or workload, enabling seamless scaling.

Consistency: Docker eliminates the "works on my machine" problem by bundling the app and its dependencies into a single image. This ensures that the application behaves the same across all environments (development, testing, and production).


<br/><br/>
### Docker installation
`https://docs.docker.com/engine/install/`

#### follow the official Docker document


<br/><br/>
### Basic commands 
`docker login -u [username]`

Login into Docker<br/><br/>

`docker push [username]/[image_name]`

Publish an image to Docker Hub<br/><br/>

`docker search [image_name]`

Search Hub for an image<br/><br/>

`docker pull [image_name]`

Pull an image from a Docker Hub<br/><br/>

`docker --help`

Get help with Docker. Can also use –help on all subcommands<br/><br/>

`docker info`

Display system-wide information<br/><br/>

`docker ps`

List running containers<br/><br/>

`docker ps --all`

List all docker containers (running and stopped)<br/><br/>

`docker build -t [image_name]`

Build an Image from a Dockerfile<br/><br/>

`docker build -t <image_name> . --no-cache`

Build an image from a Dockerfile without the cache<br/><br/>

`docker build --tag myimage:01 .`

Build an image from Dockerfile in the current directory (first tag)<br/><br/>

`docker images`

List local images<br/><br/>

`docker start|stop [container_name] or [container-id]`

Start or stop an existing container<br/><br/>

`docker rmi [image_name]`

Delete an Image<br/><br/>

`docker restart [container_name]`

Restart a container<br/><br/>

`docker rm <container_name>`

Remove a stopped container<br/><br/>

`docker kill <container_name>`

Kill the container<br/><br/>

`docker rm -f <container_name>`

Destroy the container<br/><br/>

`docker pause <container_name>`

Suspend a container<br/><br/>

`docker unpause <container_name>`

Resume a container<br/><br/>

`docker image prune`

Remove all unused images<br/><br/>

`docker rmi $(docker images -q -f "dangling=true")`

Remove dangling images<br/><br/>

`docker run -d <image_name>`

Run a container in the background<br/><br/>

`docker exec -it <container_name> sh`

Open a shell inside a running container<br/><br/>

`docker run -it ubuntu bash`

Run a container from the Ubuntu image and open a bash shell inside it<br/><br/>

`docker run -p <host_port>:<container_port> -d <image_name>`

Run a container and publish a container’s port(s) to the host<br/><br/>

`docker run --name <container_name> <image_name>`

Create and run a container from an image with a custom name<br/><br/>

`docker -d`

Start the Docker daemon<br/><br/>

`docker history <image_name>`

View the history of an image, showing layers and commands used to build it<br/><br/>

`docker save -o my_redis_image.tar redis`<br/><br/>

Save an image to a tar file<br/><br/>

`docker load -i my_redis_image.tar`

Load an image from a tar file<br/><br/>

`docker network ls`

List all Docker networks<br/><br/>


<br/><br/>
#### Docker Multiple line command

`docker run \`

`--name my-container \`

`--network my-network \`

`-d \`

`-p 8080:80 \`

`-e MYSQL_ROOT_PASSWORD=rootpassword \`

`-e MYSQL_DATABASE=mydb \`

`-v /my/local/data:/var/lib/mysql \`

`--restart always \`

`mysql:5.7`

<br/><br/>
#### Explanation below here

`docker run \`

Starts the Docker run command.<br/><br/>

`--name my-container \`

Sets the container name to my-container.<br/><br/>

`--network my-network \`

Connects the container to the my-network network.<br/><br/>

`-d \`

Runs the container in detached mode (in the background).<br/><br/>

`-p 8080:80 \`

Maps port 8080 on the host to port 80 on the container.<br/><br/>

`-e MYSQL_ROOT_PASSWORD=rootpassword \`

Sets the environment variable MYSQL_ROOT_PASSWORD with the value rootpassword.<br/><br/>

`-e MYSQL_DATABASE=mydb \`

Sets another environment variable MYSQL_DATABASE with the value mydb.<br/><br/>

`-v /my/local/data:/var/lib/mysql \`

Mounts a volume from the host (/my/local/data) to the container (/var/lib/mysql).<br/><br/>

`--restart always \`

 Configures the container to always restart if it stops.<br/><br/>

`mysql:5.7`

Specifies the Docker image and version to run (mysql:5.7).<br/><br/>

`docker logs -f <container_name>`

Fetch and follow the logs of a container (live logs)<br/><br/>

`docker port <container_id>`

Show exposed ports of a container<br/><br/>

`docker inspect <container_name>`

Inspect a running container<br/><br/>

`docker container stats`

View resource usage stats<br/><br/>

`docker system df`

Check Docker daemon disk space usage<br/><br/>

`docker system prune -af`

Remove images, networks, containers, and volumes<br/><br/>

`docker diff <container_name>`

Show differences with the images (modified files)<br/><br/>

`docker top <container_name>`

List the processes running on the container<br/><br/>

`docker volume ls`

List volumes<br/><br/>

`docker volume create --name <volume_name>`

Create a local volume<br/><br/>

`docker volume inspect my_volume`

Inspect a volume for detailed information<br/><br/>

`docker run -v <volume_name>:/data <image-name>`

Mount a volume on container start (e.g., docker run -v /host/path:/container/path nginx)<br/><br/>

`docker run -v /host/path:/container/path nginx`

`docker run -d --name my_container -v my_volume:/data nginx`

Use a volume when running a container<br/><br/>

`docker run -d --name my_container -v /my/local/path:/data nginx`

Mount a volume at a specific path<br/><br/>

`docker volume rm <volume_name>`

Destroy a volume<br/><br/>

`docker run -d --name my_container -v my_volume:/data -v /my/local/path:/config nginx`

Run a container with multiple volumes<br/><br/>

`docker cp <source-path-on-host> <container-name-or-id>:<destination-path-in-container>`

Copy from Host to Container (e.g., docker cp /path/on/host/file.txt my_container:/path/in/container/)<br/><br/>

`docker cp /path/on/host/file.txt my_container:/path/in/container/`

`docker cp <container-name-or-id>:<source-path-in-container> <destination-path-on-host>`

Copy from Container to Host (e.g., docker cp my_container:/path/in/container/file.txt /path/on/host/)<br/><br/>

`docker cp my_container:/path/in/container/file.txt /path/on/host/`

`docker cp /path/on/host/my_directory my_container:/path/in/container/`

Copy a directory from Host to Container<br/><br/>

`docker cp my_container:/path/in/container/my_directory /path/on/host/`

Copy a directory from Container to Host<br/><br/>

The docker export command is used to export the filesystem of a container as a tarball (archive) without the image layers or history. It creates a snapshot of the container's filesystem at the current state.

`docker export -o container_backup.tar my_container`

Export the filesystem of a running or stopped container into a .tar file.<br/><br/>

`docker export my_container > container_backup.tar`

Export the filesystem and view it directly or pipe it to another command.<br/><br/>

`docker network ls`

List All Docker Networks<br/><br/>

`docker network create <network_name>`

Create a local network<br/><br/>

`docker run -d --net <network_name> <image-name>`

Attach a container to a network on start<br/><br/>

`docker run -d --name my-app --network my-network nginx`

Create a container and attach it to a specific network<br/><br/>

`docker network connect <network_name> <container_id>`

Connect a running container to a network<br/><br/>

`docker network connect my-network1 my-container`

`docker network connect my-network2 my-container`

Attach multiple networks to a container<br/><br/>

This command creates a network with a specific subnet (my-static-network) and runs a container with a static IP address (172.18.0.10) on that network.

`docker network create --subnet=172.18.0.0/16 my-static-network`

`docker run -d --name my-app --network my-static-network --ip 172.18.0.10 nginx`

`docker network disconnect <network_name> <container_id>`

Disconnect a container from a network

`docker network disconnect -f my-network $(docker ps -q)`

Disconnect all containers from a network

`docker inspect -f '{{ .NetworkSettings.IPAddress }}' <container_id>`

Query a specific metadata of a running container

`docker network inspect my_network`

Disconnect a container from a network

`docker network rm my_network`

Remove a network

Information: A Dockerfile is a text document that contains a series of instructions on how to build a Docker image. Docker reads the Dockerfile to create an image with the environment and configuration you need for your applications.

`FROM image`

`FROM ubuntu:20.04`

`LABEL (Metadata)`

`LABEL maintainer="your-email@example.com"`

`COPY path dst`

`COPY ./local-file /app/remote-file`

`ADD path dst`

`ADD myapp.tar.gz /app`

`RUN args`

`RUN apt-get update && apt-get install -y curl`

`USER name`

`WORKDIR path`

`WORKDIR /app`

`CMD args`

`CMD ["node", "app.js"]`

`EXPOSE xxxx:xxxx`

`EXPOSE 8080`

`VOLUME mp`

`VOLUME ["/data"]`

1. Dockerfile for a Node.js Application

#### 1. Dockerfile for a Node.js Application

#### 

`FROM node:14`

`WORKDIR /app`

`COPY package*.json ./`

`RUN npm install`

`COPY . .`

`ENV NODE_ENV=production`

`EXPOSE 3000`

`CMD ["npm", "start"]`

2. Dockerfile for a Python Flask Application

#### 2. Dockerfile for a Python Flask Application

#### 

`FROM python:3.9-slim`

`ENV PYTHONDONTWRITEBYTECODE=1`

`ENV PYTHONUNBUFFERED=1`

`WORKDIR /app`

`COPY requirements.txt ./`

`RUN pip install --no-cache-dir -r requirements.txt`

`COPY . .`

`EXPOSE 5000`

`CMD ["python", "app.py"]`

3. Dockerfile for a Java Spring Boot Application

#### 3. Dockerfile for a Java Spring Boot Application

#### 

`FROM openjdk:11-jdk-slim`

`WORKDIR /app`

`COPY target/myapp-0.0.1-SNAPSHOT.jar app.jar`

`EXPOSE 8080`

`ENTRYPOINT ["java", "-jar", "app.jar"]`

4. Dockerfile for an Nginx-based Static Website

#### 4. Dockerfile for an Nginx-based Static Website

#### 

`FROM nginx:alpine`

`COPY ./public /usr/share/nginx/html`

`EXPOSE 80`

5. Dockerfile for a .NET Core Application

#### 5. Dockerfile for a .NET Core Application

#### 

`FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build`

`WORKDIR /app`

`COPY *.csproj ./`

`RUN dotnet restore`

`COPY . ./`

`RUN dotnet publish -c Release -o out`

`FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS runtime`

`WORKDIR /app`

`COPY --from=build /app/out ./`

`EXPOSE 80`

`ENTRYPOINT ["dotnet", "MyApp.dll"]`

6. Dockerfile for a PHP and Apache Application

#### 6. Dockerfile for a PHP and Apache Application

#### 

`FROM php:7.4-apache`

`COPY ./src /var/www/html/`

`RUN chown -R www-data:www-data /var/www/html`

`RUN a2enmod rewrite`

`EXPOSE 80`

`CMD ["apache2-foreground"]`

7. Dockerfile for a Ruby on Rails Application

#### 7. Dockerfile for a Ruby on Rails Application

#### 

`FROM ruby:2.7`

`RUN apt-get update -qq && apt-get install -y nodejs postgresql-client`

`WORKDIR /app`

`COPY Gemfile Gemfile.lock ./`

`RUN bundle install`

`COPY . .`

`EXPOSE 3000`

`CMD ["rails", "server", "-b", "0.0.0.0"]`

8. Dockerfile for a React.js Frontend Application

#### 8. Dockerfile for a React.js Frontend Application

`FROM node:16 AS build`

`WORKDIR /app`

`COPY package*.json ./`

`RUN npm install`

`COPY . .`

`RUN npm run build`

`FROM nginx:alpine`

`COPY --from=build /app/build /usr/share/nginx/html`

`EXPOSE 80`

`CMD ["nginx", "-g", "daemon off;"]`

1. Dockerfile for Production-Ready Node.js Application

#### 1. Dockerfile for Production-Ready Node.js Application

`FROM node:16 AS builder`

`WORKDIR /app`

`COPY package*.json ./`

`RUN npm install --production`

`COPY . .`

`RUN npm run build`

`FROM node:16-alpine`

`RUN addgroup -S appgroup && adduser -S appuser -G appgroup`

`USER appuser`

`WORKDIR /app`

`COPY --from=builder /app/build /app`

`EXPOSE 3000`

`ENV NODE_ENV=production`

`CMD ["npm", "start"]`

2. Dockerfile for a Microservice (Python Flask + Gunicorn)

#### 2. Dockerfile for a Microservice (Python Flask + Gunicorn)

`FROM python:3.9-slim AS base`

`ENV PYTHONDONTWRITEBYTECODE=1`

`ENV PYTHONUNBUFFERED=1`

`RUN apt-get update && apt-get install -y \`

`build-essential \`

`libpq-dev \`

`--no-install-recommends && \`

`rm -rf /var/lib/apt/lists/*`

`WORKDIR /app`

`COPY requirements.txt ./`

`RUN pip install --no-cache-dir -r requirements.txt`

`FROM base AS final`

`COPY . .`

`EXPOSE 5000`

`CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]`

3. Dockerfile for a Java Spring Boot Microservice with Multi-Stage Build

#### 3. Dockerfile for a Java Spring Boot Microservice with Multi-Stage Build

`FROM maven:3.8.4-openjdk-11 AS build`

`WORKDIR /app`

`COPY pom.xml .`

`RUN mvn dependency:go-offline`

`COPY src ./src`

`RUN mvn package -DskipTests`

`FROM openjdk:11-jre-slim`

`WORKDIR /app`

`COPY --from=build /app/target/myapp.jar ./myapp.jar`

`EXPOSE 8080`

`CMD ["java", "-jar", "myapp.jar"]`

4. Dockerfile for a CI/CD Pipeline (Node.js + Alpine + Docker)

#### 4. Dockerfile for a CI/CD Pipeline (Node.js + Alpine + Docker)

`FROM node:16-alpine AS builder`

`WORKDIR /app`

`COPY package*.json ./`

`RUN npm install --production`

`COPY . .`

`RUN npm run build`

`FROM docker:20.10.7-dind`

`RUN apk add --no-cache nodejs npm`

`WORKDIR /app`

`COPY --from=builder /app /app`

`EXPOSE 2375`

`CMD ["dockerd-entrypoint.sh"]`
