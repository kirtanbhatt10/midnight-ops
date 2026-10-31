# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-10-31
First production-ready release: a complete, authorization-first methodology and reporting
skill pack for Claude and Codex.

### Added
- `skill/SKILL.md` — canonical Claude Agent Skill definition with the authorization gate.
- `AGENTS.md` — Codex / agent prompt profile mirroring the skill.
- Methodology library: `ptes.md`, `owasp-wstg.md`, `owasp-masvs.md`, `nist-800-115.md`,
  `mitre-attack.md`.
- Templates: `rules-of-engagement.md`, `engagement-notes.md`, `report-template.md`.
- `examples/sanitized-walkthrough.md` — end-to-end fictional engagement example.
- Repo hygiene: `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.gitignore`,
  and a Markdown lint CI workflow.
- README demo video and refreshed roadmap/structure.

### Notes
- Scope remains strictly planning / methodology / documentation / reporting. No exploit
  code, payloads, or operational attack commands are included.

## [0.1.0] — 2026
### Added
- Initial README and project scaffolding.
