import logging
import json
from datetime import datetime

class ResearchLogger:
    def __init__(self):
        self.logs = []
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("ResearchAnalyst")

    def info(self, agent: str, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] [{agent.upper()}] {message}"
        self.logger.info(log_entry)
        self.logs.append(log_entry)

    def error(self, agent: str, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] [{agent.upper()}] ERROR: {message}"
        self.logger.error(log_entry)
        self.logs.append(log_entry)

    def get_logs(self):
        return self.logs

logger = ResearchLogger()
