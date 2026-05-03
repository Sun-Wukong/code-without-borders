# Docker Setup for NYC Benefits Screener

This document provides instructions for building and running the NYC Benefits Screener application using Docker.

## Prerequisites

- Docker installed on your system
- Docker Compose (optional, for easier management)
- NYC Benefits API credentials

## Building the Docker Image

### From the ny_benefits_screener directory:

```bash
# Build the image
docker build -t nyc-benefits-screener:latest .

# Build with a specific tag
docker build -t nyc-benefits-screener:v0.1.0 .
```

### Build Arguments (if needed in future):

```bash
docker build \
  --build-arg PYTHON_VERSION=3.11 \
  -t nyc-benefits-screener:latest .
```

## Running the Container

### Basic Run

```bash
docker run --rm \
  -e OPENAI_API_KEY="your_openai_key" \
  -e NYC_BENEFITS_USERNAME="your_username" \
  -e NYC_BENEFITS_PASSWORD="your_password" \
  -e NYC_BENEFITS_API_HOST="https://screeningapi.cityofnewyork.us" \
  nyc-benefits-screener:latest
```

### Run with Environment File

Create a `.env` file with your credentials:

```env
OPENAI_API_KEY=sk-...
NYC_BENEFITS_USERNAME=your_username
NYC_BENEFITS_PASSWORD=your_password
NYC_BENEFITS_API_HOST=https://screeningapi.cityofnewyork.us
```

Then run:

```bash
docker run --rm --env-file .env nyc-benefits-screener:latest
```

### Run with Volume Mounts (for outputs)

```bash
docker run --rm \
  --env-file .env \
  -v $(pwd)/output:/app/output \
  nyc-benefits-screener:latest
```

### Interactive Mode

```bash
docker run -it --rm \
  --env-file .env \
  nyc-benefits-screener:latest \
  /bin/bash
```

## Alternative Commands

### Training the Crew

```bash
docker run --rm \
  --env-file .env \
  nyc-benefits-screener:latest \
  python -m ny_benefits_screener.main train 5 training.json
```

### Testing the Crew

```bash
docker run --rm \
  --env-file .env \
  nyc-benefits-screener:latest \
  python -m ny_benefits_screener.main test 2 gpt-4o-mini
```

### Replaying a Task

```bash
docker run --rm \
  --env-file .env \
  nyc-benefits-screener:latest \
  python -m ny_benefits_screener.main replay <task_id>
```

## Docker Compose Setup

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  ny-benefits-screener:
    build:
      context: .
      dockerfile: Dockerfile
    image: nyc-benefits-screener:latest
    container_name: ny-benefits-screener
    env_file:
      - .env
    volumes:
      - ./output:/app/output
      - ./knowledge:/app/knowledge:ro
    restart: unless-stopped
    # Uncomment to override default command
    # command: python -m ny_benefits_screener.main
```

Run with Docker Compose:

```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## Environment Variables

| Variable | Required | Description | Default |
|----------|----------|-------------|---------|
| `OPENAI_API_KEY` | Yes | OpenAI API key for LLM access | - |
| `NYC_BENEFITS_USERNAME` | Yes | NYC Benefits API username | - |
| `NYC_BENEFITS_PASSWORD` | Yes | NYC Benefits API password | - |
| `NYC_BENEFITS_API_HOST` | No | NYC Benefits API host URL | `https://screeningapi.cityofnewyork.us` |
| `PYTHONUNBUFFERED` | No | Python output buffering | `1` |

## Troubleshooting

### Build Issues

**Problem**: `ny_benefits_oas` package not found

**Solution**: Ensure the `ny_benefits_oas` directory exists at `../ny_benefits_oas` relative to the Dockerfile location.

**Problem**: Permission denied errors

**Solution**: Run Docker commands with `sudo` or add your user to the docker group:
```bash
sudo usermod -aG docker $USER
```

### Runtime Issues

**Problem**: Authentication failures

**Solution**: Verify your NYC Benefits API credentials are correct and the account is active.

**Problem**: Module import errors

**Solution**: Check that `PYTHONPATH` is correctly set in the container:
```bash
docker run --rm nyc-benefits-screener:latest python -c "import sys; print(sys.path)"
```

**Problem**: Output files not persisted

**Solution**: Mount a volume to `/app/output`:
```bash
docker run --rm -v $(pwd)/output:/app/output nyc-benefits-screener:latest
```

## Image Size Optimization

The multi-stage build reduces the final image size by:
- Using `python:3.11-slim` base image
- Cleaning up apt cache after installing system dependencies
- Not including development dependencies in the final image
- Excluding unnecessary files via `.dockerignore`

Current estimated image size: ~800MB-1GB (depending on dependencies)

## Security Considerations

1. **Never commit `.env` files** with real credentials to version control
2. **Use Docker secrets** for production deployments:
   ```bash
   docker secret create openai_key openai_key.txt
   docker service create --secret openai_key nyc-benefits-screener:latest
   ```
3. **Scan images** for vulnerabilities:
   ```bash
   docker scan nyc-benefits-screener:latest
   ```
4. **Use specific version tags** instead of `latest` in production

## Production Deployment

For production deployments, consider:

1. **Using a container registry**:
   ```bash
   docker tag nyc-benefits-screener:latest registry.example.com/nyc-benefits-screener:v0.1.0
   docker push registry.example.com/nyc-benefits-screener:v0.1.0
   ```

2. **Implementing health checks** (already included in Dockerfile)

3. **Setting resource limits**:
   ```bash
   docker run --rm \
     --memory="2g" \
     --cpus="1.5" \
     nyc-benefits-screener:latest
   ```

4. **Using orchestration** (Kubernetes, Docker Swarm, etc.)

## Development Workflow

For development with live code updates:

```bash
docker run -it --rm \
  --env-file .env \
  -v $(pwd)/src:/app/src \
  -v $(pwd)/knowledge:/app/knowledge \
  nyc-benefits-screener:latest \
  /bin/bash
```

Then inside the container:
```bash
python -m ny_benefits_screener.main
```

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [NYC Benefits API Documentation](https://screeningapi.cityofnewyork.us/docs)
