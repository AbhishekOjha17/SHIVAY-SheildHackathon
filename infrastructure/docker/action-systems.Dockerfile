FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY action-systems/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY action-systems/ /app/
COPY shared/ /app/shared/

# Expose port
EXPOSE 8002

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]

