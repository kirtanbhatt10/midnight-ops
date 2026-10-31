# Rules of Engagement (ROE) / Authorization Intake

> Fill this in **before** any target-specific planning. midnight-ops will not plan,
> enumerate, or draft anything tied to a live target until every required field below is
> complete and a signed authorization is referenced.

## 1. Authorization (required)
| Field | Value |
|-------|-------|
| Authorizing organization | |
| Signatory name & title | |
| Signatory email / phone | |
| Signed document reference (SOW / contract / letter) | |
| Document date | |
| Testing provider / team | |

> The signatory must have authority to permit testing of every in-scope asset. Third-party
> assets (shared hosting, SaaS, cloud tenants you don't own) need the provider's separate
> written permission.

## 2. Scope (required)
**In scope** — only what is listed here may be assessed:

| Asset | Type (domain / IP range / app / account) | Notes |
|-------|------------------------------------------|-------|
| | | |

**Out of scope** — explicitly excluded:

| Asset / activity | Reason |
|------------------|--------|
| | |

## 3. Time window (required)
| Field | Value |
|-------|-------|
| Start date/time | |
| End date/time | |
| Permitted testing hours | |
| Timezone | |
| Blackout periods | |

## 4. Engagement type & constraints
- [ ] External network  [ ] Internal network  [ ] Web app  [ ] Mobile app  [ ] Cloud  [ ] API
- [ ] Social engineering **permitted** (if checked, attach separate written consent)
- [ ] Physical testing **permitted** (if checked, attach separate written consent)
- [ ] Denial-of-service / load testing **permitted** (default: NOT permitted)
- Credentials provided: [ ] none (black box) [ ] low-priv [ ] admin (describe below)
- Testing source IP(s) to allowlist:

## 5. Handling & safety (required)
| Field | Value |
|-------|-------|
| Sensitive-data handling rule | (e.g., prove access, do not exfiltrate) |
| Primary emergency contact | |
| Secondary emergency contact | |
| Stop-work trigger & procedure | |
| Incident / breach-found procedure | |
| Evidence storage & encryption | |

## 6. Objectives & success criteria
- Business objectives of the test:
- "Crown jewel" assets / scenarios of greatest concern:
- Definition of success for this engagement:

## 7. Deliverables
| Field | Value |
|-------|-------|
| Report format | |
| Classification / distribution | |
| Due date | |
| Retest included? | |

---

### Sign-off
By signing, the authorizing party confirms they own or control all in-scope assets and
grant permission to test them within the window and constraints above.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Authorizing signatory | | | |
| Lead tester | | | |
