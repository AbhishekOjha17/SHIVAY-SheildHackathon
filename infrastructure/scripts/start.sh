#!/bin/bash

# Start script for Shivay platform

echo "Starting Shivay Emergency Response Platform..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker is not running. Please start Docker first."
    exit 1
fi

# Start services with Docker Compose
echo "Starting services with Docker Compose..."
docker-compose up -d

echo "Services started!"
echo "Backend API: http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo "ML Agents: http://localhost:8001"
echo "Action Systems: http://localhost:8002"

