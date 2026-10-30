# 🌒 midnight-ops

> **Authorization-first red-team & penetration-testing skill pack for AI coding agents — Claude and Codex.**

![License](https://img.shields.io/badge/license-MIT-000000.svg)
![Status](https://img.shields.io/badge/status-early%20development-orange.svg)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Claude](https://img.shields.io/badge/agent-Claude-6B4FBB.svg)
![Codex](https://img.shields.io/badge/agent-Codex-10A37F.svg)

---

> ### ⚠️ Authorized use only
> **midnight-ops** is built for licensed security professionals operating under **explicit, written permission**. Only use it against systems you own or have a signed contract/scope to test. Unauthorized access to computer systems is illegal — you are solely responsible for staying within scope and within the law.

---

## 🧭 Overview

**midnight-ops** packages structured offensive-security *methodology* into a reusable skill that AI coding agents (Claude via Agent Skills, and Codex) can load to behave like a disciplined red-team assistant.

Instead of ad-hoc prompting, it gives the agent a consistent playbook: scope and rules-of-engagement intake, reconnaissance planning, methodology checklists (aligned to **PTES**, **OWASP**, and **MITRE ATT&CK**), evidence capture, and clean report generation.

The focus is on **planning, methodology, documentation, and reporting** — the parts of an engagement where an organized assistant saves the most time — while a human operator stays in control of every action taken against a target.

## ✨ Features

- 📋 **Scope & ROE intake** — captures target scope, authorization, and rules of engagement *before* anything else.
- 🔭 **Recon & enumeration planning** — turns objectives into structured, methodology-backed task lists.
- 🧩 **Framework-aligned checklists** — PTES, OWASP WSTG / MASVS, NIST, and MITRE ATT&CK mappings.
- 📝 **Evidence & finding tracking** — consistent notes and reproducible finding records.
- 📊 **Report generation** — executive summary plus technical findings with CVSS severity and remediation guidance.
- 🤝 **Dual-agent** — ready for both Claude Agent Skills and Codex.

## 🤖 Supported agents

| Agent  | Integration              |
| ------ | ------------------------ |
| Claude | Agent Skill (`SKILL.md`) |
| Codex  | Skill / prompt profile   |

## 🗂️ Planned structure

```text
midnight-ops/
├─ skill/         # the skill definition (SKILL.md + resources)
├─ methodology/   # framework-aligned checklists & references
├─ templates/     # ROE, notes, and report templates
├─ examples/      # sanitized engagement walkthroughs
└─ README.md
```

## 🚀 Getting started

1. Clone the repository.
2. Load the skill into your agent (Claude Agent Skills, or Codex).
3. Start an engagement by providing your **written authorization and scope**.
4. Let the assistant build the plan — you execute, then feed results back in.

## 🛣️ Roadmap

- [ ] Publish `skill/SKILL.md`
- [ ] Methodology checklist library (PTES / OWASP / MITRE ATT&CK)
- [ ] Report & rules-of-engagement templates
- [ ] Sanitized example engagements
- [ ] Codex prompt profile

## ⚖️ Legal & ethical use

This project is intended **solely** for authorized security testing, education, and defensive research. Unauthorized access to computer systems is illegal in most jurisdictions. By using **midnight-ops** you agree that you are solely responsible for obtaining proper authorization and complying with all applicable laws. The maintainers assume no liability for misuse.

## 🤝 Contributing

Issues and pull requests are welcome — especially methodology references, checklist improvements, and report templates.

## 📄 License

Released under the [MIT License](LICENSE).
