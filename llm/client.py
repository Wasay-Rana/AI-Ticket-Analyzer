import instructor
from openai import OpenAI
from models.request import CustomerTicket
from models.response import TicketAnalyzer
from dotenv import load_dotenv

load_dotenv()
client = instructor.from_openai(OpenAI())

def Analyze_throughLLM(data: CustomerTicket) -> TicketAnalyzer:
    result = client.chat.completions.create(
        model="gpt-4o",
        response_model=TicketAnalyzer,
        max_retries=3,
        messages=[
            {"role": "system", "content": "You are a senior support ticket analyzer."},
            {"role": "user", "content": f"Analyze this ticket: {data.message}"}
        ],
    )

    result.ticket_id = data.ticket_id
    return result