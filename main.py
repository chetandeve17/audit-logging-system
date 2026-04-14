from audit_logger import AuditLogger

logger = AuditLogger()

# Simulating real system actions

logger.log_event("CAND001", "Candidate", "Login", "Auth", "Success", "User logged in")

logger.log_event("CAND001", "Candidate", "Start Test", "Assessment", "Success", "Test started")

logger.log_event("CAND001", "Candidate", "Answer Q1", "Question Engine", "Success", "Answered Question 1")

logger.log_event("CAND001", "Candidate", "Skip Q2", "Question Engine", "Success", "Skipped Question 2")

logger.log_event("CAND001", "Candidate", "Submit Test", "Assessment", "Success", "Test submitted")

print("✅ Project-level logs created!")