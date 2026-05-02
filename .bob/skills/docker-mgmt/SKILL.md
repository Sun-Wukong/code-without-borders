---
name: docker-mgmt
description: Operate and manage containerized workloads, Docker and beyond
license: MIT
metadata:
  audience: devops
---

## What I do

- Start, stop, delete, modify and extend application containers
- Manage container workloads across different orchestration platforms(Kubernetes, RancherOS, OpenShift, more)
- Build, tag, and export containers to container registries
- Manage container resources(volumes, images, networks, plugins)
- Create blkio disc devices for container volumes

## When to use

Use this when setting up and managing Docker container workloads.

## Best practices

- When requested, use [the blkio volume creation script](./scripts/create_blkio_volume.sh) to create volumes from blkio disks
- When managing container workloads, use `docker compose` instead of `docker`
- Use `docker` for gathering information about containers, images, volumes, and networks.
- Use `docker run` for quick container usage or running individual containers
- Use singular containers for development workflows
- Use Docker Compose container groups to test and evaluate more distributed applications


## Reference Files

| File                                | Contents                                                                | Load When                     |
| ----------------------------------- | ----------------------------------------------------------------------- | ----------------------------- |
| [`Docker CLI reference`](./references/docker.md)   | Usage documentation for `docker` command tree      | Managing standalone containers and resources
| [`Docker Compose CLI reference`](./references/compose.md)  |   Usage documentation for `docker-compose` command tree      | Managing grouped containers and underlying resources         |
| [`Service Architecture Diagram`](./assets/arch_plan.md)  | Blueprint for distributed applications via `docker-compose       | Managing grouped containers and underlying resources         |


## Prerequisites

- `docker` is installed and can be used
- `docker-compose` is installed and can be used
- Existing `DOCKERFILE`, `*.dockerfile`, or `*.docker-compose.yml` files for container definitions

## Workflow

### Building and running individual containers

1. **Building Docker images** — Build Docker container based on a `name:<version>` convention. Use semantic versioning (e.g.:`0.0.0`) to tag images
2. **Create Docker volumes(if needed)** — Use either `docker volume`, include volumes in your `*.docker-compose.yml` definition, or create blkio volumes with [create_blkio_volume.sh](./scripts/create_blkio_volume.sh)
3. **Run containers** — Start running containers with .
4. **Read existing docs** — Current docstrings, OpenAPI metadata, inline documentation.

## Examples

### Running local container applications

**Run a Docker container with a bind mount volume once**:
```bash
$ docker run --rm --name my_container -p 8008:80 -v ./tmp:/app/data debian:slim-bookworm
```

**Run a headless Docker container with a bind mount volume**
```bash
$ docker run --rm --name my_container -p 8008:80 -v ./tmp:/app/data -d debian:slim-bookworm
```

**Start and stop a Docker container**
```bash
$ docker start --name my_container -p 8008:80 -v ./tmp:/app/data -d debian:slim-bookworm
$ docker stop my_container 
```

**Build and run a local multi-container application**
```bash
$ docker-compose up -f prod.docker-compose.yml
```
or
```bash
$ docker-compose build -f prod.docker-compose.yml
$ docker-compose run -f prod.docker-compose.yml
```


**Start and stop a local multi-container application**
```bash
$ docker-compose start -f prod.docker-compose.yml
$ docker-compose stop -f prod.docker-compose.yml
```

**Stop and tear down a local multi-container application**
```bash
$ docker-compose down -f prod.docker-compose.yml
```

**Restart a local multi-container application**
```bash
$ docker-compose restart -f prod.docker-compose.yml
```

### Managing container networks
**Creating a container network and connecting a new container to it**
```bash
$ docker network create bastion-network
$ docker run --rm --name my_container --network=bastion-network -p 8008:80 -v ./tmp:/app/data -d debian:slim-bookworm
```

**Connect a running container to a network**
```bash
$ docker container start my_container 
$ docker network connect bastion-network my_container
```

**Disconnect a container from a network**
```bash
$ docker network disconnect bastion-network my_container
```

**Delete a container network**
```bash
$ docker network rm bastion-network
```

**Delete unused container networks**
```bash
$ docker network prune
```

### Inspecting containers and resources
**Format the output (--format) {#format}**

If a format is specified, the given template will be executed for each result.

Go's [text/template](https://pkg.go.dev/text/template) package describes
all the details of the format.

**Specify target type (--type) {#type}**

`--type config|container|image|node|network|secret|service|volume|task|plugin`

The `docker inspect` command matches any type of object by either ID or name. In
some cases multiple type of objects (for example, a container and a volume)
exist with the same name, making the result ambiguous.

To restrict `docker inspect` to a specific type of object, use the `--type`
option.

The following example inspects a volume named `myvolume`.

```bash
$ docker inspect --type=volume myvolume
```
