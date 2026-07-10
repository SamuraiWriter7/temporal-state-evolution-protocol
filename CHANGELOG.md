# Changelog

All notable changes to the **Temporal State Evolution Protocol** are documented in this file.

The project currently follows a candidate specification release model.

---

## [0.5.0-candidate] - 2026-07-10

### Added

* Trace & Audit Bridge specification.
* Temporal Lifecycle Audit Record schema.
* Unified temporal lifecycle audit example.
* Temporal Trace Package model.
* Trace export rules.
* Lifecycle Audit pipeline.
* Audit Finding model.
* Origin Cross-Reference model.
* Attribution Readiness model.
* Royalty Bridge safeguards.
* Trace Relay Bridge rules.
* Unified Temporal Lifecycle Record.
* Trace & Audit Consistency Check.

### Added Audit Domains

The lifecycle audit now evaluates:

* temporal continuity,
* state lineage,
* cadence integrity,
* precedence consistency,
* causality integrity,
* Temporal Illusion,
* dispute visibility,
* Origin binding,
* attribution readiness.

### Added Audit Status Model

Supported statuses:

* `pass`
* `pass_with_warnings`
* `disputed`
* `quarantine`
* `fail`
* `human_review_required`

### Added Attribution Readiness Model

Supported readiness states:

* `not_ready`
* `candidate`
* `supported`
* `verified`
* `disputed`
* `blocked`

### Added Failure Modes

* Trace Completeness Illusion
* Audit Laundering
* Dispute Suppression
* Origin History Rewrite
* Attribution Overreach
* Confidence Inflation
* Audit-Trace Divergence
* Hidden Temporal Gap
* Integrity-Truth Confusion
* Derivative Trace Amnesia
* Royalty Backflow Rewrite

### Trace Export

Temporal history may now be exported across:

* agents,
* wings,
* systems,
* derivative processes.

Export must preserve:

* confidence,
* causal gaps,
* disputes,
* retrospective inference labels,
* Temporal Illusion findings,
* audit status,
* historical identity.

Trace movement must not silently increase certainty.

### Origin Cross-Reference

Version 0.5 introduces non-destructive Origin cross-reference.

The protocol now distinguishes:

```text
Origin relation
```

from:

```text
Runtime causal influence
```

A later Origin discovery must not rewrite the original runtime Decision Context.

Relevant temporal fields may include:

* `causal_effective_time`
* `discovered_at`
* `asserted_at`
* `verified_at`

### Royalty and Attribution Safeguards

Downstream attribution and Royalty systems may receive:

* audit record references,
* Trace package references,
* supported causal path references,
* Origin cross-references,
* attribution readiness status,
* open disputes,
* Temporal Illusion findings.

The bridge prohibits:

* hidden confidence upgrades,
* dispute suppression,
* Decision Context rewriting,
* unsupported Origin causality,
* chronology-only contribution claims.

### Design Principle

Version 0.5 separates:

```text
Trace Completeness
```

from:

```text
Causal Verification
```

and separates:

```text
Origin Association
```

from:

```text
Runtime Influence
```

and separates:

```text
Causal Support
```

from:

```text
Verified Attribution
```

### First Arc Complete

The first complete Temporal State Evolution lifecycle is now:

```text
Pulse
→ State
→ Evaluation
→ Transition
→ Cadence
→ Next Pulse
→ Decision Context
→ Causal Binding
→ Causal Path
→ Trace Package
→ Lifecycle Audit
→ Origin Cross-Reference
→ Attribution Readiness
```

---

## [0.4.0-candidate] - 2026-07-10

### Added

* Temporal Causality Binding specification.
* Temporal Causality Binding Record schema.
* Temporal Causality Binding example.
* Decision Context model.
* Evidence Availability model.
* State-to-Decision causal binding.
* Decision-to-Action causal binding.
* Pulse-to-Transition binding.
* Cadence causality binding.
* Temporal Causal Path construction.
* Counterfactual Support model.
* Causal Dispute model.
* Temporal Illusion Detection.
* Temporal Causality Consistency Check.

### Added Causal Relation Taxonomy

* direct cause,
* contributing cause,
* enabling condition,
* constraining condition,
* authorizing condition,
* triggering event,
* routing influence,
* timing influence,
* inhibiting cause,
* counterfactual dependency,
* disputed causality.

