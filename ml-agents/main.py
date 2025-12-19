"""
ML Agents Service - FastAPI application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from agents.speech_to_text.agent import SpeechToTextAgent
from agents.nlp_understanding.agent import NLPUnderstandingAgent
from agents.severity_scoring.agent import SeverityScoringAgent
from agents.case_clustering.agent import CaseClusteringAgent
from agents.decision_orchestrator.agent import DecisionOrchestratorAgent
from agents.communication_ai.agent import CommunicationAIAgent
from agents.code_generation.agent import CodeGenerationAgent

app = FastAPI(
    title="Shivay ML Agents Service",
    description="ML/AI Agents for emergency response",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agents
speech_agent = SpeechToTextAgent()
nlp_agent = NLPUnderstandingAgent()
severity_agent = SeverityScoringAgent()
clustering_agent = CaseClusteringAgent()
orchestrator_agent = DecisionOrchestratorAgent()
communication_agent = CommunicationAIAgent()
code_agent = CodeGenerationAgent()


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "Shivay ML Agents",
        "status": "operational",
        "agents": [
            "speech-to-text",
            "nlp-understanding",
            "severity-scoring",
            "case-clustering",
            "decision-orchestrator",
            "communication-ai",
            "code-generation",
        ],
    }


@app.post("/agents/speech-to-text/transcribe")
async def transcribe_audio(request: dict):
    """Transcribe audio"""
    audio_url = request.get("audio_url")
    language = request.get("language")
    result = await speech_agent.transcribe_from_url(audio_url, language)
    return result


@app.post("/agents/nlp/analyze")
async def analyze_text(request: dict):
    """Analyze text"""
    text = request.get("text")
    case_id = request.get("case_id")
    result = await nlp_agent.analyze_text(text, case_id)
    return result


@app.post("/agents/severity/score")
async def score_severity(request: dict):
    """Score severity"""
    case_id = request.get("case_id")
    context = request.get("context", {})
    result = await severity_agent.score_severity(case_id, context)
    return result


@app.post("/agents/clustering/cluster")
async def cluster_cases(request: dict):
    """Cluster cases"""
    case_id = request.get("case_id")
    case_text = request.get("case_text", "")
    historical_cases = request.get("historical_cases", [])
    result = await clustering_agent.find_similar_cases(case_id, case_text, historical_cases)
    return result


@app.post("/agents/orchestrator/decide")
async def make_decision(request: dict):
    """Make decision"""
    case_id = request.get("case_id")
    result = await orchestrator_agent.make_decision(case_id)
    return result


@app.post("/agents/communication/call")
async def make_call(request: dict):
    """Make outbound call"""
    to_number = request.get("to_number")
    message = request.get("message")
    case_id = request.get("case_id")
    result = await communication_agent.make_outbound_call(to_number, message, case_id)
    return result


@app.post("/agents/communication/sms")
async def send_sms(request: dict):
    """Send SMS"""
    to_number = request.get("to_number")
    message = request.get("message")
    case_id = request.get("case_id")
    result = await communication_agent.send_sms(to_number, message, case_id)
    return result


@app.post("/agents/code-generation/widget")
async def generate_widget(request: dict):
    """Generate dashboard widget"""
    widget_type = request.get("widget_type")
    config = request.get("config", {})
    result = await code_agent.generate_dashboard_widget(widget_type, config)
    return result

