# OWASP WSTG — Web Security Testing Guide (checklist)

Planning checklist aligned to the [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/).
Use it to structure coverage of an **in-scope** web application. Items describe *what to
assess and document* — the operator performs any interaction with the target.

> Prerequisite: authorization + scope confirmed (`templates/rules-of-engagement.md`).
> Record status and evidence per item in `templates/engagement-notes.md`.

## WSTG-INFO — Information gathering
- [ ] Search-engine / archive exposure reviewed
- [ ] Web server, framework, and components fingerprinted (from in-scope responses)
- [ ] Application entry points and endpoints enumerated
- [ ] Application and architecture mapped (roles, trust boundaries, data flows)
- [ ] Error messages and metadata reviewed for information leakage

## WSTG-CONF — Configuration & deployment
- [ ] TLS configuration and certificate validity assessed
- [ ] HTTP security headers reviewed (HSTS, CSP, X-Content-Type-Options, etc.)
- [ ] Admin interfaces, default pages, and backups checked for exposure
- [ ] HTTP methods and cross-domain policies reviewed
- [ ] Cloud/storage bucket and metadata exposure checked (in scope only)

## WSTG-IDNT — Identity management
- [ ] Registration, provisioning, and account-enumeration behavior reviewed
- [ ] Role definitions and privilege boundaries documented

## WSTG-ATHN — Authentication
- [ ] Credentials transported over TLS only
- [ ] Lockout, throttling, and anti-automation behavior reviewed
- [ ] Password policy and reset flow assessed
- [ ] Remember-me, MFA, and session establishment reviewed

## WSTG-ATHZ — Authorization
- [ ] Directory traversal / file-include exposure reviewed
- [ ] Privilege escalation paths (vertical/horizontal) mapped
- [ ] Insecure direct object references (IDOR) checked across roles

## WSTG-SESS — Session management
- [ ] Cookie attributes reviewed (Secure, HttpOnly, SameSite)
- [ ] Session lifecycle assessed (fixation, timeout, logout, concurrency)
- [ ] CSRF protections reviewed

## WSTG-INPV — Input validation
- [ ] Reflected / stored / DOM injection surfaces catalogued
- [ ] SQL / NoSQL / command / LDAP injection surfaces catalogued
- [ ] SSRF, open-redirect, and header-injection surfaces catalogued
- [ ] Template injection and deserialization surfaces catalogued

## WSTG-ERRH / WSTG-CRYP — Error handling & cryptography
- [ ] Error and exception handling reviewed for leakage
- [ ] Data-at-rest and in-transit crypto reviewed against policy

## WSTG-BUSL — Business logic
- [ ] Workflow abuse and sequence-bypass scenarios modeled
- [ ] Limits, quotas, and anti-automation on sensitive functions reviewed

## WSTG-CLNT — Client-side
- [ ] DOM-based issues, postMessage, and client storage reviewed
- [ ] Third-party script and CORS exposure reviewed

## WSTG-APIT — API testing
- [ ] API inventory and auth model documented
- [ ] Object-level and function-level authorization reviewed (aligns to OWASP API Top 10)
- [ ] Rate limiting and mass-assignment exposure reviewed

## Closeout
- [ ] Each confirmed issue promoted to a finding record with CVSS and remediation
