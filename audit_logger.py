import json
from datetime import datetime
import uuid

class AuditLogger:

    def __init__(self):
        self.file = "audit_logs.json"

    def log_event(self, user_id, role, action, module, status, details):
        log = {
            "log_id": str(uuid.uuid4()),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_id": user_id,
            "role": role,
            "action": action,
            "module": module,
            "status": status,
            "details": details
        }

        with open(self.file, "a") as f:
            f.write(json.dumps(log) + "\n")