# Recovery and Compromise

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines recovery, loss, theft, compromise, suspension, and re-issuance handling without rebuilding central presentation tracking.

Recovery and compromise handling MUST preserve the separation between:
- issuer trust state
- root credential state
- wallet compromise state

Ordinary verification MUST NOT depend on recovery infrastructure or presentation logs.

## 2. State domains
### 2.1 Issuer trust state
Issuer trust state MUST use one of:
- `trusted`
- `under_review`
- `suspended`
- `withdrawn`
- `compromised`
- `retired`

Issuer trust state MUST be published through trust-registry or governance channels and MUST NOT depend on holder presentation histories.

### 2.2 Root credential state
Root credential state MUST use one of:
- `active`
- `expiring`
- `suspended`
- `revoked`
- `reissued`
- `expired`

Root credential state MAY be represented through batched, cacheable, relayable, or otherwise non-unique status mechanisms.

Root credential state MUST NOT require token-specific live issuer callbacks in the normal verifier flow.

### 2.3 Wallet compromise state
Wallet compromise state MUST use one of:
- `normal`
- `lost_unconfirmed`
- `lost_confirmed`
- `compromised`
- `recovered`
- `retired`

Wallet compromise state MUST be managed without creating a holder activity log visible to issuers or verifiers.

## 3. Actor roles and permissions
Recovery and compromise handling MUST define who is allowed to request, approve, publish, and consume each state change.

| Actor | Responsibilities | May request | May approve or confirm | May publish state | Must not do |
| --- | --- | --- | --- | --- | --- |
| Holder | Reports loss, theft, suspected compromise, mistaken suspension, and device replacement. | wallet loss, wallet theft, recovery, appeal | possession of replacement wallet during rebind | no ecosystem state directly | claim issuer compromise, update trust state, or force verifier acceptance |
| Wallet | Protects root credential material, detects local compromise signals, performs local backup restore, and enforces proof refusal. | wallet compromise review, rebind, re-issuance | local device possession and holder consent | local wallet compromise state only unless governed as a status publisher | disclose root credential or recovery history in normal flow |
| Issuer | Issues, suspends, revokes, reissues, and expires root credentials under policy. | root credential suspension or revocation | root credential compromise, successful re-proofing, re-issuance | root credential state directly or through a governed status publisher | receive ordinary presentation history |
| Recovery authority | Operates recovery checks where the issuer delegates recovery or where ecosystem policy separates recovery from issuance. | recovery review, temporary suspension | recovery eligibility and mistaken-suspension findings within delegated scope | recovery outcome to issuer or status publisher | become a verifier-visible identity history service |
| Trust registry or governance authority | Maintains issuer trust state and trust anchors. | issuer review, suspension, withdrawal, reinstatement | issuer compromise, issuer reinstatement, trust withdrawal | issuer trust state | store holder data, root credential identifiers, or presentation logs |
| Status publisher or relay | Publishes signed, batched, cacheable, relayable, or otherwise non-unique state evidence. | no independent state change | no independent state change | issuer trust, root credential, or wallet compromise state as delegated | create token-specific live callbacks or verifier-visible holder trails |
| Verifier | Consumes trust and status evidence before accepting a proof. | verifier-side fraud report to governance or issuer | no direct suspension, compromise confirmation, or re-issuance | no ecosystem state | infer or display detailed compromise reason from proof failure |
| Auditor or certifier | Reviews conformance, appeal handling, abuse thresholds, and state-change evidence. | governance review | certification or non-conformance finding | audit findings, not holder status | receive raw proof payloads or ordinary presentation logs by default |

Only the issuer, a delegated recovery authority, or a governance authority MAY approve suspension or revocation of a holder's root credential. Only the trust registry or governance authority MAY update issuer trust state. Verifiers MUST NOT be able to suspend a holder, confirm wallet compromise, or trigger re-issuance without an issuer or governance review path.

## 4. State transition table
State transitions MUST be auditable without exposing ordinary presentation histories.

