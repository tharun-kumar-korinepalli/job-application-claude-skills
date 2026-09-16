#!/usr/bin/env python3
"""Keep a simple CSV tracker of job applications. Standard library only.

Usage:
    python job_tracker.py add --file tracker.csv --company "Acme GmbH" --role "ML Engineer" \
        --status applied --source stepstone --contact "Anna Weber" --next "follow up" --next-date 2026-10-07
    python job_tracker.py update --file tracker.csv --company "Acme GmbH" --role "ML Engineer" \
        --status interview --next "prep STAR stories" --next-date 2026-10-01
    python job_tracker.py list --file tracker.csv
    python job_tracker.py due --file tracker.csv        # next actions due today or overdue

Statuses: found, applied, screen, interview, offer, rejected, withdrawn, ghosted
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

FIELDS = [
    "company", "role", "location", "source", "url", "date_applied", "status",
    "contact", "salary_asked", "next_action", "next_action_date", "last_update", "notes",
]
STATUSES = {"found", "applied", "screen", "interview", "offer", "rejected", "withdrawn", "ghosted"}


def load(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return [dict(r) for r in csv.DictReader(f)]


def save(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


def key(r: dict[str, str]) -> tuple[str, str]:
    return r.get("company", "").strip().lower(), r.get("role", "").strip().lower()


def today() -> str:
    return dt.date.today().isoformat()


def cmd_add(a, rows):
    if a.status and a.status not in STATUSES:
        sys.exit(f"status must be one of {sorted(STATUSES)}")
    for r in rows:
        if key(r) == (a.company.lower(), a.role.lower()):
            sys.exit("already tracked; use `update`")
    rows.append({
        "company": a.company, "role": a.role, "location": a.location or "",
        "source": a.source or "", "url": a.url or "",
        "date_applied": a.date or (today() if (a.status or "applied") == "applied" else ""),
        "status": a.status or "applied", "contact": a.contact or "",
        "salary_asked": a.salary or "", "next_action": a.next or "",
        "next_action_date": a.next_date or "", "last_update": today(), "notes": a.notes or "",
    })
    print(f"added {a.company} / {a.role}")


def cmd_update(a, rows):
    if a.status and a.status not in STATUSES:
        sys.exit(f"status must be one of {sorted(STATUSES)}")
    for r in rows:
        if key(r) == (a.company.lower(), a.role.lower()):
            for field, val in [
                ("status", a.status), ("contact", a.contact), ("next_action", a.next),
                ("next_action_date", a.next_date), ("location", a.location), ("source", a.source),
                ("url", a.url), ("salary_asked", a.salary),
            ]:
                if val:
                    r[field] = val
            if a.notes:
                r["notes"] = (r.get("notes", "") + f" | {today()}: {a.notes}").strip(" |")
            r["last_update"] = today()
            print(f"updated {a.company} / {a.role}")
            return
    sys.exit("not found; use `add`")


def cmd_list(a, rows):
    if not rows:
        print("tracker is empty")
        return
    rows = sorted(rows, key=lambda r: (r.get("status", ""), r.get("company", "")))
    print(f"{'company':28} {'role':30} {'status':10} {'applied':10} {'next':26} {'due':10}")
    for r in rows:
        print(f"{r['company'][:28]:28} {r['role'][:30]:30} {r['status']:10} {r['date_applied']:10} "
              f"{r['next_action'][:26]:26} {r['next_action_date']:10}")


def cmd_due(a, rows):
    t = today()
    due = [r for r in rows if r.get("next_action_date") and r["next_action_date"] <= t
           and r.get("status") not in {"rejected", "withdrawn"}]
    if not due:
        print("nothing due")
        return
    for r in sorted(due, key=lambda r: r["next_action_date"]):
        print(f"{r['next_action_date']}  {r['company']} / {r['role']}: {r['next_action']}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["add", "update", "list", "due"])
    ap.add_argument("--file", default="job_tracker.csv")
    for opt in ["company", "role", "location", "source", "url", "date", "status", "contact",
                "salary", "next", "next-date", "notes"]:
        ap.add_argument(f"--{opt}")
    a = ap.parse_args()
    a.next_date = getattr(a, "next_date", None)

    path = Path(a.file)
    rows = load(path)
    if a.cmd in {"add", "update"} and not (a.company and a.role):
        sys.exit("--company and --role are required")
    {"add": cmd_add, "update": cmd_update, "list": cmd_list, "due": cmd_due}[a.cmd](a, rows)
    if a.cmd in {"add", "update"}:
        save(path, rows)


if __name__ == "__main__":
    main()
