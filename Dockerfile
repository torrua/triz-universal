FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Install package locally
RUN pip install --no-cache-dir -e .

EXPOSE 8000

ENV PORT=8000
CMD uvicorn genrikh.web.app:app --host 0.0.0.0 --port ${PORT:-8000}
