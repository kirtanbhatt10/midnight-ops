# Penetration Test Report — <Client> — <Engagement>

**Classification:** <Confidential / client-defined>
**Prepared for:** <Client org> · **Prepared by:** <Team>
**Engagement window:** <start> – <end> · **Report date:** <date>
**ROE reference:** <doc id> · **Report version:** <x.y>

---

## 1. Executive summary
Two or three paragraphs for a non-technical reader:
- What was tested, and why (objectives from the ROE).
- The overall security posture in plain language.
- The most important risks and the business impact if unaddressed.
- The headline recommendations.

### Findings at a glance
| Severity | Count |
|----------|-------|
| Critical | |
| High | |
| Medium | |
| Low | |
| Informational | |

## 2. Scope & methodology
- **In-scope assets:** (from the ROE)
- **Out of scope / limitations:** (and anything that constrained coverage)
- **Methodology:** frameworks followed — PTES, OWASP WSTG/MASVS, NIST SP 800-115,
  with findings mapped to MITRE ATT&CK.
- **Timeline:** key dates and phases.

## 3. Risk rating method
State the scale and how severity was derived (CVSS v3.1 / 4.0 base vectors, plus business
context). Define each severity label as used in this report.

## 4. Technical findings
> One subsection per finding, ordered by severity. Pull from the finding records in
> `templates/engagement-notes.md`.

### 4.1 FND-001 — <title>  ·  <Severity>
- **CVSS:** <vector> (<score>)
- **ATT&CK tactic(s):** <IDs>
- **Affected assets:** <in-scope assets>
- **Description:** what the issue is.
- **Evidence:** figures/log references (redacted as needed).
- **Reproduction:** factual, numbered steps.
- **Impact:** business impact.
- **Remediation:** prioritized, actionable fix(es).
- **References:** CWE / advisories / standards.

*(repeat for each finding)*

## 5. Strategic recommendations
Themes across findings (e.g., patch management, identity hygiene, monitoring gaps) and a
prioritized roadmap, separating quick wins from longer-term program improvements.

## 6. Remediation & retest plan
| Finding | Owner | Target date | Retest status |
|---------|-------|-------------|---------------|
| | | | |

## 7. Appendices
- A. Full asset / endpoint inventory tested
- B. Tools and versions used
- C. Evidence index (with storage/encryption notes)
- D. Glossary

---

*This report is confidential and intended solely for the named client. It documents the
security posture observed during a defined, authorized window and is not a guarantee of
security.*
