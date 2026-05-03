# NYC Benefits Screener - CrewAI Application
# Multi-stage build for optimized Python application

# Stage 1: Base image with Python and uv
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

# Set working directory
WORKDIR /app

# Stage 2: Dependencies installation
FROM base as dependencies

# Copy dependency files
COPY pyproject.toml ./

# Copy the ny_benefits_oas package (OpenAPI client dependency)
COPY ../ny_benefits_oas /app/ny_benefits_oas

# Install ny_benefits_oas package first
WORKDIR /app/ny_benefits_oas
RUN pip install -e .

# Return to main app directory
WORKDIR /app

# Install project dependencies using uv
RUN uv pip install --system -e .

# Stage 3: Application
FROM base as application

# Copy installed dependencies from previous stage
COPY --from=dependencies /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=dependencies /usr/local/bin /usr/local/bin

# Copy application source code
COPY src/ /app/src/
COPY knowledge/ /app/knowledge/
COPY examples/ /app/examples/
COPY pyproject.toml /app/

# Copy ny_benefits_oas for runtime
COPY --from=dependencies /app/ny_benefits_oas /app/ny_benefits_oas

# Set Python path to include both packages
ENV PYTHONPATH="/app/src:/app/ny_benefits_oas:${PYTHONPATH}"

# Create directory for outputs
RUN mkdir -p /app/output

# Set working directory
WORKDIR /app

# Expose port (if needed for future API endpoints)
EXPOSE 8000

# Health check (optional - checks if Python can import the module)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import ny_benefits_screener; print('OK')" || exit 1

# Default command - run the crew
CMD ["python", "-m", "ny_benefits_screener.main"]

# Alternative entry points (can be overridden):
# docker run <image> python -m ny_benefits_screener.main train 5 training.json
# docker run <image> python -m ny_benefits_screener.main test 2 gpt-4o-mini
# docker run <image> python -m ny_benefits_screener.main replay <task_id>
