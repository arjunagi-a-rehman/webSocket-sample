import json
import random
from datetime import datetime, timedelta

def random_time_pair():
    # Generate a random opening time in the format HH:MM
    open_hour = random.randint(0, 22)  # Ensuring at least 1 hour difference
    open_minute = random.choice([0, 15, 30, 45])
    
    close_hour = random.randint(open_hour + 1, 23)
    close_minute = random.choice([0, 15, 30, 45])
    
    if open_hour == 23 and open_minute > 0:
        close_hour = 23
        close_minute = 0  # Ensuring close time is valid when open time is close to midnight

    open_time = f"{open_hour:02}:{open_minute:02}"
    close_time = f"{close_hour:02}:{close_minute:02}"
    
    return open_time, close_time

def random_datetime():
    # Generate a random datetime in the past year
    now = datetime.utcnow()
    random_days = random.randint(0, 365)
    random_seconds = random.randint(0, 86400)  # seconds in a day
    random_date = now - timedelta(days=random_days, seconds=random_seconds)
    return random_date.strftime("%Y-%m-%dT%H:%M:%SZ")

def generate_random_payload(device_id, open_time=None, close_time=None):
    # Generate random times if not provided
    if open_time is None or close_time is None:
        open_time, close_time = random_time_pair()
    
    payload = {
        device_id: {
            "shutterRange": f"{random.randint(0, 100)}",
            "shutterClosed": random.choice([True, False]),
            "alertPriority": random.randint(0, 5),
            "vibrationIntensity": random.randint(0, 5),
            "batteryLevel": random.randint(0, 100),
            "isDocked": random.choice([True, False]),
            "signalStrength": random.randint(-100, 0),
            "shopOpenTime": open_time,
            "shopCloseTime": close_time,
            "lastAlert": random_datetime()
        }
    }
    return json.dumps(payload, indent=2)

