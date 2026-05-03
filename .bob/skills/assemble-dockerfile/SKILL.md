---
name: assemble-dockerfile
description: Create Dockerfiles based on codebases
license: MIT
metadata:
  audience: devops
---

## What I do

- Review codebases and:
  - Identify the required dependencies to install
  - Identify the required base image, per codebase language
  - Consider additional details like environment variables, ports, etc.
  - Confirm configuration commands to set up the codebase and environment
- Create a Dockerfile based on the information gathered
- Offer to build the image after completing the Dockerfile

## When to use

Use this when creating Docker images to host and deploy your codebase.

## Best practices

- Start by identifying the codebase structure
- Refer to the codebase program files to identify the base image and programming language
- Read manifest, requirement files, configuration files, and environment variables to identify details for the Dockerfile
- Write a `WORKSPACE` to `COPY` the codebase to the container image 
- use `RUN` to install dependencies and perform additional setup commands
- Finalize the container definition with a `CMD` or `ENTRYPOINT` to start the container


## Reference Files

| File                                | Contents                                                                | Load When                     |
| ----------------------------------- | ----------------------------------------------------------------------- | ----------------------------- |
| [`VueJS tutorial container`](./references/learn-vue/)   | Sample Codebase with simple Dockerfile      | Reference for creating Dockerfiles |


## Workflow

### Writing Dockerfiles for your codebase

1. **Scanning the codebase** — Scan the codebase directory to identify the required dependencies to install, base image required to run the codebase, and any additional details like environment variables, ports, etc.
2. **Draft Dockerfile** — Use the details gathered to write the Dockerfile layers
3. **Review Dockerfile** — Explain what each layer of the Dockerfile does and how it results in a running container
4. **Get approval or changes** — Ask if the Dockerfile is correct and meets the requirements to run the codebase
