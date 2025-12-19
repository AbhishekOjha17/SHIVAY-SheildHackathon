#!/bin/bash

# Setup script for Shivay platform

echo "Setting up Shivay Emergency Response Platform..."

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "Please update .env with your configuration"
fi

# Create necessary directories
echo "Creating directories..."
mkdir -p logs
mkdir -p ml-agents/models
mkdir -p analytics/reports

# Setup Python virtual environments
echo "Setting up Python environments..."

# Backend
if [ ! -d "backend/venv" ]; then
    echo "Creating backend virtual environment..."
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
    cd ..
fi

# ML Agents
if [ ! -d "ml-agents/venv" ]; then
    echo "Creating ML agents virtual environment..."
    cd ml-agents
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
    cd ..
fi

# Action Systems
if [ ! -d "action-systems/venv" ]; then
    echo "Creating action systems virtual environment..."
    cd action-systems
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
    cd ..
fi

# Analytics
if [ ! -d "analytics/venv" ]; then
    echo "Creating analytics virtual environment..."
    cd analytics
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
    cd ..
fi

# Frontend
echo "Setting up frontend..."
cd frontend
if [ ! -d "node_modules" ]; then
    npm install
fi
cd ..

# Mobile
echo "Setting up mobile app..."
cd mobile
if [ ! -d "node_modules" ]; then
    npm install
fi
cd ..

echo "Setup complete!"
echo "Next steps:"
echo "1. Update .env file with your configuration"
echo "2. Start MongoDB and Redis"
echo "3. Run: docker-compose up -d"

