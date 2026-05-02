---
name: design-container-solution
description: Create Markdown documents, detailing Docker resources and properties 
license: MIT
metadata:
  audience: devops
---

## What I do

- Collect container image details from prompts or conversation context
- Express distributed container application designs with `mermaid.architecture` diagrams
- Write `<name>.DOCKERFILE` container image definitions, based on `mermaid.architecture` diagram
- Write `docker compose` defintions, saving the information to a `*.docker-compose.yml` file

## When to use

Use this when you are planning distributed applications based on Docker containers.

## Best practices

- Refer to the [docker compose reference](./reference/compose-spec.json) schema when writing `docker compose` definitions
- When writing Mermaid diagrams, refer to the [Architecture Specification](https://mermaid.ai/open-source/syntax/architecture.html#services) for guidelines on `docker compose` definition design
- Refer to the [Dockerfile specification](./reference/dockerfile-spec.md) when writing `DOCKERFILE` definitions

## Workflow
1. Ask the user if they're planning a single container or a group of containers
2. Collect details of the intended container or container group, and confirm with the user
3. If planning a ... 
  - Container: Write a list of required layers(base image, customization steps, commands, entry point command). Check [your references](./references) for DOCKERFILE samples showing a single and a multi-stage container build 
  - Multi-container application: Write a `mermaid` diagram, using an `architecture` schema. A reference may be found [here](./references)
4. Confirm drafted documents contain all details the user needs for their plan
5. Write the `DOCKERFILE` or `*.docker-compose.yml` definition, based on the drafted documents
6. Confirm the drafted definition file is what the user is looking for
7. If fixes are necessary, ask the user for details on what needs to be changed

### Procedures
**Mermaid to Docker Compose Translation**

## Examples
- Hypothetical Jellyfin `docker-compose.yml` [definition](./references/jfin.docker-compose.yml)
- Singular `DOCKERFILE` definition for a [`yt_dlp` container](./references/)