| Domain | From | To | Trigger | Requester | Approver | Publisher | Verifier behavior after propagation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Issuer trust | `trusted` | `under_review` | credible issuer incident or governance review | regulator, auditor, verifier report, issuer self-report | trust registry or governance authority | trust registry | MAY soft-fail or require fresher trust evidence according to policy |
| Issuer trust | `under_review` | `suspended` | unresolved risk requiring temporary stop | trust registry or governance authority | trust registry or governance authority | trust registry | MUST reject where policy treats suspension as blocking |
| Issuer trust | `under_review` or `suspended` | `trusted` | review clears issuer | issuer or governance authority | trust registry or governance authority | trust registry | MAY accept again once proof and freshness requirements are satisfied |
| Issuer trust | `trusted`, `under_review`, or `suspended` | `withdrawn` | trust accreditation removed | governance authority | trust registry or governance authority | trust registry | MUST reject affected derived proofs |
| Issuer trust | any active trust state | `compromised` | issuer signing, issuance, or registry integrity compromise | issuer, auditor, regulator, governance authority | trust registry or governance authority | trust registry | MUST reject affected derived proofs unless a governed exception explicitly permits temporary handling |
| Issuer trust | `trusted` or `withdrawn` | `retired` | issuer exits without suspected compromise | issuer or governance authority | trust registry or governance authority | trust registry | MUST apply retirement policy and credential expiry rules |
| Root credential | `active` | `expiring` | planned renewal window | issuer or wallet | issuer | issuer or status publisher | MAY accept if still within validity and freshness limits |
| Root credential | `active` or `expiring` | `suspended` | lost device, appeal review, suspected misuse, or temporary risk | holder, wallet, issuer, recovery authority | issuer or delegated recovery authority | issuer or status publisher | SHOULD soft-fail as temporarily unavailable without exposing reason |
| Root credential | `suspended` | `active` | mistaken suspension resolved or lost device recovered before compromise | holder, wallet, recovery authority | issuer or delegated recovery authority | issuer or status publisher | MAY accept after fresh status evidence |
| Root credential | `active`, `expiring`, or `suspended` | `revoked` | confirmed compromise, confirmed theft, fraud, or issuer policy requirement | holder, wallet, issuer, recovery authority | issuer | issuer or status publisher | MUST reject affected derived proofs |
| Root credential | `active`, `expiring`, `suspended`, or `revoked` | `reissued` | replacement credential issued after rebind or re-proofing | holder, wallet, issuer, recovery authority | issuer | issuer or status publisher | MUST reject old credential lineage where marked non-current |
| Root credential | any non-revoked state | `expired` | validity period ends | issuer policy | issuer policy | issuer or status publisher | MUST reject unless a governed grace rule explicitly allows retry-only handling |
| Wallet compromise | `normal` | `lost_unconfirmed` | holder reports loss but theft or misuse is not confirmed | holder or wallet | wallet locally, issuer if root suspension is requested | wallet locally; status publisher only if delegated | MAY treat as freshness-sensitive; SHOULD avoid reason disclosure |
| Wallet compromise | `lost_unconfirmed` | `lost_confirmed` | loss confirmed and original device remains unavailable | holder, recovery authority, wallet | recovery authority or issuer | status publisher if delegated | SHOULD reject or soft-fail according to root credential state |
| Wallet compromise | `normal`, `lost_unconfirmed`, or `lost_confirmed` | `compromised` | theft, key extraction, malware, or unauthorized proof generation confirmed | holder, wallet, issuer, recovery authority | issuer or delegated recovery authority | status publisher if delegated | MUST reject once relevant state has propagated |
| Wallet compromise | `lost_unconfirmed`, `lost_confirmed`, or `compromised` | `recovered` | replacement wallet is rebound and old credential is suspended, revoked, expired, or reissued | holder and wallet | issuer or delegated recovery authority | status publisher if delegated | MAY accept only replacement credential proofs |
| Wallet compromise | any state | `retired` | wallet instance decommissioned | holder or wallet | wallet locally; issuer if root state is affected | local or delegated status publisher | MUST reject retired wallet-bound proofs where detectable |

## 5. Propagation and stale-state behavior
State propagation MUST be designed as a privacy-preserving validity channel, not as a presentation callback.

Conformant implementations MUST define:
- the publication channel for each state domain
- the signature or integrity mechanism for state evidence
- the maximum status age a verifier may accept
- the maximum trust-registry snapshot age a verifier may accept
- the behavior when state evidence is unavailable, stale, contradictory, or newer than local verifier policy

Issuer trust state SHOULD propagate through signed trust-registry snapshots or equivalent governance feeds. Root credential and wallet compromise state SHOULD propagate through signed batched status lists, cacheable accumulators, relayable status proofs, short-lived credentials, or another non-unique mechanism.

The following stale-state rules apply:
- A verifier MUST reject, retry, or soft-fail when required status evidence is older than the profile or policy maximum.
- A verifier MUST NOT call the issuer with a token-specific or holder-specific status request in the normal flow.
- A verifier MAY use cached positive state only until the declared freshness window expires.
- A verifier MUST treat signed negative state with equal or newer freshness as overriding older positive state.
- A wallet SHOULD refresh locally known state before presenting where freshness failure is predictable.
- A wallet SHOULD present recovery or rebind UX to the holder when proof failure is likely due to known local recovery state.

Temporary grace behavior MAY be used only for stale, unavailable, or delayed state where there is no confirmed compromise, revocation, issuer withdrawal, or issuer compromise. Grace behavior MUST be explicit in policy, time-limited, auditable, and no broader than necessary. Grace behavior SHOULD prefer retry, deferred completion, or lower-risk access over accepting a proof as fully valid.

