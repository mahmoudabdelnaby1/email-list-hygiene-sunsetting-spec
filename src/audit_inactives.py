"""
Email Subscriber List Hygiene & Automated Sunsetting Sentinel
Audits newsletter lists to detect inactive subscribers and segment for sunsetting:
- Active: Opened / clicked within last 60 days
- At Risk: Inactive between 60 - 90 days (Target for Re-engagement / Winback)
- Sunset Warning: Inactive between 90 - 120 days (Final ultimatum campaign)
- Suppress / Prune: Inactive > 120 days (Automatic unsubscription to protect domain rep)
"""
import json
import argparse
from datetime import datetime
from typing import List, Dict, Any

def audit_subscriber_list(subscribers: List[Dict[str, Any]], reference_date_str: str = "2026-10-01") -> Dict[str, Any]:
    ref_date = datetime.strptime(reference_date_str, "%Y-%m-%d")
    
    segments = {
        "active": [],
        "at_risk": [],
        "sunset_warning": [],
        "suppress": []
    }
    
    for sub in subscribers:
        email = sub.get("email", "")
        last_activity = sub.get("last_activity_date")
        
        if not last_activity:
            segments["suppress"].append(email)
            continue
            
        act_date = datetime.strptime(last_activity, "%Y-%m-%d")
        days_inactive = (ref_date - act_date).days
        
        if days_inactive <= 60:
            segments["active"].append(email)
        elif 61 <= days_inactive <= 90:
            segments["at_risk"].append(email)
        elif 91 <= days_inactive <= 120:
            segments["sunset_warning"].append(email)
        else:
            segments["suppress"].append(email)
            
    total = len(subscribers)
    return {
        "total_subscribers": total,
        "reference_date": reference_date_str,
        "counts": {k: len(v) for k, v in segments.items()},
        "percentages": {k: round((len(v) / total) * 100.0, 1) if total > 0 else 0 for k, v in segments.items()},
        "suppression_candidates": segments["suppress"][:10],
        "winback_candidates": segments["at_risk"][:10]
    }

def main():
    sample = [
        {"email": "active1@brand.com", "last_activity_date": "2026-09-20"},
        {"email": "atrisk@brand.com", "last_activity_date": "2026-07-15"},
        {"email": "sunset@brand.com", "last_activity_date": "2026-06-25"},
        {"email": "dead@brand.com", "last_activity_date": "2025-12-01"}
    ]
    res = audit_subscriber_list(sample)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
