# 🐳 Docker Cheat Sheet for Beginners

## 📦 1. Basic Docker Concepts

- **Image**: Blueprint for a container (e.g., OS + App + Environment)
- **Container**: Running instance of an image
- **Dockerfile**: Script to build a Docker image
- **Docker Hub**: Public repo for Docker images
- **Volume**: Persistent data storage for containers
- **Network**: Virtual network for communication between containers

---

## 🛠 2. Docker Installation

```bash
docker --version        # Check Docker version
docker info             # View system-wide Docker info
```
## 🚀3. Docker Image Commands

```bash
# Pull image from Docker Hub
docker pull ubuntu

# List all images
docker images

# Build image from Dockerfile
docker build -t myimage .

# Remove an image
docker rmi image_name_or_id
```
## 📦4. Docker Container Commands
```bash
# Run a container from image
docker run ubuntu

# Run with interactive shell
docker run -it ubuntu bash

# Run in detached mode (background)
docker run -d ubuntu

# Name your container
docker run --name mycontainer ubuntu

# List all running containers
docker ps

# List all containers (even stopped)
docker ps -a

# Stop a container
docker stop container_id_or_name

# Start a container
docker start container_id_or_name

# Remove a container
docker rm container_id_or_name
```
---
## ⚙️ 5. Working Inside Containers
```bash
# Execute command in a running container
docker exec -it container_name bash

# Attach to a running container
docker attach container_name
```
## 📁 6. Volumes & Mounts
```bash
# Create a volume
docker volume create myvolume

# Use volume with container
docker run -v myvolume:/data ubuntu

# Bind mount local folder
docker run -v /host/path:/container/path ubuntu
```
## 🌐 7. Networking
```bash
# List networks
docker network ls

# Create a network
docker network create mynetwork

# Run container on specific network
docker run --network=mynetwork nginx

```
## 📄 8. Dockerfile Basics
```dockerfile
# Example Dockerfile
FROM ubuntu
RUN apt update && apt install -y nginx
COPY . /app
WORKDIR /app
CMD ["nginx", "-g", "daemon off;"]
```
### Build with:

```bash
docker build -t my-nginx .
```
## 📦 9. Docker Compose
```yaml
# docker-compose.yml
version: "3"
services:
  web:
    image: nginx
    ports:
      - "8080:80"
```
### Use it:
```bash
docker-compose up
docker-compose down
```
## 🧹 10. Cleanup Commands
```bash
# Remove all stopped containers
docker container prune

# Remove all unused images
docker image prune

# Remove all unused volumes
docker volume prune

# System-wide cleanup
docker system prune
```
