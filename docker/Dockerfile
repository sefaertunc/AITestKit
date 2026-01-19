# AITestKit Docker Image
#
# Build: docker build -t aitestkit -f docker/Dockerfile .
# Run: docker run --rm -v $(pwd):/workspace -e ANTHROPIC_API_KEY aitestkit --help
#
# Multi-stage build for smaller final image

FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for better caching
COPY pyproject.toml .
COPY README.md .
COPY src/ src/

# Install package
RUN pip install --no-cache-dir .

# --- Final stage ---
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy source for development
COPY src/ src/

# Create non-root user
RUN useradd -m aitestkit
USER aitestkit

# Set working directory for user projects
WORKDIR /workspace

# Entry point
ENTRYPOINT ["python", "-m", "aitestkit"]
CMD ["--help"]
