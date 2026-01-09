from pydantic import BaseModel, Field, field_validator
from typing import Literal

class TicketAnalyzer(BaseModel):
    schema_version: Literal["v1"] = "v1"
    ticket_id: str
    category: Literal["billing", "bug", "feature request", "other"]
    urgency: Literal["low", 'medium', "high"]
    toxic: bool

    summary: str = Field(description="One Sentence Summary of Customer Issue")
    confidence: float = Field(ge=0.0, le=1.0, description="Model Confidence on the Classification")

    @field_validator("summary")
    def no_emotional_language(cls, value):
        banned = ["stupid", "angry", "idiot"]
        if any(word in value.lower() for word in banned):
            raise ValueError("Summary Must Be Neutral") 
        return value
