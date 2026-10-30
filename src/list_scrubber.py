#!/usr/bin/env python3
import csv
import sys

def scrub_list(in_csv, out_csv):
    scrubbed = []
    with open(in_csv, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            inactive_days = int(r.get("days_inactive") or 0)
            if inactive_days < 90:
                scrubbed.append(r)

    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["email", "days_inactive"])
        writer.writeheader()
        writer.writerows(scrubbed)
    return len(scrubbed)

if __name__ == "__main__":
    c = scrub_list(sys.argv[1], sys.argv[2])
    print(f"Retained {c} active subscribers.")
