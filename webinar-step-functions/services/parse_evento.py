import json
from services.audit import write_stepfunction_data

def parse_event_eventbridge(message):
    payload = message["detail"]
    write_stepfunction_data(message)
    return payload

