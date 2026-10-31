# Engagement Notes & Finding Records

Running log for an authorized engagement. Keep it factual and reproducible. Confirmed
issues are promoted into **Finding records** and then into the report
(`templates/report-template.md`).

> Prerequisite: ROE on file (`templates/rules-of-engagement.md`).

## Engagement header
| Field | Value |
|-------|-------|
| Engagement name | |
| Client | |
| ROE reference | |
| Window | |
| Operator(s) | |

## Activity log
> One line per meaningful action. The operator performs the action; this log records it.

| Timestamp (TZ) | Phase | In-scope target | Action / observation | Evidence ref |
|----------------|-------|-----------------|----------------------|--------------|
| | | | | |

## Scope guard log
> Anything encountered that is out of scope or unexpected. Do not pursue — record and report.

| Timestamp | What was encountered | Decision | Reported to |
|-----------|----------------------|----------|-------------|
| | | | |

---

## Finding record (copy one block per confirmed finding)

### FND-001 — <short title>
- **Status:** draft / confirmed / reported / remediated / retested
- **Asset:** <in-scope asset>
- **Severity:** <Critical/High/Medium/Low/Info> · **CVSS:** <vector + base score>
- **ATT&CK tactic(s):** <e.g., TA0001 Initial Access> (`methodology/mitre-attack.md`)
- **Summary:** one or two sentences on the issue and why it matters.
- **Affected scope:** endpoints / hosts / accounts in scope that are affected.
- **Reproduction:** numbered, factual steps sufficient for the client to reproduce.
  Describe *what was done and observed* — no weaponized payloads beyond what the ROE allows.
- **Evidence:** references to screenshots / logs / request-response captures (stored encrypted).
- **Impact:** concrete business impact in the client's terms.
- **Remediation:** specific, actionable fix and any compensating controls.
- **References:** CWE / vendor advisory / standard section.
- **Retest result:** (filled in at the retest phase)

---

> Evidence handling: store captures encrypted per the ROE; redact third-party or
> personal data not required to demonstrate the finding.