### Added Causal Basis Taxonomy

* explicit runtime reference,
* policy dependency,
* state diff,
* execution dependency,
* action receipt,
* tool call dependency,
* handoff dependency,
* intervention result,
* replay comparison,
* counterfactual simulation,
* human review,
* statistical association,
* unknown.

### Added Evidence Availability States

Evidence may now be classified as:

* `available`
* `accessible_but_unused`
* `used`
* `unavailable`
* `unknown`
* `discovered_later`

This prevents information that merely existed somewhere in a system from being automatically treated as a causal influence.

### Added Temporal Illusion Detection

Checks now cover:

* late evidence injection,
* reconstructed context substitution,
* post-hoc causal narrative,
* timestamp-only causality,
* future knowledge backflow,
* superseded decision attribution.

### Added Failure Modes

* Temporal Illusion
* Chronology-Causality Confusion
* Causal Path Hallucination
* Evidence Backfill
* Decision-Action Misattribution
* Causal Overconfidence
* Causal Under-Specification
* Hidden Competing Path
* Outcome Backflow

### Design Principle

Version 0.4 separates temporal order from causal influence.

The protocol now distinguishes:

```text
Occurred Before
```

from:

```text
Contributed To
Enabled
Constrained
Authorized
Triggered
Changed Timing
Prevented
```

A causal history must preserve:

* what existed,
* what was available,
* what was used,
* what influenced the decision,
* what produced the action,
* what followed,
* what remains uncertain.

### Causal Path Model

The protocol can now represent:

```text
Pulse
→ State
→ Evidence
→ Evaluation
→ Decision
→ Action
→ Outcome
```

as a sequence of independently auditable causal bindings.

Missing links remain explicit causal gaps.

Competing explanations may coexist as separate candidate paths.

---

## [0.3.0-candidate] - 2026-07-10

### Added

* Adaptive Cadence Policy.
* Cadence Decision Record schema.
* Adaptive Cadence example.
* State-aware Pulse timing model.
* Cadence Signal model.
* Cadence Hysteresis policy.
* Cadence Budget policy.
* Computational Pranayama Bridge.
* State Transition Rule binding.
* Structural Precedence binding.
* Cadence Consistency Check.

### Added Cadence Modes

* `quiet`
* `normal`
* `active`
* `critical`
* `sleep`
* `suspended`

### Added Cadence Actions

* `accelerate`
* `maintain`
* `decelerate`
* `enter_quiet`
* `enter_sleep`
* `wake`
* `suspend`
* `emergency_escalate`

### Added State Signals

Cadence decisions may now consider:

* state stability,
* risk level,
* goal urgency,
* unresolvedness,
* computational load,
* resource pressure,
* external event pressure,
* human attention requirement.

### Added Next Pulse Policies

* fixed interval,
* bounded interval,
* event-driven,
* hybrid,
* suspended.

### Added Failure Modes

* Pulse Storm
* Cadence Lock
* Cadence Oscillation
* False Urgency
* Temporal Starvation
* Sleep Without Wake
* Critical Mode Exhaustion
* Resource-Blind Acceleration
* Retroactive Cadence Justification

### Computational Pranayama Integration

Version 0.3 formally connects temporal state evolution with computation pacing and rest policy.

The protocol recognizes that unresolved state does not automatically justify additional computation.

A system may instead:

* reduce activity,
* wait,
* sleep,
* delegate,
* reroute,
* suspend,
* resume later.

### Design Principle

Version 0.3 introduces adaptive temporal pacing.

The protocol now represents:

```text
State
  ↓
Cadence Evaluation
  ↓
Next Pulse Policy
  ↓
Pulse
  ↓
Evaluation
  ↓
State Transition
```

The current state may influence when the next evaluation occurs.

This closes the first temporal feedback loop:

```text
State(t)
   ↓
Cadence(t)
   ↓
Pulse(t+1)
   ↓
Evaluation(t+1)
   ↓
State(t+1)
```

---

## [0.2.0-candidate] - 2026-07-10

### Added

* State Transition Rule specification.
* State Transition Record schema.
* State Transition example.
* Transition Proposal model.
* Precondition checks.
* Transition Guard model.
* Authorization model.
* State Lineage model.
* State Lifecycle Status model.
* Structural Precedence binding.
* Transition Consistency Check.

