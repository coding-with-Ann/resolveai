from pydantic import BaseModel


class TicketPreviewRequest(BaseModel):
    customer_name: str
    issue: str
    priority: int


class TicketPreviewResponse(BaseModel):
    title: str
    priority: int
    is_urgent: bool
    summary: str
    category: str


class PriorityCheckRequest(BaseModel):
    customer_name: str
    priority: int


class PriorityCheckResponse(BaseModel):
    customer_name: str
    priority: int
    is_urgent: bool


class TicketTagRequest(BaseModel):
    issue: str


class TicketTagResponse(BaseModel):
    issue: str
    tag: str


class TicketTriageRequest(BaseModel):
    customer_name: str
    issue: str
    priority: int


class TicketTriageResponse(BaseModel):
    customer_name: str
    priority: int
    is_urgent: bool
    category: str
    recommended_queue: str


class EscalationCheckRequest(BaseModel):
    customer_name: str
    priority: int
    issue: str


class EscalationCheckResponse(BaseModel):
    customer_name: str
    should_escalate: bool
    reason: str



class TicketSummaryResponse(BaseModel):
    customer_name: str
    summary: str
    category: str


class QueueCheckRequest(BaseModel):
    issue: str 
    priority: int 

class QueueCheckResponse(BaseModel):
    category: str 
    is_urgent: bool 
    recommended_queue: str 
