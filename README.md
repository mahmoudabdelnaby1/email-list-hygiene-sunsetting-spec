# Email Subscriber List Hygiene & Automated Sunsetting Spec

> Boost your open rates and cut your ESP billing bills. Standardized email sunsetting policy and automated suppression workflow logic.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: TEMPLATE_FRAMEWORK](https://img.shields.io/badge/Format-TEMPLATE--FRAMEWORK-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source email list hygiene and sunsetting toolkit: 1) 3-stage sunset policy (Engagement Warning, Last-Chance Re-engagement, Automated Suppression), 2) example copy templates for the 'Goodbye / Are you still there?' re-engagement sequence, 3) Python audit script (`audit_inactives.py`) parsing subscriber activity exports, 4) Executive business case slide template justifying list pruning.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `docs/executive-business-case.md`
- `examples/clean_output.csv`
- `examples/scrubbed_contacts_sample.csv`
- `LICENSE`
- `playbooks/automated-sunset-policy.md`
- `policies/enterprise-sunsetting-policy.md`
- `README.md`
- `src/audit_inactives.py`
- `src/list_scrubber.py`
- `templates/last-chance-reengagement-copy.md`
- `templates/re-engagement-campaign-ar.md`
- `tests/test_audit.py`
- `tests/test_hygiene.py`
- `tests/test_scrubber.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/audit_inactives.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "automation",
  "repository": "email-list-hygiene-sunsetting-spec",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Inactivity Thresholds:** Automatically flags contacts with 0 opens and 0 clicks over 90, 120, or 180 days for progressive re-engagement and sunsetting.
- **Hard Bounce vs Soft Bounce Handling:** Automatically purges fatal hard bounces (code 5.X.X) while allowing transient soft bounces up to 3 attempts.
- **Spam Trap Avoidance:** Recovers sender domain reputation by suppressing unengaged subscribers before inbox providers convert dormant addresses into spam traps.

---

## 📚 Primary Documentation & Verifiable References

- [M3AAWG (Messaging Anti-Abuse Working Group) Best Practices](https://www.m3aawg.org/) - Global industry guidelines for subscriber list hygiene and sender authentication.
- [RFC 5321: Simple Mail Transfer Protocol (SMTP Bounce Processing)](https://datatracker.ietf.org/doc/html/rfc5321) - Technical specification for handling delivery failure notifications and bounce codes.
- [Validity / Return Path Sender Reputation Guide](https://www.validity.com/) - Best practices for maintaining high inbox placement and domain health.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
