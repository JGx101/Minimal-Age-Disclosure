# Threat Model Seed

## 1. Goal
Identify privacy, security, trust, governance, and deployment risks in a minimal age-disclosure architecture.

## 2. Assets
- root credential
- derived proof
- issuer signing keys
- trust registry data
- verifier request policy object
- wallet disclosure decisions
- issuer trust state
- root credential state
- recovery artifacts
- audit logs
- conformance evidence
- user privacy and behavioural patterns

## 3. Actors
- Holder
- Issuer
- Wallet
- Verifier
- Trust registry operator
- Status publisher or relay
- Auditor or certifier
- Regulator
- Malicious verifier
- Malicious issuer
- Passive network observer
- Colluding verifier set
- Credential thief or attacker
- Analytics or telemetry operator
- Recovery or backup operator if one exists

## 4. Trust boundaries
- between issuer and wallet during root issuance
- between wallet and verifier during derived proof presentation
- between verifier and trust registry during issuer validation
- between verifier and status infrastructure during issuer or root-state checking
- between holder device and local storage
- between recovery mechanism and holder control
- between normal flow and exceptional higher-disclosure flow

## 5. Key threats

### T1. Over-collection by verifier
A verifier requests identity or document-level data when only a threshold answer is needed.

### T2. Cross-site correlation
Multiple verifiers correlate the same holder using a stable subject identifier, reusable proof artifact, repeated metadata, or timing patterns.

### T3. Revocation surveillance
A status or revocation design learns when and where a holder uses their credential.

### T4. Issuer presentation visibility
The issuer learns about ordinary presentation events.

### T5. Replay or forwarding
An attacker reuses or forwards a captured proof to another verifier.

### T6. Credential sharing
A credential is presented by someone other than the intended holder.

### T7. Wallet over-sharing
The wallet hides what is being disclosed or defaults to an overbroad response.

### T8. Compromised issuer
Issuer keys are stolen or the issuer becomes malicious.

### T9. Policy creep
The ecosystem drifts from threshold proof to routine identity disclosure.

### T10. Exception abuse
A supposedly rare higher-disclosure route becomes the default operational path.

### T11. Metadata fingerprinting
Coarse assurance values, issuer references, timestamps, policy identifiers, or proof-binding metadata become practical correlators.

### T12. Recovery surveillance
A recovery or backup mechanism recreates centralised visibility or long-term holder tracking.

### T13. Trust-registry overreach
The trust registry accumulates or exposes more than issuer-validation metadata.

### T14. Telemetry leakage
Verifier or wallet telemetry silently reconstructs proof usage patterns even when the proof payload is minimal.

## 6. Initial mitigations
- root credential kept local
- derived transaction-bound proof
- no stable verifier-visible holder identifier in the normal flow
- nonce and audience binding
- coarse assurance buckets
- issuer-class abstraction by default where possible
- metadata minimisation rules
- batched or expiry-first status for issuer or root state only
- verifier conformance and retention controls
- local-first recovery stance
- explicit exception governance

## 7. Open threat-model questions
- what anti-sharing support is realistic without breaking anti-correlation goals
- where exact issuer identity is required versus where issuer class is sufficient
- how to validate verifier telemetry minimisation in practice
- how much offline verification is achievable across both technical profiles
- which metadata fields are acceptable in Profile R but not in Profile P
- what recovery approach adds the least new tracking surface
