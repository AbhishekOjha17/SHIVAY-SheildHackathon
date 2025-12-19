FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY ml-agents/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ml-agents/ /app/
COPY shared/ /app/shared/

# Expose port
EXPOSE 8001

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

