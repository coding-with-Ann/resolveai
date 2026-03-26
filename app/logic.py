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
    


def normalize_customer_name(customer_name: str) -> str:
    return customer_name.strip().title()



def is_high_priority(priority: int) -> bool:
    return priority in [1, 2]