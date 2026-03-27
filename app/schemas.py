from pydantic import BaseModel, Field


class TicketPreviewRequest(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=50)
    issue: str = Field(..., min_length=5, max_length=200)
    priority: int = Field(..., ge=1, le=3)


class TicketPreviewResponse(BaseModel):
    title: str
    priority: int
    is_urgent: bool
    summary: str
    category: str


class PriorityCheckRequest(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=50)
    priority: int = Field(..., ge=1, le=3)


class PriorityCheckResponse(BaseModel):
    customer_name: str
    priority: int
    is_urgent: bool


class TicketTagRequest(BaseModel):
    issue: str = Field(..., min_length=5, max_length=200)


class TicketTagResponse(BaseModel):
    issue: str
    tag: str


class TicketTriageRequest(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=50)
    issue: str = Field(..., min_length=5, max_length=200)
    priority: int = Field(..., ge=1, le=3)


class TicketTriageResponse(BaseModel):
    customer_name: str
    priority: int
    is_urgent: bool
    category: str
    recommended_queue: str


class EscalationCheckRequest(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=50)
    priority: int = Field(..., ge=1, le=3)
    issue: str = Field(..., min_length=5, max_length=200)


class EscalationCheckResponse(BaseModel):
    customer_name: str
    should_escalate: bool
    reason: str


class TicketSummaryResponse(BaseModel):
    customer_name: str
    summary: str
    category: str


class QueueCheckRequest(BaseModel):
    issue: str = Field(..., min_length=5, max_length=200)
    priority: int = Field(..., ge=1, le=3)


class QueueCheckResponse(BaseModel):
    category: str
    is_urgent: bool
    recommended_queue: str