import json
import requests
import datetime
from typing import Any, Dict, Optional


class TelegramLoggerClient:
    def __init__(self, base_url: str, x_id: str):
        self.base_url = base_url
        self.x_id = x_id

    def send_log(
        self,
        caller: str,
        level: str,
        message: str,
        error: Optional[str] = None,
        request_id: Optional[str] = None,
        trace_id: Optional[str] = None,
        span_id: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        payload = {
            "caller": caller,
            "time": datetime.datetime.now().isoformat(),
            "level": level,
            "message": message,
            "error": error,
            "requestID": request_id,
            "traceID": trace_id,
            "spanID": span_id,
            "data": data or {},
        }

        headers = {"Content-Type": "application/json", "X-ID": self.x_id}

        response = requests.post(
            self.base_url, headers=headers, data=json.dumps(payload)
        )
        response.raise_for_status()
        return response
