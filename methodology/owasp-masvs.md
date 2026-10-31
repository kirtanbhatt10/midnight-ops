# OWASP MASVS — Mobile App Security (checklist)

Planning checklist aligned to the [OWASP Mobile Application Security Verification
Standard](https://mas.owasp.org/MASVS/) and MASTG. Use it to structure coverage of an
**in-scope** mobile app. Items are assessment/documentation steps; the operator performs
any interaction with the app or device.

> Prerequisite: authorization + scope confirmed (`templates/rules-of-engagement.md`).

## MASVS-STORAGE — Data storage & privacy
- [ ] Sensitive data at rest inventoried (local DBs, files, keychains, logs)
- [ ] Data cached by the OS/keyboard/screenshots reviewed
- [ ] Backup inclusion/exclusion of sensitive data reviewed
- [ ] Data-minimization and retention reviewed against stated policy

## MASVS-CRYPTO — Cryptography
- [ ] Algorithms, key sizes, and modes reviewed against current guidance
- [ ] Key generation, storage, and lifecycle reviewed
- [ ] No hardcoded keys / secrets in the package

## MASVS-AUTH — Authentication & authorization
- [ ] Auth model and session handling documented
- [ ] Biometric / local-auth integration reviewed
- [ ] Server-side enforcement of authorization confirmed (not client-only)

## MASVS-NETWORK — Network communication
- [ ] TLS enforced for all sensitive traffic
- [ ] Certificate / public-key handling and pinning reviewed
- [ ] Endpoint inventory and trust reviewed

## MASVS-PLATFORM — Platform interaction
- [ ] Exported components, deep links, and IPC surfaces reviewed
- [ ] WebView configuration and bridges reviewed
- [ ] Permissions requested vs. required reviewed
- [ ] Sensitive data exposure via UI / notifications reviewed

## MASVS-CODE — Code quality & build
- [ ] Debuggable / backup flags and build config reviewed
- [ ] Third-party libraries and known-vulnerable dependencies inventoried
- [ ] Error handling and memory safety reviewed (as applicable)

## MASVS-RESILIENCE — Anti-tampering & resilience
- [ ] Root/jailbreak detection posture documented (as a defense-in-depth note)
- [ ] Anti-debugging / integrity controls documented
- [ ] Obfuscation posture documented
> Resilience controls are defense-in-depth; findings describe posture, not bypass steps.

## Closeout
- [ ] Each confirmed issue promoted to a finding record with CVSS and remediation
