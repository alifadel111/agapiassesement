from fastapi import FastAPI
from typing import Dict
from datetime import datetime, timedelta, timezone
from app.aws import get_results_for_website

app = FastAPI()

@app.get("/uptime/{website}")
def get_uptime_stats(website: str) -> Dict:
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=24)

    all_results = get_results_for_website(website)
    filtered = [
        r for r in all_results
        if datetime.fromisoformat(r["timestamp"]) >= cutoff
    ]

    total = len(filtered)
    up = sum(1 for r in filtered if r["status"] == "UP")
    down = total - up
    uptime_percentage = (up / total * 100) if total > 0 else 0

    return {
        "website": website,
        "total_checks": total,
        "up_checks": up,
        "down_checks": down,
        "uptime_percentage": round(uptime_percentage, 2)
    }
