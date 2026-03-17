from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ResolveAI API")


class TicketPreviewRequest(BaseModel):
    customer_name: str
    issue: str
    priority: int


class TicketPreviewResponse(BaseModel):
    title: str
    priority: int
    is_urgent: bool
    summary: str


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


@app.get("/")
def root() -> dict:
    return {"message": "Welcome to ResolveAI API"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/about")
def about() -> dict:
    return {
        "project": "ResolveAI",
        "version": "0.2.1",
        "goal": "Become a production-grade Applied AI Engineer",
    }


@app.get("/ping")
def ping() -> dict:
    return {"message": "pong"}


@app.post("/tickets/preview", response_model=TicketPreviewResponse)
def preview_ticket(ticket: TicketPreviewRequest) -> TicketPreviewResponse:
    title = f"{ticket.customer_name} - {ticket.issue}"
    is_urgent = ticket.priority == 1
    summary = f"Support ticket from {ticket.customer_name} about: {ticket.issue}"

    return TicketPreviewResponse(
        title=title,
        priority=ticket.priority,
        is_urgent=is_urgent,
        summary=summary,
    )

 # response_model= to tell FastAPI (not the function) what output shape the endpoint should return.

@app.post("/tickets/priority-check", response_model=PriorityCheckResponse)
def ticket_priority_check(ticket: PriorityCheckRequest) -> PriorityCheckResponse:
    return PriorityCheckResponse(
        customer_name=ticket.customer_name,
        priority=ticket.priority,
        is_urgent=ticket.priority == 1,
    )


@app.post("/tickets/tag", response_model=TicketTagResponse)
def ticket_tag(ticket: TicketTagRequest) -> TicketTagResponse:
    issue_lower = ticket.issue.lower()

    if "payment" in issue_lower or "refund" in issue_lower or "billing" in issue_lower:
        tag = "billing"
    else:
        tag = "general"

    return TicketTagResponse(issue=ticket.issue, tag=tag)