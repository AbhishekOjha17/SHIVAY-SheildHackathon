# API Documentation

## Base URL
- Development: `http://localhost:8000`
- Production: `https://api.shivay.emergency`

## Authentication
All endpoints (except public ones) require JWT authentication.

Include the token in the Authorization header:
```
Authorization: Bearer <your-token>
```

## Endpoints

### Emergency Cases
- `POST /api/v1/emergency/` - Create emergency case
- `GET /api/v1/emergency/` - List emergency cases
- `GET /api/v1/emergency/{case_id}` - Get case details
- `PUT /api/v1/emergency/{case_id}` - Update case
- `DELETE /api/v1/emergency/{case_id}` - Delete case
- `POST /api/v1/emergency/{case_id}/resolve` - Resolve case

### Voice Calls
- `POST /api/v1/calls/inbound` - Handle inbound call
- `POST /api/v1/calls/outbound` - Initiate outbound call
- `GET /api/v1/calls/{call_id}` - Get call details

### Ambulance
- `GET /api/v1/ambulance/` - List ambulances
- `GET /api/v1/ambulance/{ambulance_id}/tracking` - Get tracking
- `POST /api/v1/ambulance/dispatch` - Dispatch ambulance

### Hospital
- `GET /api/v1/hospital/` - List hospitals
- `GET /api/v1/hospital/{hospital_id}/resources` - Get resources
- `PUT /api/v1/hospital/{hospital_id}/resources` - Update resources

### Police
- `GET /api/v1/police/officers` - List officers
- `POST /api/v1/police/alert` - Send alert
- `GET /api/v1/police/actions` - Get actions

### AI Agents
- `POST /api/v1/ai/transcribe` - Transcribe audio
- `POST /api/v1/ai/analyze` - Analyze text
- `POST /api/v1/ai/severity` - Score severity
- `POST /api/v1/ai/cluster` - Cluster cases
- `POST /api/v1/ai/decide` - Make decision

### Analytics
- `GET /api/v1/analytics/dashboard` - Dashboard data
- `GET /api/v1/analytics/reports` - Generate reports
- `POST /api/v1/analytics/trends` - Analyze trends

### WebSocket
- `ws://localhost:8000/api/v1/websocket` - Real-time updates

