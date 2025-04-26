# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install system dependencies required for psycopg2 and other packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    gcc \
    python3-dev \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=cs421_assignment.settings

# Set the working directory in the container
WORKDIR /app

# Copy and install Python dependencies first (for better layer caching)
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Verify Django installation and Python path
RUN python -c "import django; print(f'Django {django.__version__} installed successfully')" && \
    python -c "import sys; print(f'Python path: {sys.path}')"

# Create necessary Django directories (if needed)
RUN mkdir -p /app/static /app/media

# Ensure proper permissions
RUN chown -R 1000:1000 /app && \
    find /app -type d -exec chmod 755 {} \; && \
    find /app -type f -exec chmod 644 {} \; && \
    chmod a+x /app/cs421_assignment/wsgi.py

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import requests; exit(0 if requests.get('http://localhost:8000/health/').status_code == 200 else 1)"

# Expose port
EXPOSE 8000

# Start Django app using gunicorn
CMD ["gunicorn", "cs421_assignment.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120", "--access-logfile", "-"]