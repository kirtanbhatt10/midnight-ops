# Sanitized walkthrough — an authorized web engagement

A fully fictional, end-to-end example of how midnight-ops organizes an engagement. All
names, assets, and findings are invented. It shows the **flow and artifacts** — intake,
planning, tracking, reporting — not any attack technique or command.

> Client: *Acme Widgets Inc.* (fictional) · Target: `app.acme-widgets.example`
> Authorization: signed SOW #AW-2026-014 on file.

---

## Step 1 — Authorization gate

**Operator:** "Help me plan a web pentest of our staging app."

**Assistant:** confirms the hard gate before anything target-specific:

> Before I plan anything tied to a live target I need written authorization and scope.
> Here's the ROE intake to fill in first.

Operator provides the completed `rules-of-engagement.md`:
- Authorizing signatory: Dana Lee, VP Engineering, Acme Widgets.
- Signed SOW: #AW-2026-014, dated 2026-03-02.
- In scope: `app.acme-widgets.example`, `api.acme-widgets.example` (staging only).
- Out of scope: production, payment processor, all third-party SaaS.
- Window: 2026-03-10 to 2026-03-14, business hours IST.
- No DoS, no social engineering. Low-priv test account provided.

The assistant records the authorization and proceeds.

## Step 2 — Objectives → task list

Objectives from the ROE become a methodology-backed task list:
- Confirm authorization model and tenant isolation on the API.
- Assess session management and authorization boundaries in the app.
- Review configuration/headers and input-validation surfaces.

Each task is tagged to a WSTG section and a MITRE ATT&CK tactic for the report.

## Step 3 — Pick the checklist

The assistant loads `methodology/owasp-wstg.md` and presents the relevant sections
(WSTG-SESS, WSTG-ATHZ, WSTG-INPV, WSTG-CONF, WSTG-APIT) as a working checklist, scoped to
the two staging hosts only.

## Step 4 — Track as you go

As the operator works, the assistant maintains `engagement-notes.md`:

| Timestamp (IST) | Phase | Target | Observation | Evidence |
|-----------------|-------|--------|-------------|----------|
| 2026-03-10 10:15 | Authz | api.acme | Test user A could read order owned by user B | ev-012 |
| 2026-03-11 14:40 | Config | app.acme | Missing HSTS and weak CSP on authenticated pages | ev-021 |

The out-of-scope guard log captures that a linked production hostname appeared in a
response — noted, **not pursued**, and flagged for the report.

## Step 5 — Promote to findings

A confirmed issue becomes a finding record:

### FND-001 — IDOR on order lookup (API)
- **Severity:** High · **CVSS:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N (7.1)
- **ATT&CK:** TA0007 Discovery, TA0009 Collection
- **Summary:** An authenticated low-priv user can read other tenants' order records by
  changing the order identifier; server-side authorization is not enforced per object.
- **Impact:** Cross-tenant disclosure of customer order data in staging; same pattern
  would expose production data if present there.
- **Remediation:** Enforce per-object authorization server-side; add automated tests for
  object-level access across roles.
- **References:** CWE-639, OWASP API1:2023.

## Step 6 — Report

The assistant assembles `report-template.md`:
- Executive summary: one High (IDOR), two Medium (session + headers), posture overall
  "needs improvement in authorization testing coverage."
- Findings at a glance table, technical findings, strategic recommendations
  (object-level authZ testing in CI), and a remediation/retest plan.

## Step 7 — Remediation & retest

After the client reports fixes, the assistant produces a retest checklist from the open
findings and records retest results back into each finding record.

---

### What the assistant did *not* do
- It did not write exploit code, payloads, or copy-paste attack commands.
- It did not touch anything outside the two authorized staging hosts.
- It did not pursue the out-of-scope production hostname it noticed.

That discipline — authorization first, scope always visible, documentation over
improvisation — is the whole point of midnight-ops.
