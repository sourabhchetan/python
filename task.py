import json
from datetime import datetime

def parse_data_1(data):
    
    parsed = {
        "device": data["device"],
        "timestamp": data["timestamp"],
        "data": {
            "temperature": data["temperature"],
            "humidity": data["humidity"],
            "pressure": data["pressure"]
        }
    }
    return parsed

def parse_data_2(data):

    iso_timestamp = data["timestamp"]
    dt = datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%SZ")
    timestamp_ms = int(dt.timestamp() * 1000)
    
    parsed = {
        "device": data["device"],
        "timestamp": timestamp_ms,
        "data": {
            "temperature": data["data"]["temperature"],
            "humidity": data["data"]["humidity"],
            "pressure": data["data"]["pressure"]
        }
    }
    return parsed