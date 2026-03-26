from fastapi import APIRouter

from app.logic import (
    build_ticket_summary,
    build_ticket_title,
    check_escalation,
    classify_issue,
    get_escalation_reason,
    get_recommended_queue,
    is_urgent_priority,
)
from app.schemas import (
    EscalationCheckRequest,
    EscalationCheckResponse,
    PriorityCheckRequest,
    PriorityCheckResponse,
    TicketPreviewRequest,
    TicketPreviewResponse,
    TicketTagRequest,
    TicketTagResponse,
    TicketTriageRequest,
    TicketTriageResponse,
    QueueCheckRequest, 
    QueueCheckResponse
)

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("/preview", response_model=TicketPreviewResponse)
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


@router.post("/priority-check", response_model=PriorityCheckResponse)
def ticket_priority_check(ticket: PriorityCheckRequest) -> PriorityCheckResponse:
    return PriorityCheckResponse(
        customer_name=ticket.customer_name,
        priority=ticket.priority,
        is_urgent=is_urgent_priority(ticket.priority),
    )


@router.post("/tag", response_model=TicketTagResponse)
def ticket_tag(ticket: TicketTagRequest) -> TicketTagResponse:
    return TicketTagResponse(
        issue=ticket.issue,
        tag=classify_issue(ticket.issue),
    )


@router.post("/triage", response_model=TicketTriageResponse)
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


@router.post("/escalation-check", response_model=EscalationCheckResponse)
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


@router.post("queue-check", response_model=QueueCheckResponse)
def queue_check(ticket: QueueCheckRequest)-> QueueCheckResponse:
    return QueueCheckResponse(category=classify_issue(ticket.issue), is_urgent=is_urgent_priority(ticket.priority))
