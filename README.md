# Shivay Emergency Response Platform

A comprehensive AI-driven emergency response and inter-agency coordination platform.

## 🏗️ Architecture

The platform follows a 6-layer architecture:

1. **Citizen & Field User Interaction** - Mobile app, web forms, chatbots
2. **API Gateway & Data Processing** - FastAPI gateway with processing pipeline
3. **Core Database & Media Storage** - MongoDB + Cloudinary
4. **AI / Decision Intelligence Layer** - 6 autonomous AI agents
5. **Action & Response Execution** - Ambulance, Hospital, Police, Road Clearance systems
6. **Government Portal & Analytics** - Next.js dashboard with real-time updates
   
<img width="2560" height="1396" alt="TechStackFinal" src="https://github.com/user-attachments/assets/ebd5a345-4948-4932-94bb-c9cf24f5bb3e" />


### 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- MongoDB 6.0+
- Redis 7.0+
- Docker & Docker Compose (optional)

### Environment Setup

1. Copy `.env.example` to `.env` and fill in your configuration
2. Start services with Docker Compose:
   ```bash
   docker-compose up -d
   ```

### Manual Setup

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

#### Mobile App

```bash
cd mobile
npm install
npx react-native run-android  # or run-ios
```

#### ML Agents

```bash
cd ml-agents
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📁 Project Structure

```
shivay-platform/
├── backend/          # FastAPI backend
├── frontend/         # Next.js admin portal
├── mobile/           # React Native mobile app
├── ml-agents/        # ML/AI agents
├── action-systems/   # Response execution systems
├── analytics/        # Analytics & reporting
├── shared/           # Shared code/types
└── infrastructure/   # DevOps & deployment
```

## 🔌 API Endpoints

### Emergency Management
- `POST /api/v1/emergency/` - Create emergency case
- `GET /api/v1/emergency/{case_id}` - Get case details
- `PUT /api/v1/emergency/{case_id}` - Update case
- `GET /api/v1/emergency/` - List all cases

### Voice Calls
- `POST /api/v1/calls/inbound` - Handle inbound call
- `POST /api/v1/calls/outbound` - Initiate outbound call
- `GET /api/v1/calls/{call_id}` - Get call details

### Ambulance
- `GET /api/v1/ambulance/` - List all ambulances
- `GET /api/v1/ambulance/{ambulance_id}/tracking` - Get live tracking
- `POST /api/v1/ambulance/dispatch` - Dispatch ambulance

### Hospital
- `GET /api/v1/hospital/` - List hospitals
- `GET /api/v1/hospital/{hospital_id}/resources` - Get resources
- `PUT /api/v1/hospital/{hospital_id}/resources` - Update resources

### Police
- `GET /api/v1/police/officers` - List officers
- `POST /api/v1/police/alert` - Send alert to officers
- `GET /api/v1/police/actions` - Get officer actions

### AI Agents
- `POST /api/v1/ai/transcribe` - Speech-to-text
- `POST /api/v1/ai/analyze` - NLP analysis
- `POST /api/v1/ai/severity` - Severity scoring
- `POST /api/v1/ai/cluster` - Case clustering
- `POST /api/v1/ai/decide` - Decision orchestration

### Analytics
- `GET /api/v1/analytics/dashboard` - Dashboard data
- `GET /api/v1/analytics/reports` - Generate reports
- `GET /api/v1/analytics/trends` - Trend analysis

### WebSocket
- `ws://localhost:8000/api/v1/websocket` - Real-time updates

## 🤖 AI Agents

1. **Speech-to-Text Agent** - Converts emergency calls to text (Whisper/DeepSpeech)
2. **NLP Understanding Agent** - Extracts intent, entities, urgency
3. **Severity Scoring Agent** - Assigns severity levels (Critical/High/Med/Low)
4. **Case Clustering Agent** - Detects similar cases using vector embeddings
5. **Decision Orchestrator Agent** - Central decision-making hub
6. **Communication AI Agent** - Handles outbound calls and SMS (Twilio/Exotel)

## 🗄️ Database Collections

- `Emergency_Cases` - Emergency case records
- `Caller_Transcripts` - Call transcripts and audio metadata
- `Location_Metadata` - Location data and geocoding
- `Hospital_Resources` - Hospital bed/ICU availability
- `Ambulance_Live_Tracking` - Real-time ambulance positions
- `Police_Officer_Actions` - Officer action logs
- `AI_Recommendations` - AI decision records

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test

# ML agents tests
cd ml-agents
pytest
```



## 👥 Contributors

Team TrailPeriod


