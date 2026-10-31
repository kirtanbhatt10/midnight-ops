# Contributing to midnight-ops

Thanks for your interest! midnight-ops is a **methodology, documentation, and reporting**
skill pack. Contributions that make authorized engagements more organized are very welcome.

## What we accept
- Methodology checklist improvements (PTES, OWASP WSTG/MASVS, NIST 800-115, MITRE ATT&CK).
- Template improvements (ROE, engagement notes, report).
- Additional **sanitized, fully fictional** example walkthroughs.
- Documentation, clarity, and accessibility fixes.

## What we will not accept
To stay within the project's purpose, we will close PRs that add:
- Exploit code, payloads, malware, or weaponized proof-of-concept.
- Operational, copy-paste attack commands tuned to live targets.
- Anything that lowers or removes the authorization gate.
- Real, non-sanitized engagement data (client names, hosts, credentials, evidence).

## Ground rules
1. Keep everything at the **planning / methodology / documentation** level.
2. Examples must be clearly fictional and use `.example` domains.
3. No secrets or client data in commits, issues, or PRs.
4. Cite the framework/standard section you align to.

## Workflow
1. Fork and branch from `main` (`feature/…` or `docs/…`).
2. Make focused changes; run the markdown lint (`.github/workflows/lint.yml` runs it in CI).
3. Open a PR describing the change and the framework reference.
4. A maintainer reviews for scope, accuracy, and the "no offensive tooling" rule.

By contributing you agree your work is released under the project's [MIT License](LICENSE).