### Added Transition Decision Types

* `retain`
* `advance`
* `branch`
* `suspend`
* `resume`
* `supersede`
* `reconcile`
* `terminate`

### Added State Lifecycle Statuses

* `proposed`
* `active`
* `retained`
* `branched`
* `suspended`
* `superseded`
* `reconciled`
* `terminated`
* `quarantined`

### Added Transition Pipeline

```text
Transition Proposal
        ↓
Precondition Check
        ↓
Guard Evaluation
        ↓
Authorization
        ↓
Execution
        ↓
Trace Binding
```

### Added Lineage Models

Direct lineage:

```text
S0 → S1 → S2 → S3
```

Branch lineage:

```text
          → S2-A → S3-A
S0 → S1
          → S2-B → S3-B
```

Reconciliation lineage:

```text
S3-A ───\
         → S4-R
S3-B ───/
```

### Added Failure Modes

* Unauthorized Transition
* Transition Without Predecessor
* Hidden State Fork
* Invalid Reconciliation
* State Overwrite
* Transition Loop
* Authorization Laundering
* False Retention

### Design Principle

Version 0.2 defines a state transition as more than value mutation.

A valid state-changing transition requires:

* a predecessor,
* a reason,
* applicable prerequisites,
* cleared guards,
* valid authorization,
* an auditable successor lineage.

Version 0.2 also recognizes **retention** as an explicit temporal decision.

A system may legitimately evaluate itself and decide not to change.

---

## [0.1.0-candidate] - 2026-07-08

### Added

* Initial Temporal State Evolution Protocol structure.
* Pulse Record model.
* Pulse Record JSON Schema.
* Pulse Record example.
* Structural Precedence Core specification.
* Initial cadence mode vocabulary.
* Pulse trigger model.
* State evaluation result model.
* Precedence assertion modes.
* Initial Precedence Consistency Check foundation.

### Added Structural Precedence Hierarchy

#### Local Precedence

Direct state or event causality.

```text
State(t)
    ↓
Transition
    ↓
State(t+1)
```

#### Structural Precedence

A prerequisite structure enables or constrains a later process.

```text
Prerequisite Structure
        ↓
Allowed Transition Space
```

#### Ontological Precedence

An Origin, source, foundational rule, or contribution basis makes a later process possible.

```text
Origin
    ↓
Derivative Possibility Space
    ↓
Temporal Process
```

### Added Initial Failure Modes

* Precedence Collapse
* Temporal Illusion
* Causal Direction Inversion
* Retroactive Origin Injection
* Precedence Cycle

### Added Core Principle

Chronological order alone must not be treated as proof of causality.

A prior timestamp does not automatically establish causal precedence.

Temporal history becomes structurally meaningful only when:

* predecessor,
* successor,
* relation type,
* evidence,
* assertion mode,

remain explicit.

### Design Principle

Version 0.1 establishes the initial relationship:

```text
Pulse
    ↓
Evaluation
    ↓
Transition
    ↓
State Evolution
    ↓
Structural Precedence
```

The first specification layer answers:

> When did evaluation occur, what changed, and what legitimately preceded what?

---

# First Arc Summary

The first candidate arc consists of:

```text
v0.1
Pulse Record
+
Structural Precedence Foundation
        │
        ▼
v0.2
State Transition Rule
        │
        ▼
v0.3
Adaptive Cadence Policy
        │
        ▼
v0.4
Temporal Causality Binding
        │
        ▼
v0.5
Trace & Audit Bridge
```

The architecture evolved from recording individual temporal events into a complete auditable lifecycle:

```text
Pulse
→ State
→ Transition
→ Cadence
→ Decision Context
→ Causal Binding
→ Causal Path
→ Trace Package
→ Audit
→ Origin Cross-Reference
→ Attribution Readiness
```

The first arc is now structurally complete.

Future development may focus on executable semantic validators for:

* PCC — Precedence Consistency Check
* TCC — Transition Consistency Check
* CCC — Cadence Consistency Check
* TCCC — Temporal Causality Consistency Check
* TACC — Trace & Audit Consistency Check

and on interoperability with external Trace, Origin, handoff, audit, and Royalty protocol ecosystems.
