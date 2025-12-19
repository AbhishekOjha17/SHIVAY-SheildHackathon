# Deployment Guide

## Prerequisites

- Docker & Docker Compose
- MongoDB 6.0+
- Redis 7.0+
- Node.js 18+
- Python 3.11+

## Local Development Setup

1. Clone the repository
2. Run setup script:
   ```bash
   chmod +x infrastructure/scripts/setup.sh
   ./infrastructure/scripts/setup.sh
   ```

3. Update `.env` file with your configuration

4. Start services:
   ```bash
   docker-compose up -d
   ```

## Production Deployment

1. Update environment variables for production
2. Build Docker images:
   ```bash
   docker-compose build
   ```

3. Deploy to your infrastructure:
   ```bash
   docker-compose up -d
   ```

## Service URLs

- Backend API: `http://localhost:8000`
- Frontend: `http://localhost:3000`
- ML Agents: `http://localhost:8001`
- Action Systems: `http://localhost:8002`
- MongoDB: `mongodb://localhost:27017`
- Redis: `redis://localhost:6379`

## Monitoring

- Health check: `GET /health`
- API docs: `http://localhost:8000/docs`

