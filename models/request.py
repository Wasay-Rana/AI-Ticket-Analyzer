from pydantic import BaseModel

class CustomerTicket(BaseModel):
    ticket_id: str
    message: str