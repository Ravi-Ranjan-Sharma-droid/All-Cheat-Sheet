# Complete Docker Learning Guide: Beginner to Advanced

## Table of Contents
1. [Introduction to Containers](#introduction-to-containers)
2. [Installing Docker](#installing-docker)
3. [Docker CLI Essentials](#docker-cli-essentials)
4. [Images vs Containers](#images-vs-containers)
5. [Building Images with Dockerfiles](#building-images-with-dockerfiles)
6. [Volumes & Bind Mounts](#volumes--bind-mounts)
7. [Networking](#networking)
8. [Docker Compose](#docker-compose)
9. [Container Lifecycle](#container-lifecycle)
10. [Multi-Stage Builds](#multi-stage-builds)
11. [Debugging & Logs](#debugging--logs)
12. [Docker Registry](#docker-registry)
13. [Best Practices](#best-practices)
14. [Docker Security](#docker-security)
15. [Advanced Use Cases](#advanced-use-cases)
16. [Command Reference Cheatsheet](#command-reference-cheatsheet)

---

## Introduction to Containers

### What are Containers?
Containers are lightweight, portable, and isolated environments that package applications with all their dependencies. Think of them as standardized shipping containers for software.

### Key Benefits
- *Consistency*: "Works on my machine" becomes "works everywhere"
- *Isolation*: Applications run independently without conflicts
- *Portability*: Run anywhere Docker is installed
- *Efficiency*: Share OS kernel, lighter than VMs
- *Scalability*: Easy to spin up/down instances

### Containers vs Virtual Machines

Virtual Machines                 Containers
┌─────────────────────┐         ┌─────────────────────┐
│   App A   │  App B  │         │   App A   │  App B  │
├───────────┼─────────┤         ├───────────┼─────────┤
│  Guest OS │Guest OS │         │   Runtime Libraries │
├─────────────────────┤         ├─────────────────────┤
│     Hypervisor      │         │   Container Engine  │
├─────────────────────┤         ├─────────────────────┤
│      Host OS        │         │      Host OS        │
└─────────────────────┘         └─────────────────────┘


### Docker Architecture
- *Docker Engine*: Core runtime and management layer
- *Docker Images*: Read-only templates for containers
- *Docker Containers*: Running instances of images
- *Docker Registry*: Storage for images (Docker Hub, private registries)

---

## Installing Docker

### Windows Installation

#### Docker Desktop for Windows
bash
# Download from: https://docs.docker.com/desktop/windows/install/
# Requirements: Windows 10/11 Pro, Enterprise, or Education
# WSL2 or Hyper-V backend required


#### Post-Installation Verification
bash
docker --version
docker run hello-world


*Common Windows Issues:*
- Enable WSL2 feature in Windows Features
- Ensure virtualization is enabled in BIOS
- Docker Desktop may require restart after installation

### macOS Installation

#### Docker Desktop for Mac
bash
# Download from: https://docs.docker.com/desktop/mac/install/
# Available for Intel and Apple Silicon Macs


#### Using Homebrew
bash
brew install --cask docker


#### Verification
bash
docker --version
docker-compose --version


### Linux Installation

#### Ubuntu/Debian
bash
# Update package index
sudo apt-get update

# Install prerequisites
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Add repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin


#### CentOS/RHEL/Fedora
bash
# Install using DNF/YUM
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker


#### Post-Installation Linux Setup
bash
# Add user to docker group (avoid sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker run hello-world


---

## Docker CLI Essentials

### Core Commands Structure
bash
docker [OPTIONS] COMMAND [ARG...]


### Image Management
bash
# List images
docker images
docker image ls

# Pull image from registry
docker pull nginx
docker pull nginx:1.21-alpine

# Remove images
docker rmi image_name
docker image rm image_id

# Search for images
docker search python

# Image history
docker history nginx


### Container Operations
bash
# Run container
docker run nginx                    # Foreground
docker run -d nginx                 # Background (detached)
docker run -it ubuntu bash          # Interactive with TTY

# List containers
docker ps                          # Running containers
docker ps -a                       # All containers

# Start/Stop containers
docker start container_name
docker stop container_name
docker restart container_name

# Remove containers
docker rm container_name
docker rm -f container_name        # Force remove running container


### Advanced Run Options
bash
# Port mapping
docker run -p 8080:80 nginx        # Host:Container

# Environment variables
docker run -e NODE_ENV=production node:alpine

# Volume mounting
docker run -v /host/path:/container/path nginx

# Name containers
docker run --name my-nginx nginx

# Resource limits
docker run --memory="512m" --cpus="1.5" nginx


### Container Interaction
bash
# Execute commands in running container
docker exec -it container_name bash
docker exec container_name ls -la

# Copy files
docker cp file.txt container_name:/path/
docker cp container_name:/path/file.txt ./

# View container details
docker inspect container_name


### System Management
bash
# System information
docker system info
docker system df                   # Disk usage

# Clean up
docker system prune               # Remove unused data
docker system prune -a            # Remove all unused images
docker container prune            # Remove stopped containers
docker image prune               # Remove dangling images


---

## Images vs Containers

### Understanding the Relationship

Image (Template)          Container (Instance)
┌─────────────────┐      ┌─────────────────┐
│     nginx       │ ───→ │   nginx:8080    │
│   (Read-only)   │      │   (Writable)    │
└─────────────────┘      └─────────────────┘
                          ┌─────────────────┐
                     ───→ │   nginx:8081    │
                          │   (Writable)    │
                          └─────────────────┘


### Image Concepts
- *Layers*: Images are built in layers for efficiency
- *Base Images*: Starting point (e.g., ubuntu, alpine)
- *Tags*: Version identifiers (latest, v1.0, stable)
- *Digest*: Immutable content identifier

### Image Layers Example
bash
# View image layers
docker history nginx

# Example output:
IMAGE          CREATED BY                                      SIZE
e784f4560448   /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
<missing>      /bin/sh -c #(nop)  STOPSIGNAL SIGQUIT           0B
<missing>      /bin/sh -c #(nop)  EXPOSE 80                    0B


### Container States
bash
# Container lifecycle states
Created → Running → Paused → Stopped → Deleted

# Check container status
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"


---

## Building Images with Dockerfiles

### Dockerfile Basics
A Dockerfile contains instructions to build a Docker image.

### Essential Instructions

#### Basic Structure
dockerfile
# Comment
FROM base_image:tag
LABEL maintainer="your-email@domain.com"
WORKDIR /app
COPY source dest
RUN command
EXPOSE port
CMD ["executable","param1","param2"]


#### FROM - Base Image
dockerfile
FROM ubuntu:20.04
FROM node:16-alpine
FROM python:3.9-slim


#### WORKDIR - Set Working Directory
dockerfile
WORKDIR /app
# Subsequent instructions execute from /app


#### COPY vs ADD
dockerfile
# COPY (preferred) - Simple file/directory copy
COPY package.json /app/
COPY . /app/

# ADD - Has additional features (URL download, auto-extract)
ADD https://example.com/file.tar.gz /app/
ADD archive.tar.gz /app/  # Auto-extracts


#### RUN - Execute Commands
dockerfile
# Shell form
RUN apt-get update && apt-get install -y python3

# Exec form (preferred)
RUN ["apt-get", "update"]


### Complete Examples

#### Node.js Application
dockerfile
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# Change ownership
RUN chown -R nextjs:nodejs /app
USER nextjs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

# Start application
CMD ["npm", "start"]


#### Python Application
dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /code

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Create user
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /code
USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]


### Building Images
bash
# Basic build
docker build -t my-app .

# Build with context and tag
docker build -t my-app:v1.0 -f Dockerfile.prod .

# Build with build arguments
docker build --build-arg NODE_ENV=production -t my-app .

# Build for different platforms
docker buildx build --platform linux/amd64,linux/arm64 -t my-app .


### Build Arguments and Environment Variables
dockerfile
# Build arguments (compile-time)
ARG NODE_ENV=development
ARG BUILD_DATE

# Environment variables (runtime)
ENV NODE_ENV=${NODE_ENV}
ENV PORT=3000


*Common Pitfalls:*
- Layer caching: Order instructions for optimal caching
- Use .dockerignore to exclude unnecessary files
- Combine RUN commands to reduce layers
- Don't install unnecessary packages

---

## Volumes & Bind Mounts

### Types of Mounts
1. *Volumes*: Managed by Docker, best for persistence
2. *Bind Mounts*: Direct host filesystem mounting
3. *tmpfs Mounts*: Stored in host memory only

### Volumes

#### Creating and Managing Volumes
bash
# Create volume
docker volume create my-volume

# List volumes
docker volume ls

# Inspect volume
docker volume inspect my-volume

# Remove volume
docker volume rm my-volume

# Remove all unused volumes
docker volume prune


#### Using Volumes in Containers
bash
# Mount named volume
docker run -v my-volume:/data nginx

# Anonymous volume
docker run -v /data nginx

# Multiple volumes
docker run -v vol1:/data1 -v vol2:/data2 nginx


### Bind Mounts
bash
# Absolute path required
docker run -v /host/path:/container/path nginx

# Current directory
docker run -v $(pwd):/app node:alpine

# Read-only mount
docker run -v /host/path:/container/path:ro nginx


### Practical Examples

#### Database Persistence
bash
# PostgreSQL with persistent data
docker run -d \
  --name postgres-db \
  -e POSTGRES_PASSWORD=secret \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:13


#### Development Environment
bash
# Node.js development with live reload
docker run -d \
  --name dev-server \
  -p 3000:3000 \
  -v $(pwd):/app \
  -v /app/node_modules \
  node:16-alpine \
  npm run dev


### Volume Driver and Options
bash
# Using different volume drivers
docker volume create \
  --driver local \
  --opt type=nfs \
  --opt o=addr=192.168.1.1,rw \
  --opt device=:/path/to/dir \
  nfs-volume


### Best Practices
- Use volumes for data that needs to persist
- Use bind mounts for development and configuration files
- Avoid storing sensitive data in volumes without encryption
- Use .dockerignore with bind mounts to exclude unnecessary files

---

## Networking

### Docker Network Types
1. *Bridge*: Default, isolated network
2. *Host*: Share host's network stack
3. *None*: No networking
4. *Overlay*: Multi-host networking (Swarm)
5. *Custom*: User-defined networks

### Network Management
bash
# List networks
docker network ls

# Create network
docker network create my-network
docker network create --driver bridge my-bridge

# Inspect network
docker network inspect bridge

# Remove network
docker network rm my-network

# Connect/disconnect containers
docker network connect my-network container-name
docker network disconnect my-network container-name


### Network Examples

#### Default Bridge Network
bash
# Containers can communicate via IP
docker run -d --name web nginx
docker run -d --name app node:alpine

# Find container IP
docker inspect web | grep IPAddress


#### Custom Bridge Network
bash
# Create custom network
docker network create web-network

# Run containers on custom network
docker run -d --name web --network web-network nginx
docker run -d --name app --network web-network node:alpine

# Containers can communicate by name
docker exec app ping web


#### Port Publishing
bash
# Publish specific port
docker run -p 8080:80 nginx

# Publish all exposed ports
docker run -P nginx

# Bind to specific interface
docker run -p 127.0.0.1:8080:80 nginx

# Multiple port mappings
docker run -p 8080:80 -p 8443:443 nginx


### Multi-Container Communication
dockerfile
# docker-compose.yml example
version: '3.8'
services:
  web:
    image: nginx
    networks:
      - frontend
  
  api:
    image: node:alpine
    networks:
      - frontend
      - backend
  
  db:
    image: postgres:13
    networks:
      - backend

networks:
  frontend:
  backend:


### Network Security
bash
# Isolated networks
docker network create --internal secure-network

# Network with custom subnet
docker network create \
  --driver bridge \
  --subnet=172.20.0.0/16 \
  --ip-range=172.20.240.0/20 \
  custom-network


---

## Docker Compose

### What is Docker Compose?
Docker Compose is a tool for defining and running multi-container Docker applications using YAML files.

### Basic docker-compose.yml Structure
yaml
version: '3.8'

services:
  service-name:
    image: image-name
    # or
    build: ./path-to-dockerfile
    
volumes:
  volume-name:
  
networks:
  network-name:


### Essential Compose Commands
bash
# Start services
docker-compose up
docker-compose up -d                # Detached mode
docker-compose up --build           # Force rebuild

# Stop services
docker-compose down
docker-compose down -v              # Remove volumes
docker-compose down --rmi all       # Remove images

# View logs
docker-compose logs
docker-compose logs service-name

# Scale services
docker-compose up --scale web=3

# Execute commands
docker-compose exec service-name bash


### Complete Web Application Example
yaml
version: '3.8'

services:
  # Reverse Proxy
  nginx:
    image: nginx:alpine
    container_name: nginx-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - web
    networks:
      - frontend
    restart: unless-stopped

  # Web Application
  web:
    build: 
      context: .
      dockerfile: Dockerfile.prod
    container_name: web-app
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://user:pass@db:5432/myapp
      - REDIS_URL=redis://redis:6379
    volumes:
      - ./uploads:/app/uploads
    depends_on:
      - db
      - redis
    networks:
      - frontend
      - backend
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Database
  db:
    image: postgres:13-alpine
    container_name: postgres-db
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - backend
    secrets:
      - db_password
    restart: unless-stopped

  # Redis Cache
  redis:
    image: redis:6-alpine
    container_name: redis-cache
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - backend
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true

secrets:
  db_password:
    file: ./secrets/db_password.txt


### Environment Variables
yaml
# Method 1: Direct declaration
services:
  web:
    environment:
      - NODE_ENV=production
      - API_KEY=secret123

# Method 2: Environment file
services:
  web:
    env_file:
      - .env
      - .env.local

# Method 3: Array format
services:
  web:
    environment:
      NODE_ENV: production
      API_KEY: secret123


### Development vs Production Configs
yaml
# docker-compose.yml (base)
version: '3.8'
services:
  web:
    build: .
    volumes:
      - .:/app

# docker-compose.override.yml (development - auto-loaded)
version: '3.8'
services:
  web:
    command: npm run dev
    ports:
      - "3000:3000"

# docker-compose.prod.yml (production)
version: '3.8'
services:
  web:
    command: npm start
    restart: unless-stopped


### Using Override Files
bash
# Development (uses docker-compose.yml + docker-compose.override.yml)
docker-compose up

# Production
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d


---

## Container Lifecycle

### Container States

Created → Running → Paused → Stopped → Deleted
    ↓        ↓        ↓         ↓
  Start    Pause    Stop    Remove


### Lifecycle Management Commands
bash
# Create container without starting
docker create --name my-container nginx

# Start existing container
docker start my-container

# Pause/unpause container
docker pause my-container
docker unpause my-container

# Stop container gracefully
docker stop my-container              # SIGTERM then SIGKILL after 10s
docker stop -t 30 my-container        # Custom timeout

# Kill container immediately
docker kill my-container              # SIGKILL
docker kill -s SIGTERM my-container   # Custom signal

# Restart container
docker restart my-container


### Container Resource Management
bash
# Resource limits during run
docker run --memory="512m" --cpus="1.5" --name limited nginx

# Update running container resources
docker update --memory="1g" --cpus="2" my-container

# Monitor resource usage
docker stats
docker stats --no-stream              # One-time stats
docker stats container1 container2    # Specific containers


### Health Checks
dockerfile
# In Dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1


bash
# Runtime health check
docker run -d \
  --health-cmd="curl -f http://localhost:8080/health || exit 1" \
  --health-interval=30s \
  --health-timeout=3s \
  --health-retries=3 \
  my-app


### Container Events and Monitoring
bash
# Watch container events
docker events
docker events --filter container=my-container

# Container processes
docker top my-container

# Container resource usage
docker stats my-container

# Container filesystem changes
docker diff my-container


### Restart Policies
bash
# No restart (default)
docker run --restart=no nginx

# Always restart
docker run --restart=always nginx

# Restart unless manually stopped
docker run --restart=unless-stopped nginx

# Restart on failure with max attempts
docker run --restart=on-failure:3 nginx


---

## Multi-Stage Builds

### Why Multi-Stage Builds?
- Reduce final image size
- Separate build and runtime environments
- Include only necessary artifacts
- Improved security by excluding build tools

### Basic Multi-Stage Example
dockerfile
# Build stage
FROM node:16-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Production stage
FROM node:16-alpine AS production
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
EXPOSE 3000
CMD ["npm", "start"]


### Advanced Multi-Stage Build
dockerfile
# Development dependencies stage
FROM node:16-alpine AS dev-deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Build stage
FROM dev-deps AS builder
COPY . .
RUN npm run build
RUN npm run test

# Production dependencies
FROM node:16-alpine AS prod-deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

# Final production stage
FROM node:16-alpine AS production
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

WORKDIR /app

# Copy built application
COPY --from=builder --chown=nextjs:nodejs /app/dist ./dist
COPY --from=prod-deps --chown=nextjs:nodejs /app/node_modules ./node_modules
COPY --chown=nextjs:nodejs package*.json ./

USER nextjs

EXPOSE 3000
ENV NODE_ENV=production

CMD ["npm", "start"]


### Go Application Multi-Stage
dockerfile
# Build stage
FROM golang:1.19-alpine AS builder

RUN apk add --no-cache git

WORKDIR /app

# Copy go mod files
COPY go.mod go.sum ./
RUN go mod download

# Copy source code
COPY . .

# Build binary
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

# Final stage
FROM alpine:latest AS production

RUN apk --no-cache add ca-certificates
WORKDIR /root/

# Copy binary from builder stage
COPY --from=builder /app/main .

CMD ["./main"]


### Build Specific Stages
bash
# Build specific stage
docker build --target builder -t my-app:builder .

# Build production stage (default)
docker build -t my-app:latest .

# Build with different target for development
docker build --target development -t my-app:dev .


### Copying from External Images
dockerfile
FROM alpine AS production

# Copy from another image
COPY --from=nginx:alpine /etc/nginx/nginx.conf /etc/nginx/
COPY --from=my-registry/my-image:latest /app/binary /usr/local/bin/

# Copy from previous stage
COPY --from=builder /app/dist ./public


---

## Debugging & Logs

### Container Logs
bash
# View logs
docker logs container_name
docker logs -f container_name         # Follow logs
docker logs --tail 50 container_name  # Last 50 lines
docker logs --since 2h container_name # Since 2 hours ago
docker logs -t container_name         # With timestamps

# Compose logs
docker-compose logs
docker-compose logs -f service_name
docker-compose logs --tail=100


### Debugging Running Containers
bash
# Execute shell in running container
docker exec -it container_name bash
docker exec -it container_name sh     # If bash not available

# Run commands without shell
docker exec container_name ls -la /app
docker exec container_name cat /etc/hosts

# Inspect container configuration
docker inspect container_name

# View processes in container
docker top container_name

# Monitor resource usage
docker stats container_name


### Debugging Failed Containers
bash
# Run container with different command
docker run -it image_name bash

# Check exit code
docker ps -a
# Look at STATUS column for exit codes

# Inspect failed container
docker logs failed_container
docker inspect failed_container


### Network Debugging
bash
# Test connectivity between containers
docker exec container1 ping container2
docker exec container1 nslookup container2
docker exec container1 telnet container2 80

# Check port bindings
docker port container_name

# Network inspection
docker network inspect network_name

# Test from host
curl -I http://localhost:8080
netstat -tulpn | grep 8080


### Advanced Debugging Techniques

#### Debug Init Issues
dockerfile
# Add debugging to Dockerfile
FROM node:16-alpine
WORKDIR /app

# Debug layer
RUN echo "Node version: $(node --version)"
RUN echo "NPM version: $(npm --version)"
RUN pwd && ls -la

COPY package*.json ./
RUN npm ci

COPY . .
RUN ls -la && echo "Files copied successfully"

CMD ["npm", "start"]


#### Container Health Debugging
bash
# Check health status
docker inspect --format='{{.State.Health.Status}}' container_name

# View health check logs
docker inspect --format='{{json .State.Health}}' container_name | jq


#### Performance Debugging
bash
# Monitor resource usage in real-time
docker stats --no-stream

# Check container processes
docker exec container_name ps aux

# Memory usage analysis
docker exec container_name free -h
docker exec container_name cat /proc/meminfo


### Log Configuration
yaml
# docker-compose.yml with logging config
version: '3.8'
services:
  web:
    image: nginx
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"


### Common Debug Scenarios

#### Container Won't Start
bash
# Check image exists
docker images | grep image_name

# Run with interactive shell
docker run -it --entrypoint="" image_name bash

# Check Dockerfile syntax
docker build --no-cache -t debug-image .


#### Application Not Accessible
bash
# Verify port mapping
docker ps
netstat -tulpn | grep port_number

# Check firewall rules
sudo ufw status
sudo iptables -L

# Test internal connectivity
docker exec container_name netstat -tulpn


---

## Docker Registry

### Docker Hub (Public Registry)

#### Basic Registry Operations
bash
# Login to Docker Hub
docker login
docker login -u username

# Tag image for push
docker tag local-image:latest username/repo-name:tag

# Push image
docker push username/repo-name:tag

# Pull image
docker pull username/repo-name:tag

# Logout
docker logout


#### Repository Management
bash
# Create repository structure
username/
├── web-app:latest
├── web-app:v1.0.0
├── web-app:development
└── api-server:latest


### Private Registry Setup

#### Local Registry
bash
# Run local registry
docker run -d -p 5000:5000 --name registry registry:2

# Tag image for local registry
docker tag my-app:latest localhost:5000/my-app:latest

# Push to local registry
docker push localhost:5000/my-app:latest

# Pull from local registry
docker pull localhost:5000/my-app:latest


#### Secure Local Registry
yaml
# docker-compose.yml for secure registry
version: '3.8'
services:
  registry:
    image: registry:2
    ports:
      - "5000:5000"
    environment:
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: Registry Realm
      REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY: /data
      REGISTRY_HTTP_TLS_CERTIFICATE: /certs/domain.crt
      REGISTRY_HTTP_TLS_KEY: /certs/domain.key
    volumes:
      - ./auth:/auth
      - ./certs:/certs
      - ./data:/data
    restart: unless-stopped


#### Authentication Setup
bash
# Create htpasswd file
mkdir auth
docker run --rm --entrypoint htpasswd registry:2 \
  -Bbn testuser testpassword > auth/htpasswd

# Generate SSL certificates (for production)
openssl req -newkey rsa:4096 -nodes -sha256 \
  -keyout certs/domain.key -x509 -days 365 \
  -out certs/domain.crt


### Registry Operations

#### Image Management
bash
# List repositories in registry
curl -X GET https://registry.example.com/v2/_catalog

# List tags for repository
curl -X GET https://registry.example.com/v2/my-app/tags/list

# Get image manifest
curl -X GET https://registry.example.com/v2/my-app/manifests/latest


#### Cleanup and Maintenance
bash
# Remove image from local daemon
docker rmi image:tag

# Registry garbage collection (local registry)
docker exec -it registry bin/registry garbage-collect /etc/docker/registry/config.yml

# Prune unused images
docker image prune -a


### Cloud Registry Services

#### AWS ECR (Elastic Container Registry)
bash
# Login to ECR
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-west-2.amazonaws.com

# Create repository
aws ecr create-repository --repository-name my-app

# Tag and push
docker tag my-app:latest 123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:latest
docker push 123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:latest


#### Google Container Registry (GCR)
bash
# Configure Docker with gcloud
gcloud auth configure-docker

# Tag and push
docker tag my-app:latest gcr.io/project-id/my-app:latest
docker push gcr.io/project-id/my-app:latest


#### Azure Container Registry (ACR)
bash
# Login to ACR
az acr login --name myregistry

# Tag and push
docker tag my-app:latest myregistry.azurecr.io/my-app:latest
docker push myregistry.azurecr.io/my-app:latest


---

## Best Practices

### Dockerfile Best Practices

#### Layer Optimization
dockerfile
# ❌ Bad: Creates multiple layers
FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN rm -rf /var/lib/apt/lists/*

# ✅ Good: Single layer for related commands
FROM ubuntu:20.04
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*


#### Leverage Build Cache
dockerfile
# ✅ Copy dependency files first for better caching
FROM node:16-alpine
WORKDIR /app

# Copy package files first (changes less frequently)
COPY package*.json ./
RUN npm ci --only=production

# Copy source code last (changes more frequently)
COPY . .

CMD ["npm", "start"]


#### Use .dockerignore
bash
# .dockerignore
node_modules
npm-debug.log
.git
.gitignore
README.md
.env
.nyc_output
coverage
.vscode


#### Security Best Practices
dockerfile
# Use non-root user
FROM node:16-alpine

# Create app directory
WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm ci --only=production

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

# Copy app source
COPY --chown=nextjs:nodejs . .

# Switch to non-root user
USER nextjs

EXPOSE 3000
CMD ["npm", "start"]


### Image Optimization

#### Choose Right Base Images
dockerfile
# ✅ Use Alpine for smaller images
FROM node:16-alpine          # ~110MB
# vs
FROM node:16                 # ~350MB

# ✅ Use distroless for production
FROM gcr.io/distroless/nodejs:16

# ✅ Use scratch for static binaries
FROM scratch
COPY binary /
CMD ["/binary"]


#### Multi-stage Build Optimization
dockerfile
# Build stage
FROM node:16-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage - only copy what's needed
FROM node:16-alpine AS production
WORKDIR /app
RUN addgroup -g 1001 -S nodejs && adduser -S nextjs -u 1001

# Copy only production files
COPY --from=builder --chown=nextjs:nodejs /app/dist ./dist
COPY --from=builder --chown=nextjs:nodejs /app/node_modules ./node_modules
COPY --chown=nextjs:nodejs package*.json ./

USER nextjs
EXPOSE 3000
CMD ["npm", "start"]


### Container Runtime Best Practices

#### Resource Management
bash
# Always set resource limits
docker run -d \
  --name web-app \
  --memory="512m" \
  --cpus="1.0" \
  --restart=unless-stopped \
  my-app:latest


#### Health Checks
dockerfile
# Add health checks to containers
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1


#### Logging Configuration
yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    image: my-app:latest
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"


### Development vs Production

#### Development Environment
yaml
# docker-compose.dev.yml
version: '3.8'
services:
  web:
    build:
      context: .
      target: development
    volumes:
      - .:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    command: npm run dev


#### Production Environment
yaml
# docker-compose.prod.yml
version: '3.8'
services:
  web:
    image: my-app:latest
    restart: unless-stopped
    environment:
      - NODE_ENV=production
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3


### Performance Optimization

#### Build Performance
bash
# Use BuildKit for better performance
export DOCKER_BUILDKIT=1
docker build -t my-app .

# Parallel builds
docker buildx build --platform linux/amd64,linux/arm64 -t my-app .


#### Runtime Performance
bash
# Optimize container startup
docker run -d \
  --name fast-app \
  --memory="512m" \
  --cpus="1.0" \
  --ulimit nofile=65536:65536 \
  my-app:latest


---

## Docker Security

### Container Security Fundamentals

#### Run as Non-Root User
dockerfile
# Create and use non-root user
FROM ubuntu:20.04

RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN mkdir -p /app && chown appuser:appuser /app

USER appuser
WORKDIR /app

COPY --chown=appuser:appuser . .
CMD ["./app"]


#### Use Read-Only Filesystems
bash
# Run container with read-only filesystem
docker run --read-only --tmpfs /tmp --tmpfs /run my-app:latest


#### Limit Container Capabilities
bash
# Drop all capabilities and add only needed ones
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE my-app:latest

# Common capabilities to drop
docker run \
  --cap-drop=ALL \
  --cap-add=CHOWN \
  --cap-add=DAC_OVERRIDE \
  --cap-add=FOWNER \
  --cap-add=SETGID \
  --cap-add=SETUID \
  my-app:latest


### Image Security

#### Scan Images for Vulnerabilities
bash
# Using Docker Scout (built-in)
docker scout cves my-app:latest

# Using Trivy
trivy image my-app:latest

# Using Snyk
snyk container test my-app:latest


#### Secure Base Images
dockerfile
# ✅ Use official, minimal base images
FROM node:16-alpine

# ✅ Use distroless images for production
FROM gcr.io/distroless/nodejs:16

# ✅ Pin image versions with digest
FROM node:16-alpine@sha256:a1cc8f7acebb39f3c27fd8c5e4f8f1a1c47e8ca9d9e5c5f8e7b4b0e4f8e7b4b0


#### Keep Images Updated
bash
# Regularly update base images
docker pull node:16-alpine
docker build --no-cache -t my-app:latest .

# Use automated tools for updates
# Dependabot, Renovate, etc.


### Runtime Security

#### Security Profiles
bash
# Run with security profiles
docker run --security-opt apparmor=docker-default my-app:latest

# Use seccomp profiles
docker run --security-opt seccomp=seccomp-profile.json my-app:latest

# Disable seccomp (not recommended for production)
docker run --security-opt seccomp=unconfined my-app:latest


#### Network Security
bash
# Create isolated networks
docker network create --internal backend-network

# Use custom bridge networks
docker network create --driver bridge \
  --subnet=172.20.0.0/16 \
  --gateway=172.20.0.1 \
  secure-network

# Disable inter-container communication
docker network create --driver bridge --opt com.docker.network.bridge.enable_icc=false isolated-network


#### Secrets Management
yaml
# docker-compose.yml with secrets
version: '3.8'
services:
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt


### Host Security

#### Docker Daemon Security
bash
# Secure Docker daemon socket
sudo chmod 660 /var/run/docker.sock
sudo chown root:docker /var/run/docker.sock

# Enable Docker content trust
export DOCKER_CONTENT_TRUST=1
docker push my-app:latest


#### Resource Limits
bash
# Prevent fork bombs and resource exhaustion
docker run \
  --pids-limit 100 \
  --memory="512m" \
  --cpus="1.0" \
  --ulimit nproc=1024:2048 \
  --ulimit nofile=1024:2048 \
  my-app:latest


### Security Scanning and Monitoring

#### Container Security Scanning
dockerfile
# Add security scanning to CI/CD
FROM node:16-alpine

# Install security updates
RUN apk upgrade --no-cache

# Use hadolint for Dockerfile linting
# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    && rm -rf /var/lib/apt/lists/*


#### Runtime Monitoring
bash
# Monitor container behavior
docker run -d \
  --name monitored-app \
  --log-driver=syslog \
  --log-opt syslog-address=tcp://localhost:514 \
  my-app:latest

# Use security monitoring tools
# Falco, Sysdig, Aqua Security, etc.


---

## Advanced Use Cases

### Container Orchestration Preparation

#### Docker Swarm
bash
# Initialize swarm
docker swarm init

# Create services
docker service create --name web-service --publish 8080:80 --replicas 3 nginx

# Scale services
docker service scale web-service=5

# Rolling updates
docker service update --image nginx:1.21 web-service


#### Kubernetes Integration
yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-app
        image: my-app:latest
        ports:
        - containerPort: 3000
        resources:
          requests:
            memory: "128Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "500m"


### CI/CD Integration

#### GitHub Actions
yaml
# .github/workflows/docker.yml
name: Docker Build and Push

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2
    
    - name: Login to DockerHub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}
    
    - name: Build and push
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: |
          user/app:latest
          user/app:${{ github.sha }}
        cache-from: type=gha
        cache-to: type=gha,mode=max


#### Jenkins Pipeline
groovy
pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'my-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
        REGISTRY = 'my-registry.com'
    }
    
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("${REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    docker.image("${REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}").inside {
                        sh 'npm test'
                    }
                }
            }
        }
        
        stage('Push') {
            steps {
                script {
                    docker.withRegistry("https://${REGISTRY}", 'registry-credentials') {
                        docker.image("${REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                        docker.image("${REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}").push('latest')
                    }
                }
            }
        }
    }
}


### Microservices Architecture

#### Service Discovery
yaml
# docker-compose.yml for microservices
version: '3.8'

services:
  # API Gateway
  gateway:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - user-service
      - product-service
      - order-service

  # User Service
  user-service:
    build: ./user-service
    environment:
      - DB_HOST=user-db
      - REDIS_HOST=redis
    depends_on:
      - user-db
      - redis

  user-db:
    image: postgres:13-alpine
    environment:
      POSTGRES_DB: users
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - user-data:/var/lib/postgresql/data

  # Product Service
  product-service:
    build: ./product-service
    environment:
      - DB_HOST=product-db
    depends_on:
      - product-db

  product-db:
    image: mongo:5
    volumes:
      - product-data:/data/db

  # Order Service
  order-service:
    build: ./order-service
    environment:
      - USER_SERVICE_URL=http://user-service:3000
      - PRODUCT_SERVICE_URL=http://product-service:3000
      - QUEUE_HOST=rabbitmq
    depends_on:
      - rabbitmq

  # Shared Services
  redis:
    image: redis:6-alpine
    volumes:
      - redis-data:/data

  rabbitmq:
    image: rabbitmq:3-management-alpine
    ports:
      - "15672:15672"
    environment:
      RABBITMQ_DEFAULT_USER: admin
      RABBITMQ_DEFAULT_PASS: password

volumes:
  user-data:
  product-data:
  redis-data:


### Advanced Networking

#### Custom Network Configuration
bash
# Create custom network with specific configuration
docker network create \
  --driver bridge \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  --opt com.docker.network.bridge.name=custom-bridge \
  --opt com.docker.network.bridge.enable_ip_masquerade=true \
  --opt com.docker.network.bridge.enable_icc=true \
  --opt com.docker.network.bridge.host_binding_ipv4=0.0.0.0 \
  custom-network


#### Load Balancing
yaml
# HAProxy load balancer
version: '3.8'
services:
  haproxy:
    image: haproxy:2.4-alpine
    ports:
      - "80:80"
      - "8404:8404"
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    depends_on:
      - web1
      - web2
      - web3

  web1:
    image: nginx:alpine
    volumes:
      - ./html:/usr/share/nginx/html:ro

  web2:
    image: nginx:alpine
    volumes:
      - ./html:/usr/share/nginx/html:ro

  web3:
    image: nginx:alpine
    volumes:
      - ./html:/usr/share/nginx/html:ro


### Monitoring and Observability

#### Prometheus and Grafana Stack
yaml
version: '3.8'
services:
  # Application
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - METRICS_ENABLED=true

  # Prometheus
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'

  # Grafana
  grafana:
    image: grafana/grafana:latest
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-data:/var/lib/grafana

  # Node Exporter
  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--collector.filesystem.ignored-mount-points=^/(sys|proc|dev|host|etc)($$|/)'

volumes:
  prometheus-data:
  grafana-data:


---

## Command Reference Cheatsheet

### Essential Commands
bash
# Images
docker images                     # List images
docker pull image:tag             # Pull image
docker build -t name:tag .        # Build image
docker rmi image:tag              # Remove image
docker tag source:tag target:tag  # Tag image

# Containers
docker run image                  # Run container
docker run -d image               # Run detached
docker run -it image bash         # Interactive
docker ps                         # List running containers
docker ps -a                      # List all containers
docker stop container             # Stop container
docker start container            # Start container
docker rm container              # Remove container
docker exec -it container bash   # Execute command

# System
docker system info               # System information
docker system df                 # Disk usage
docker system prune              # Clean up unused data
docker logs container            # View logs
docker inspect container        # Inspect container


### Advanced Commands
bash
# Resource Management
docker run --memory="512m" --cpus="1.5" image
docker stats                     # Monitor resources
docker update --memory="1g" container

# Networking
docker network ls                # List networks
docker network create network    # Create network
docker run --network=network image

# Volumes
docker volume ls                 # List volumes
docker volume create volume      # Create volume
docker run -v volume:/path image

# Registry
docker login                     # Login to registry
docker push image:tag            # Push image
docker pull image:tag            # Pull image

# Compose
docker-compose up                # Start services
docker-compose up -d             # Start detached
docker-compose down              # Stop services
docker-compose logs              # View logs
docker-compose exec service bash # Execute command


### Quick Reference Tags
bash
# Common Image Tags
nginx:alpine                     # Alpine-based (smaller)
node:16-alpine                   # Node.js 16 on Alpine
python:3.9-slim                  # Python 3.9 slim
postgres:13                      # PostgreSQL 13
redis:6-alpine                   # Redis 6 on Alpine
ubuntu:20.04                     # Ubuntu 20.04


### Docker-Compose Quick Start
yaml
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    restart: unless-stopped


### Dockerfile Template
dockerfile
FROM node:16-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN addgroup -g 1001 -S nodejs && adduser -S nextjs -u 1001
RUN chown -R nextjs:nodejs /app
USER nextjs
EXPOSE 3000
HEALTHCHECK --interval=30s CMD curl -f http://localhost:3000/health || exit 1
CMD ["npm", "start"]


---

## Conclusion

This comprehensive guide covers Docker from basic concepts to advanced production use cases. Key takeaways:

- *Start Simple*: Begin with basic docker run commands and gradually build complexity
- *Security First*: Always run containers as non-root users and scan images for vulnerabilities
- *Optimize Images*: Use multi-stage builds and appropriate base images to minimize image size
- *Monitor Everything*: Implement logging, health checks, and monitoring from the start
- *Automate Workflows*: Integrate Docker into CI/CD pipelines for consistent deployments

Practice these concepts with real projects, and gradually incorporate more advanced features as your applications grow in complexity. Docker's ecosystem is vast, but mastering these fundamentals will provide a solid foundation for containerized application development and deployment.