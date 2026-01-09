# AI Ticket Analyzer

A FastAPI service that uses large language models to analyze customer support tickets and return validated, structured outputs (Pydantic schemas) for downstream systems.

## Key features
- Categorizes tickets (Billing, Bug, Feature Request, Other)  
- Detects urgency (Low, Medium, High)  
- Flags toxic or emotional messages  
- Produces a one-line summary and reasoning metadata  
- Outputs validated with Pydantic for predictable structure  
- Production-oriented: retries and error handling

## Requirements
- Python 3.10+  
- An OpenAI-compatible API key

## Installation
1. Clone the repo:
```bash
git clone https://github.com/Wasay-Rana/AI-Ticket-Analyzer.git
cd ai-ticket-analyzer
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

## Run (development)
Start the FastAPI server:
```bash
uvicorn main:myApp --reload
```

Health check:
- GET /health  
    Response: `{ "status": "healthy" }`

Analyze ticket:
- POST /analyze_ticket  
    Request JSON:
```json
{
    "ticket_id": "TCW-123",
    "message": "I was charged twice and need a refund."
}
```

Example response:
```json
{
    "schema_version": "v1",
    "ticket_id": "TCW-123",
    "category": "Billing",
    "urgency": "High",
    "toxic": false,
    "summary": "Amount deducted but purchase not reflected after two card attempts.",
    "confidence": 0.95,
    "reasoning": "Customer reports a failed transaction, categorized as Billing with high urgency.",
    "llm_model": "gpt-4o"
}
```

Fields:
- toxic: whether the message contains strong language or notable frustration  
- confidence: model confidence score (0.0–1.0)

## Project structure
ai-ticket-analyzer/
├── llm/
│   └── client.py        # LLM wrapper (calls OpenAI/Instructor)
├── models/
│   ├── request.py       # Pydantic model for incoming ticket
│   └── response.py      # Pydantic model for structured LLM output
├── main.py              # FastAPI server
├── .env                 # Environment variables (not committed)
├── requirements.txt     # Python dependencies
└── README.md