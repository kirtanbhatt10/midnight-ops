# PTES — Penetration Testing Execution Standard

Phase checklist aligned to the [PTES](http://www.pentest-standard.org/). Every item is a
planning or documentation step; the human operator performs all actions against
in-scope targets.

> Prerequisite: signed authorization and scope (`templates/rules-of-engagement.md`).

## 1. Pre-engagement interactions
- [ ] Authorizing party and signatory identified
- [ ] Signed contract / SOW / ROE on file
- [ ] In-scope and out-of-scope assets listed explicitly
- [ ] Testing window and permitted hours agreed
- [ ] Emergency contacts and stop-work procedure agreed
- [ ] Handling of sensitive data found during testing agreed
- [ ] Success criteria and engagement objectives written down
- [ ] Rules for social engineering / physical / DoS explicitly in or out
- [ ] Deliverables, format, and classification agreed

## 2. Intelligence gathering (planning)
- [ ] Objectives translated into a recon task list
- [ ] Passive OSINT sources identified (public records, DNS, certs, code repos)
- [ ] Organizational footprint mapped (domains, subdomains, IP ranges, ASNs)
- [ ] Technology and service inventory drafted from public data
- [ ] Human/role footprint noted only as relevant to authorized scope
- [ ] Every planned source confirmed to be within scope and legal

## 3. Threat modeling
- [ ] Assets ranked by business value
- [ ] Relevant threat actors / scenarios described
- [ ] Attack surface grouped (external, internal, app, cloud, identity)
- [ ] Objectives mapped to MITRE ATT&CK tactics (`methodology/mitre-attack.md`)
- [ ] Priority order for testing agreed with the operator

## 4. Vulnerability analysis (planning & checklists)
- [ ] Appropriate checklist(s) selected for each asset class
  - Web → `methodology/owasp-wstg.md`
  - Mobile → `methodology/owasp-masvs.md`
  - Network / host → `methodology/nist-800-115.md`
- [ ] Validation plan recorded (how each candidate finding will be confirmed)
- [ ] False-positive handling agreed

## 5. Exploitation (operator-executed)
> The assistant does **not** produce exploit code, payloads, or attack commands.
> It records what the operator attempted and observed.
- [ ] Each attempt tied to an in-scope objective and logged with timestamp
- [ ] Evidence captured per `templates/engagement-notes.md`
- [ ] Out-of-scope discoveries flagged, not pursued, and reported

## 6. Post-exploitation (operator-executed)
- [ ] Access level and reachable assets documented
- [ ] Business impact described in plain terms
- [ ] Sensitive data handling honored (no exfiltration beyond proof agreed in ROE)
- [ ] Cleanup / artifact-removal items tracked for the retest phase

## 7. Reporting
- [ ] Findings promoted from notes to structured records
- [ ] Severity scored with CVSS v3.1 / 4.0
- [ ] Executive summary written for non-technical readers
- [ ] Technical detail, reproduction, and remediation per finding
- [ ] Report assembled from `templates/report-template.md`
- [ ] Remediation guidance and retest checklist delivered

## Handoff
When a phase is complete, summarize status, open items, and the next phase's entry
criteria before moving on.