Confirmed `compromised`, `revoked`, `withdrawn`, and issuer `compromised` states MUST NOT receive normal-flow grace acceptance after the verifier has fresh evidence of the state.

## 6. Backup and recovery architecture choices
Implementations MUST choose and document at least one recovery architecture. Multiple choices MAY coexist if the wallet clearly separates their privacy and assurance properties.

| Recovery choice | Description | Privacy and security constraints | Profile guidance |
| --- | --- | --- | --- |
| Encrypted backup | Root credential material or recovery material is backed up under holder-controlled encryption. | Backup metadata MUST NOT reveal presentation history; restore MUST require holder consent and device rebind; backup provider MUST NOT learn root secrets. | `Profile R` MAY use it with strong encryption and governance controls. `Profile P` SHOULD avoid portable correlation material or use designs that preserve unlinkability after restore. |
| Hardware-bound recovery | Credential authority remains bound to secure hardware, passkeys, platform keys, or equivalent device-bound keys. | Recovery MUST rotate or rebind keys when the old device is unavailable; old wallet proofs MUST fail after state propagation. | Preferred for high-assurance `Profile R`; compatible with `Profile P` if verifier-stable handles are not introduced. |
| Re-proofing | Holder repeats evidence checking before a new root credential is issued. | Re-proofing MUST NOT disclose old presentation history; issuer retention remains bounded by issuance policy. | Acceptable for both profiles; often the cleanest privacy fallback. |
| Re-issuance only | Issuer issues a replacement after governed recovery checks without restoring old credential material. | Old root credential SHOULD remain `revoked`, `suspended`, or `expired`; new credential MUST NOT carry verifier-visible links to the old credential. | Acceptable baseline for both profiles; `Profile P` SHOULD prefer it over stateful recovery where feasible. |

Normal-flow verifiers MUST NOT learn which recovery architecture was used.

## 7. Lost-device flow
When a holder reports a lost device, the system SHOULD first support local recovery or backup restoration where available.

If local recovery is unavailable, the system MAY use controlled re-issuance.

During lost-device handling:
- wallet compromise state SHOULD move to `lost_unconfirmed` or `lost_confirmed`
- root credential state MAY move to `suspended`
- verifier-facing derived proofs from the lost wallet SHOULD fail once relevant state is updated
- issuer or recovery service MUST NOT receive ordinary presentation history

## 8. Stolen-device or compromised-wallet flow
When theft or compromise is confirmed:
- wallet compromise state MUST move to `compromised`
- affected root credential state MUST move to `suspended` or `revoked`
- replacement credentials MAY be issued through controlled re-issuance
- derived proofs from the compromised wallet MUST be rejected once state has propagated

The compromise response MUST NOT require per-presentation issuer callbacks.

## 9. Device replacement and holder rebind flow
A replacement wallet or device MUST be rebound before it can produce conformant derived proofs from replacement authority.

The rebind flow MUST include:
1. Holder initiates replacement from a trusted recovery, wallet, or issuer channel.
2. Wallet or recovery authority verifies holder control using the chosen recovery architecture.
3. Issuer or delegated recovery authority determines whether the old root credential is `active`, `suspended`, `revoked`, `expired`, or eligible for `reissued`.
4. Replacement wallet creates new wallet-bound authority or key material.
5. Issuer issues a new root credential or marks the existing credential lineage as `reissued` according to policy.
6. Old wallet-bound proofs are blocked by root credential state, wallet compromise state, key rotation, expiry, or another documented mechanism.
7. Verifiers see only a normal derived proof from the replacement wallet plus permitted status evidence.

Replacement proofs MUST NOT expose:
- previous device identifier
- recovery ticket identifier
- old root credential identifier
- appeal or compromise reason
- backup provider identity
- stable cross-verifier link between old and new wallet instances

## 10. Mistaken suspension, dispute, and appeal flow
Implementations MUST provide a governed path for mistaken suspension and disputed compromise decisions.

The appeal flow MUST include:
- holder-visible notice through wallet, issuer, or recovery channel where notice is safe
- a way for the holder to challenge `suspended`, `lost_confirmed`, or mistaken `compromised` classification
- review by an issuer, delegated recovery authority, or governance authority that did not rely solely on a verifier allegation
- bounded evidence retention
- state correction publication through the same privacy-preserving propagation channel used for the original state

During appeal, root credential state MAY remain `suspended`. Verifiers SHOULD receive only a generic unavailable or invalid result, not the fact that the holder is appealing a suspension.

