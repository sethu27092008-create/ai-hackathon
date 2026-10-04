from pydantic import BaseModel, Field


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=20)
    style: str = "short"   # short, detailed, or bullet points


class SummaryResponse(BaseModel):
    summary: str