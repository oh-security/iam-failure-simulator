import boto3
from typing import Dict, List


def lookup_events(days_back: int = 30) -> List[Dict]:
    ct = boto3.client("cloudtrail")
    events: List[Dict] = []

    resp = ct.lookup_events(MaxResults=50)
    events.extend(resp.get("Events", []))

    return events
