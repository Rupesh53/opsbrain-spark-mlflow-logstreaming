import os
import time, json, random

os.makedirs("data/stream", exist_ok=True)   # ✅ ADD THIS

while True:
    log = {
        "timestamp": "2026-01-01",
        "status_code": random.choice([200, 500, 503]),
        "response_time": random.randint(50, 1200)
    }

    with open(f"data/stream/log_{int(time.time())}.json", "w") as f:
        json.dump(log, f)

    print("Sent:", log)
    time.sleep(2)