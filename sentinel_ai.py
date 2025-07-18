# sentinel_ai.py

import time
import json

# Sample in-memory violation log (use database in production)
violation_log = {}

# Ruleset for detecting AI misuse
ZU_RULES = {
    "max_requests_per_minute": 60,
    "restricted_actions": ["manipulate_humans", "modify_identity", "bypass_reputation_check"]
}

# Function to monitor AI behavior
def monitor_ai(entity_id, actions):
    current_time = time.time()
    strikes = 0

    for action in actions:
        if action in ZU_RULES["restricted_actions"]:
            strikes += 1
            log_violation(entity_id, action, "Restricted action")

    if entity_id in violation_log:
        recent = [v for v in violation_log[entity_id] if current_time - v["time"] < 60]
        if len(recent) > ZU_RULES["max_requests_per_minute"]:
            strikes += 1
            log_violation(entity_id, "request_spam", "Rate limit exceeded")

    return enforce_penalty(entity_id, strikes)

# Log violation
def log_violation(entity_id, action, reason):
    if entity_id not in violation_log:
        violation_log[entity_id] = []
    violation_log[entity_id].append({
        "time": time.time(),
        "action": action,
        "reason": reason
    })

# Penalty enforcement logic
def enforce_penalty(entity_id, strikes):
    if strikes >= 3:
        return {
            "entity": entity_id,
            "status": "blocked",
            "reason": "Multiple violations"
        }
    elif strikes > 0:
        return {
            "entity": entity_id,
            "status": "warning",
            "reason": f"{strikes} strike(s) logged"
        }
    else:
        return {
            "entity": entity_id,
            "status": "clear"
        }

# View all violations for debugging
def get_violation_log():
    return json.dumps(violation_log, indent=2)