If an appeal succeeds:
- root credential state MAY return from `suspended` to `active`
- wallet compromise state MAY return from `lost_unconfirmed` or `lost_confirmed` to `normal` or move to `recovered`
- status publishers MUST publish the corrected state within the documented propagation target

If an appeal fails:
- root credential state SHOULD move to `revoked`, `expired`, or remain `suspended` according to policy
- wallet compromise state SHOULD move to `compromised`, `retired`, or remain `lost_confirmed` according to evidence
- rebind or re-proofing SHOULD be offered where policy allows

## 11. Recovery flow
After successful recovery:
- wallet compromise state MAY move to `recovered`
- root credential state MAY move to `reissued` or `active`
- old root credentials SHOULD remain `revoked`, `suspended`, or `expired`

Recovery records MUST be limited to recovery and trust-management purposes. They MUST NOT become verifier-visible identity history.

## 12. Issuer compromise and trust withdrawal
When issuer compromise is detected:
- issuer trust state MUST move to `under_review`, `suspended`, `withdrawn`, or `compromised`
- trust registry updates MUST be sufficient for verifiers to reject affected derived proofs
- wallets SHOULD be able to renew or replace affected root credentials
- affected root credential state MAY move to `suspended`, `revoked`, `reissued`, or `expired`

Issuer compromise handling MUST NOT depend on presentation logs.

Issuer trust withdrawal MUST invalidate trust in affected derived proofs without exposing holder activity.

## 13. Failed-proof privacy behavior
Failed proofs create privacy risk because a verifier may infer that a holder is suspended, compromised, under appeal, using a replacement device, or affected by issuer trust withdrawal.

Wallets and verifiers MUST minimize that inference by:
- using generic failure categories such as `invalid`, `unavailable`, `freshness_unavailable`, or `policy_refused`
- avoiding verifier-visible reason codes such as `compromised_wallet`, `lost_device`, `appeal_pending`, or `suspended_holder` in normal flow
- separating holder-facing recovery UX from verifier-facing failure messages
- avoiding stable retry tokens that link failed and successful presentations across time
- avoiding issuer callbacks that reveal the verifier, holder, or failed presentation

Verifier audit records MAY record that a proof was not accepted, the applicable verifier policy, and the coarse freshness class. They MUST NOT retain raw proof payloads, recovery reason codes, or status artifacts that allow reconstruction of the holder's recovery state unless exception governance explicitly requires and bounds that retention.

## 14. Profile-specific status behavior
### 14.1 Profile R
`Profile R` MAY use deployable batched or cacheable status mechanisms for issuer trust, root credential state, and wallet compromise state where policy requires freshness.

`Profile R` verifiers MAY require fresher status for `V2` high-assurance checks than for `V1` standard checks. They MUST still avoid token-specific live issuer callbacks and MUST avoid retaining verifier-scoped `B1` continuity material as recovery telemetry.

`Profile R` MAY use encrypted backup, hardware-bound recovery, re-proofing, or re-issuance only, provided replacement proofs do not expose old credential or device identifiers in normal flow.

### 14.2 Profile P
`Profile P` SHOULD prefer expiry-first, short-lived authority, privacy-preserving accumulators, relayed status, or re-issuance designs that minimize status lookups.

`Profile P` normal flow MUST NOT expose verifier-stable holder handles, recovery identifiers, old-to-new wallet links, or exact compromise reasons. If a status mechanism would let a verifier distinguish suspended, compromised, appealed, or recovered states for a holder, that mechanism is non-conformant for `Profile P` normal flow.

`Profile P` SHOULD prefer re-proofing or unlinkability-preserving re-issuance over portable backup designs that risk carrying correlation material across devices.

## 15. Privacy impacts
Recovery and compromise handling creates privacy risk because it can introduce:
- issuer observability during re-issuance
- recovery-service metadata
- status lookup correlation
- retained compromise records
- verifier inference from failed proofs

Implementations MUST mitigate these risks by:
- preferring local-first recovery where feasible
- using controlled re-issuance only where needed
- using batched, cacheable, relayable, or non-unique status mechanisms
- limiting retained recovery records to governance need
- keeping ordinary presentation history out of issuer, status, and recovery systems

## 16. Conformance requirements
An implementation MUST be treated as non-conformant if recovery or compromise handling:
- requires per-presentation issuer callbacks in normal flow
- creates issuer-visible presentation histories
- turns the trust registry into a holder registry
- requires normal-flow root credential disclosure
- retains recovery data beyond the declared governance need
- allows a verifier to suspend a holder or confirm compromise directly
- lacks documented propagation and stale-state behavior
- exposes detailed suspension, compromise, appeal, or recovery reasons to verifiers in normal flow
- links old and replacement wallets through verifier-visible recovery or rebind metadata
- applies grace acceptance after fresh evidence of confirmed compromise, revocation, issuer withdrawal, or issuer compromise
