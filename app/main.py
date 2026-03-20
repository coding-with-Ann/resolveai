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


def is_urgent_priority(priority: int) -> bool:
    return priority == 1


def classify_issue(issue: str) -> str:
    issue_lower = issue.lower()

    if "payment" in issue_lower or "refund" in issue_lower or "billing" in issue_lower:
        return "billing"
    elif "bug" in issue_lower or "error" in issue_lower or "crash" in issue_lower or "timeout" in issue_lower:
        return "technical"
    elif "login" in issue_lower or "password" in issue_lower or "account" in issue_lower:
        return "account"
    else:
        return "general"


def build_ticket_title(customer_name: str, issue: str) -> str:
    return f"{customer_name} - {issue}"


def build_ticket_summary(customer_name: str, issue: str) -> str:
    return f"Support ticket from {customer_name} about: {issue}"


def get_recommended_queue(category: str, is_urgent: bool) -> str:
    if is_urgent and category == "billing":
        return "priority_billing"
    elif is_urgent and category == "account":
        return "priority_account"
    elif is_urgent:
        return "priority_general"
    elif category == "billing":
        return "billing"
    elif category == "account":
        return "account_support"
    elif category == "technical":
        return "technical_support"
    else:
        return "general_support"


def check_escalation(priority_satisfied: bool, issue_type: str) -> bool:
    if priority_satisfied or issue_type == "technical":
        return True
    else:
        return False


def get_escalation_reason(priority_satisfied: bool, issue_type: str) -> str:
    if priority_satisfied:
        return "Urgent priority requires escalation"
    elif issue_type == "technical":
        return "Technical issue requires escalation"
    else:
        return "No escalation needed"


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
        "version": "0.3.0",
        "goal": "Become a production-grade Applied AI Engineer",
    }


@app.get("/ping")
def ping() -> dict:
    return {"message": "pong"}


@app.post("/tickets/preview", response_model=TicketPreviewResponse)
def preview_ticket(ticket: TicketPreviewRequest) -> TicketPreviewResponse:
    title = build_ticket_title(ticket.customer_name, ticket.issue)
    is_urgent = is_urgent_priority(ticket.priority)
    summary = build_ticket_summary(ticket.customer_name, ticket.issue)
    category = classify_issue(ticket.issue)

    return TicketPreviewResponse(
        title=title,
        priority=ticket.priority,
        is_urgent=is_urgent,
        summary=summary,
        category=category,
    )


@app.post("/tickets/priority-check", response_model=PriorityCheckResponse)
def ticket_priority_check(ticket: PriorityCheckRequest) -> PriorityCheckResponse:
    return PriorityCheckResponse(
        customer_name=ticket.customer_name,
        priority=ticket.priority,
        is_urgent=is_urgent_priority(ticket.priority),
    )


@app.post("/tickets/tag", response_model=TicketTagResponse)
def ticket_tag(ticket: TicketTagRequest) -> TicketTagResponse:
    return TicketTagResponse(
        issue=ticket.issue,
        tag=classify_issue(ticket.issue),
    )


@app.post("/tickets/triage", response_model=TicketTriageResponse)
def ticket_triage(ticket: TicketTriageRequest) -> TicketTriageResponse:
    is_urgent = is_urgent_priority(ticket.priority)
    category = classify_issue(ticket.issue)
    recommended_queue = get_recommended_queue(category, is_urgent)

    return TicketTriageResponse(
        customer_name=ticket.customer_name,
        priority=ticket.priority,
        is_urgent=is_urgent,
        category=category,
        recommended_queue=recommended_queue,
    )


@app.post("/tickets/escalation-check", response_model=EscalationCheckResponse)
def escalation(ticket: EscalationCheckRequest) -> EscalationCheckResponse:
    is_urgent = is_urgent_priority(ticket.priority)
    issue_type = classify_issue(ticket.issue)

    should_escalate = check_escalation(is_urgent, issue_type)
    reason = get_escalation_reason(is_urgent, issue_type)

    return EscalationCheckResponse(
        customer_name=ticket.customer_name,
        should_escalate=should_escalate,
        reason=reason,
    )




