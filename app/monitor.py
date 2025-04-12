import json
import requests
from datetime import datetime, timezone
from app.aws import upload_result_to_s3

with open("app/urls.json") as f:
    config = json.load(f)
urls = config["urls"]

for url in urls:
    status_code = None
    status = "DOWN"

     # According to the assessment instructions:
    # A website is considered UP **only** if the HTTP response code is **200**
    # All other status codes (including 3xx, 4xx, 5xx) or exceptions = DOWN

    for attempt in range(3):
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
            if status_code == 200:
                status = "UP"
                break
        except Exception:
            continue

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "url": url,
        "status_code": status_code,
        "status": status
    }

    print(result)
    upload_result_to_s3(result)
