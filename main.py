from fastapi import FastAPI, HTTPException
from models.request import CustomerTicket
from models.response import TicketAnalyzer
from llm.client import Analyze_throughLLM
from dotenv import load_dotenv
from pydantic import ValidationError
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

load_dotenv()

myApp = FastAPI()

@myApp.post("/analyze_ticket", response_model=TicketAnalyzer)
async def ticket_analysis(data: CustomerTicket):
    try:
        logger.info("Received ticket for analysis")

        analysis = Analyze_throughLLM(data)

        logger.info("Ticket analysis completed successfully")
        return analysis

    except ValidationError as e:
        logger.error("Schema validation failed")
        logger.error(e)
        raise HTTPException(status_code=422, detail=e.errors())

    except Exception as e:
        logger.critical("Unhandled error during ticket analysis")
        raise HTTPException(status_code=500, detail="Internal server error")


@myApp.get("/health")
def health_check():
    return {"status": "healthy"}
