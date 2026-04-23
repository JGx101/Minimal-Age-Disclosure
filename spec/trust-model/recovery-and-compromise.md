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

## 3. Lost-device flow
When a holder reports a lost device, the system SHOULD first support local recovery or backup restoration where available.

If local recovery is unavailable, the system MAY use controlled re-issuance.

During lost-device handling:
- wallet compromise state SHOULD move to `lost_unconfirmed` or `lost_confirmed`
- root credential state MAY move to `suspended`
- verifier-facing derived proofs from the lost wallet SHOULD fail once relevant state is updated
- issuer or recovery service MUST NOT receive ordinary presentation history

## 4. Stolen-device or compromised-wallet flow
When theft or compromise is confirmed:
- wallet compromise state MUST move to `compromised`
- affected root credential state MUST move to `suspended` or `revoked`
- replacement credentials MAY be issued through controlled re-issuance
- derived proofs from the compromised wallet MUST be rejected once state has propagated

The compromise response MUST NOT require per-presentation issuer callbacks.

## 5. Recovery flow
After successful recovery:
- wallet compromise state MAY move to `recovered`
- root credential state MAY move to `reissued` or `active`
- old root credentials SHOULD remain `revoked`, `suspended`, or `expired`

Recovery records MUST be limited to recovery and trust-management purposes. They MUST NOT become verifier-visible identity history.

## 6. Issuer compromise and trust withdrawal
When issuer compromise is detected:
- issuer trust state MUST move to `under_review`, `suspended`, `withdrawn`, or `compromised`
- trust registry updates MUST be sufficient for verifiers to reject affected derived proofs
- wallets SHOULD be able to renew or replace affected root credentials
- affected root credential state MAY move to `suspended`, `revoked`, `reissued`, or `expired`

Issuer compromise handling MUST NOT depend on presentation logs.

Issuer trust withdrawal MUST invalidate trust in affected derived proofs without exposing holder activity.

## 7. Privacy impacts
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

## 8. Conformance requirements
An implementation MUST be treated as non-conformant if recovery or compromise handling:
- requires per-presentation issuer callbacks in normal flow
- creates issuer-visible presentation histories
- turns the trust registry into a holder registry
- requires normal-flow root credential disclosure
- retains recovery data beyond the declared governance need
