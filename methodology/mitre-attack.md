# MITRE ATT&CK — Tactic reference (threat modeling & reporting)

A reference for mapping objectives and findings to [MITRE ATT&CK](https://attack.mitre.org/)
tactics. Use it during threat modeling (PTES §3) and to tag findings in the report so
clients can connect results to their detection and defense program.

> This is a **mapping and communication aid**, not a how-to. It names tactics and the
> questions to answer; it does not provide techniques, procedures, or commands.

## Enterprise tactics (TA order)

| Tactic | ATT&CK ID | Question to answer in the report |
|--------|-----------|----------------------------------|
| Reconnaissance | TA0043 | What could an attacker learn before touching the target? |
| Resource development | TA0042 | What infrastructure/accounts would an attacker need? |
| Initial access | TA0001 | How could an attacker first get in, within scope? |
| Execution | TA0002 | Where could attacker-controlled code or actions run? |
| Persistence | TA0003 | How could access survive reboots/credential changes? |
| Privilege escalation | TA0004 | What paths raise privilege from the foothold? |
| Defense evasion | TA0005 | What detections/controls were weak or absent? |
| Credential access | TA0006 | Where are credentials exposed or weakly protected? |
| Discovery | TA0007 | What internal visibility does a foothold grant? |
| Lateral movement | TA0008 | How could an attacker move between assets? |
| Collection | TA0009 | What sensitive data is reachable? |
| Command and control | TA0011 | What egress/C2 paths are possible and detectable? |
| Exfiltration | TA0010 | How could data leave, and would it be seen? |
| Impact | TA0040 | What business impact (availability/integrity) is at risk? |

## How to use in an engagement
1. **Threat modeling.** For each prioritized objective, note the relevant tactics and the
   defensive question each raises.
2. **Finding tags.** Tag each finding with the tactic(s) it enables so the client sees
   coverage gaps across the kill chain — not just isolated bugs.
3. **Detection narrative.** In the report, pair each tactic with "would current monitoring
   have caught this?" to turn findings into defensive value.

## Related resources
- ATT&CK Navigator — for building a coverage heatmap from the finding tags.
- D3FEND — to pair offensive findings with defensive countermeasures in remediation.
