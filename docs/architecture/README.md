# Architecture Documentation

## System Architecture

The Shivay platform follows a 6-layer architecture:

1. **Citizen & Field User Interaction**
   - Mobile app (React Native)
   - Web dashboard forms
   - WhatsApp/Telegram bots
   - Emergency calls (108/112)

2. **API Gateway & Data Processing**
   - FastAPI gateway
   - Authentication & rate limiting
   - Data cleaning & validation
   - Event timestamping

3. **Core Database & Media Storage**
   - MongoDB for structured data
   - Cloudinary for media files

4. **AI / Decision Intelligence Layer**
   - 6 autonomous AI agents
   - Decision orchestrator
   - Real-time processing

5. **Action & Response Execution**
   - Ambulance dispatch system
   - Hospital notification system
   - Police alert system
   - Road clearance system

6. **Government Portal & Analytics**
   - Next.js dashboard
   - Real-time visualizations
   - Analytics & reporting

## Data Flow

1. User reports emergency → API Gateway
2. Data processing → MongoDB storage
3. AI agents analyze → Decision orchestrator
4. Actions executed → Response systems
5. Real-time updates → Dashboard

## Technology Stack

- **Backend**: FastAPI, Python 3.11+, MongoDB, Redis
- **Frontend**: Next.js 14, TypeScript, Tailwind CSS
- **Mobile**: React Native, TypeScript
- **ML**: Python, Whisper, Sentence Transformers
- **Communication**: Twilio/Exotel
- **Storage**: MongoDB, Cloudinary

