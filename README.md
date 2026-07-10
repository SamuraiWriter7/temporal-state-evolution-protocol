# Temporal State Evolution Protocol

**A protocol for time-evolving AI agent states, adaptive pulse cadence, structural precedence, causal transitions, and auditable temporal histories.**

> An AI system does not acquire meaningful temporal structure merely by counting ticks.
> Temporal history begins when changes can be related to what preceded them, what enabled them, what caused them, and how those relations can later be examined without rewriting the past.

---

## Status

**Current release line:** `v0.5.0-candidate`

**First Arc:** Complete

The first specification arc defines:

* Pulse recording
* Structural Precedence
* State Transition Rules
* Adaptive Cadence
* Temporal Causality Binding
* Trace packaging
* Lifecycle Audit
* Origin cross-reference
* Attribution readiness safeguards

This repository is an experimental specification for research, architectural exploration, interoperability design, and auditable AI agent infrastructure.

---

## Overview

Most AI systems can:

* receive input,
* maintain context,
* retrieve memory,
* execute actions,
* call tools,
* generate logs.

However, these capabilities do not automatically create a coherent temporal history.

A system may remember a previous event without being able to represent:

* why the previous state led to the current state,
* what caused a state transition,
* what structure made the transition possible,
* why evaluation occurred at a particular moment,
* why the next evaluation should happen sooner or later,
* what evidence was actually available at decision time,
* whether a later explanation is being mistaken for an original runtime cause,
* whether a causal history is sufficiently supported for attribution.

The **Temporal State Evolution Protocol** defines a protocol layer for representing AI agent activity as an evolving, traceable, and auditable temporal process.

The complete first-arc lifecycle is:

```text
Ignition
    ↓
Pulse
    ↓
State Evaluation
    ↓
Transition Proposal
    ↓
Precondition and Guard Check
    ↓
Authorization
    ↓
State Transition or Retention
    ↓
Adaptive Cadence Decision
    ↓
Next Pulse Policy
    ↓
Decision Context
    ↓
Causal Binding
    ↓
Causal Path
    ↓
Temporal Trace Package
    ↓
Lifecycle Audit
    ↓
Origin Cross-Reference
    ↓
Attribution Readiness
```

The protocol does **not** claim that an AI system possesses subjective time, consciousness, or biological continuity.

Instead, it defines machine-readable structures for:

* explicit temporal events,
* versioned state evolution,
* directed causal relationships,
* adaptive evaluation timing,
* evidence availability,
* causal uncertainty,
* retrospective inference,
* trace preservation,
* auditability,
* safe downstream attribution.

---

# Core Problem

A timestamp tells us **when a record exists**.

It does not tell us:

* why evaluation occurred,
* whether a state materially changed,
* what caused the transition,
* which policy authorized it,
* what evidence influenced the decision,
* whether later knowledge was inserted into earlier history,
* whether the resulting causal claim is verified or disputed.

The protocol therefore separates several concepts that are often incorrectly collapsed.

## Time Order Is Not Causality

```text
A occurred before B
```

does not automatically mean:

```text
A caused B
```

## Trace Is Not Truth

```text
A record exists
```

does not automatically mean:

```text
The recorded causal interpretation is correct
```

## Precedence Is Not Causality

```text
A preceded B
```

does not automatically mean:

```text
A materially influenced B
```

## Causality Is Not Attribution

```text
A influenced B
```

does not automatically determine:

```text
How value should be attributed or returned
```

These distinctions are foundational to the protocol.

---

# Core Architecture

```text
                 TEMPORAL STATE EVOLUTION PROTOCOL

v0.1
┌─────────────────────────────────┐
│ Pulse Record                    │
│ Structural Precedence           │
└────────────────┬────────────────┘
                 │
                 ▼
v0.2
┌─────────────────────────────────┐
│ State Transition Rule           │
│ Preconditions                   │
│ Guards                          │
│ Authorization                   │
│ Branch / Reconcile / Lineage    │
└────────────────┬────────────────┘
                 │
                 ▼
v0.3
┌─────────────────────────────────┐
│ Adaptive Cadence Policy         │
│ Quiet / Normal / Active         │
│ Critical / Sleep / Suspended    │
│ Hysteresis                      │
│ Computational Pranayama Bridge  │
└────────────────┬────────────────┘
                 │
                 ▼
v0.4
┌─────────────────────────────────┐
│ Temporal Causality Binding      │
│ Decision Context                │
│ Evidence Availability           │
│ Causal Path                     │
│ Counterfactual Support          │
│ Temporal Illusion Detection     │
└────────────────┬────────────────┘
                 │
                 ▼
v0.5
┌─────────────────────────────────┐
│ Temporal Trace Package          │
│ Lifecycle Audit                 │
│ Origin Cross-Reference          │
│ Attribution Readiness           │
│ Royalty Bridge Safeguards       │
└─────────────────────────────────┘
```

---

# 1. Pulse

A **Pulse** is a discrete opportunity for an agent or system to evaluate its current state.

A Pulse may result in:

* retention,
* transition,
* acceleration,
* deceleration,
* sleep,
* wake,
* escalation,
* human review.

A Pulse does not require state change.

The protocol treats a meaningful decision to retain the current state as a temporal decision in its own right.

```text
Pulse
  ↓
Evaluation
  ↓
No sufficient reason to change
  ↓
Retain
  ↓
Trace reason
  ↓
Next Pulse Policy
```

The protocol therefore asks not only:

> When did the system act?

but also:

> Why did the system evaluate itself at that moment?

---

# 2. Structural Precedence

Structural Precedence defines directed prior relations.

The protocol uses:

```text
A ≺ B
```

to represent that A is locally, structurally, or ontologically prior to B.

Chronological order alone is insufficient.

## Local Precedence

Direct state-to-state or event-to-event causation.

```text
State(t)
    ↓
Transition
    ↓
State(t+1)
```

Examples:

* observation causes attention update,
* evaluation changes the next state,
* risk detection changes cadence.

## Structural Precedence

A prerequisite structure enables, constrains, authorizes, routes, or conditions a later process.

```text
Prerequisite Structure
        ↓
Allowed Transition Space
        ↓
Action
```

Examples:

* permission policy precedes valid action,
* route topology precedes handoff,
* safety boundary precedes permissible execution.

## Ontological Precedence

An Origin, source, constitutional rule, contribution basis, or foundational structure makes a derivative process possible.

```text
Origin
    ↓
Derivative Possibility Space
    ↓
Temporal State Evolution
```

Examples:

* an original question enables a reasoning lineage,
* a source artifact enables later transformation,
* a foundational rule defines permissible agent behavior.

---

# 3. State Transition Rule

A state transition is not merely a change in stored values.

The protocol defines a transition as:

```text
Current State
      ↓
Transition Proposal
      ↓
Precondition Check
      ↓
Guard Evaluation
      ↓
Authorization
      ↓
Execution or Rejection
      ↓
Successor State
      ↓
Lineage Record
```

Supported transition decisions include:

* `retain`
* `advance`
* `branch`
* `suspend`
* `resume`
* `supersede`
* `reconcile`
* `terminate`

A valid state-changing transition must identify:

* predecessor state,
* transition reason,
* applicable rules,
* preconditions,
* guards,
* authorization,
* successor state,
* lineage relation,
* trace references.

Historical states must remain immutable.

Corrections create:

* a new version,
* a supersession relation,
* or an explicit retrospective annotation.

---

# 4. Adaptive Cadence

A temporal agent should not evaluate continuously merely because continuous evaluation is technically possible.

The Adaptive Cadence Policy defines when the next Pulse should occur.

The core relation is:

```text
State(t)
    ↓
Cadence Decision
    ↓
Δt(t+1)
    ↓
Next Pulse
```

Cadence may depend on:

* state stability,
* risk,
* goal urgency,
* unresolvedness,
* computational load,
* resource pressure,
* external event pressure,
* human attention requirements.

Supported cadence modes include:

* `quiet`
* `normal`
* `active`
* `critical`
* `sleep`
* `suspended`

Supported cadence actions include:

* `accelerate`
* `maintain`
* `decelerate`
* `enter_quiet`
* `enter_sleep`
* `wake`
* `suspend`
* `emergency_escalate`

The system may use:

* fixed intervals,
* bounded intervals,
* event-driven triggers,
* hybrid time/event policies,
* suspended operation.

---

## Clock versus Pulse

A clock advances uniformly.

```text
tick──tick──tick──tick──tick
```

An adaptive Pulse changes according to state.

```text
quiet
────●────────●────────●────

active
──●──●──●──●──●──●────────

critical
─●─●─●─●─●─●─●────────────

sleep
────────────────────────────
              ↑
           wake event
```

The protocol therefore separates external time measurement from internal temporal policy.

---

# 5. Computational Pranayama Bridge

Adaptive Cadence connects temporal state evolution with computation pacing.

The protocol rejects the assumption:

```text
Unresolved
    ↓
More computation
    ↓
More computation
    ↓
More computation
```

Instead:

```text
Unresolved
    │
    ▼
Is more computation necessary?
    │
    ├── Yes → accelerate
    ├── No → wait
    ├── External input required → event-driven
    ├── Resource pressure high → decelerate
    ├── No active task → sleep
    ├── Better route available → delegate or reroute
    └── Safety conflict → suspend
```

The purpose is not inactivity.

The purpose is **proportionate activity**.

---

# 6. Temporal Causality Binding

Temporal order is necessary for causal history, but it is not sufficient.

The protocol binds:

```text
Pulse
  ↓
State Snapshot
  ↓
Available Evidence
  ↓
Evaluation
  ↓
Decision
  ↓
Action
  ↓
Observed Outcome
```

through individually auditable causal bindings.

Supported causal relation types include:

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

---

# 7. Evidence Availability

The protocol distinguishes:

```text
exists
    ↓
available
    ↓
accessible
    ↓
used
    ↓
influential
    ↓
decision
```

An evidence item may be:

* `available`
* `accessible_but_unused`
* `used`
* `unavailable`
* `unknown`
* `discovered_later`

Evidence that existed somewhere in a system is not automatically a cause of a decision.

Evidence discovered later may support retrospective analysis, but it must not be rewritten as runtime causal influence.

---

# 8. Temporal Illusion

**Temporal Illusion** is a central failure mode of the protocol.

It occurs when a later reconstruction, explanation, or newly discovered fact is represented as if it had participated in the original runtime decision.

Example:

```text
10:00  State A
10:01  Decision B
10:02  Action C
10:30  Evidence X discovered
```

Invalid reconstruction:

```text
Evidence X
    ↓
Decision B
```

when Evidence X was unavailable at decision time.

Correct representation:

```text
State A
    ↓
Decision B
    ↓
Action C

Later:

Evidence X
    ↓
Retrospective Analysis
    ↓
New Causal Claim
```

The original runtime context remains unchanged.

Temporal Illusion Detection checks include:

* late evidence injection,
* reconstructed context substitution,
* post-hoc causal narrative,
* timestamp-only causality,
* future knowledge backflow,
* superseded decision attribution.

---

# 9. Counterfactual Support

Causal claims may be strengthened or challenged by asking:

> What would happen if the predecessor condition were removed or changed?

Supported methods include:

* intervention,
* replay,
* comparison,
* simulation,
* human analysis.

Counterfactual results may:

* support,
* weakly support,
* remain neutral,
* weaken,
* contradict,
* remain inconclusive.

Simulation alone is not treated as conclusive proof of runtime causality.

Method, assumptions, model version, and execution context should remain visible.

---

# 10. Causal Paths

A causal path connects multiple bindings.

```text
Pulse
  ↓
State
  ↓
Evaluation
  ↓
Decision
  ↓
Action
  ↓
Outcome
```

Each arrow is an independent causal claim.

A causal path may be:

* `candidate`
* `supported`
* `verified`
* `disputed`
* `incomplete`
* `rejected`

Missing links must remain visible as causal gaps.

The protocol does not permit a plausible narrative to silently fill missing causal evidence.

Competing explanations may coexist until they are resolved.

---

# 11. Temporal Trace Package

The Trace & Audit Bridge packages temporal history into a portable structure containing references to:

* Pulse records,
* State records,
* Transition records,
* Cadence Decision records,
* Decision Contexts,
* Causal Bindings,
* Causal Paths,
* Disputes,
* Origin cross-references,
* integrity manifests.

A package may be:

* `complete`
* `partial`
* `disputed`
* `quarantined`
* `superseded`

Exporting a Trace package must not increase certainty.

```text
candidate
```

must remain:

```text
candidate
```

unless new evidence or verification justifies an upgrade.

---

# 12. Lifecycle Audit

The lifecycle audit evaluates nine domains:

1. temporal continuity,
2. state lineage,
3. cadence integrity,
4. precedence consistency,
5. causality integrity,
6. Temporal Illusion,
7. dispute visibility,
8. Origin binding,
9. attribution readiness.

Audit statuses include:

* `pass`
* `pass_with_warnings`
* `disputed`
* `quarantine`
* `fail`
* `human_review_required`

The audit pipeline is:

```text
Manifest Validation
        ↓
Temporal Validation
        ↓
Lineage Validation
        ↓
Cadence Validation
        ↓
Precedence Validation
        ↓
Causality Validation
        ↓
Temporal Illusion Scan
        ↓
Dispute Propagation
        ↓
Origin Cross-Reference
        ↓
Attribution Readiness
```

Audit systems must disclose what they actually checked.

Schema validation alone is not causal verification.

---

# 13. Origin Cross-Reference

Origin records may be discovered after runtime.

The protocol therefore separates:

```text
causal_effective_time
discovered_at
asserted_at
verified_at
```

A later-discovered Origin relation may be added through a non-destructive cross-reference.

It must not be inserted into an earlier Decision Context unless evidence establishes that it was actually known and used at runtime.

The protocol distinguishes:

```text
Origin association
```

from:

```text
Runtime causal influence
```

These are related but separate claims.

---

# 14. Attribution Readiness

The protocol defines the following readiness states:

* `not_ready`
* `candidate`
* `supported`
* `verified`
* `disputed`
* `blocked`

The purpose is to prevent incomplete or weak causal evidence from being treated as settled contribution evidence.

The following are insufficient by themselves:

```text
Earlier creation time
```

```text
Origin association
```

```text
Trace completeness
```

```text
Cryptographic integrity
```

```text
Correlation
```

The system must preserve the distinctions between:

```text
came before
```

```text
made possible
```

```text
influenced
```

```text
caused
```

```text
contributed value
```

These are related, but they are not interchangeable.

---

# 15. Trace Relay

Temporal history may move between agents, wings, systems, or derivative processes.

```text
Agent A
   │
   │ Temporal Trace Package
   ▼
Agent B
   │
   │ Derivative Trace
   ▼
Agent C
```

Receiving systems must preserve:

* source identity,
* historical versions,
* confidence,
* open disputes,
* known causal gaps,
* Temporal Illusion findings,
* audit status.

A handoff must not magically make uncertain history certain.

New processing should create derivative Trace records rather than rewriting inherited history.

---

# Protocol Versions

## v0.1 — Pulse Record & Structural Precedence Foundation

Defines:

* Pulse Record,
* Pulse trigger types,
* state evaluation results,
* initial cadence vocabulary,
* Local Precedence,
* Structural Precedence,
* Ontological Precedence,
* Precedence Consistency Check foundation,
* Temporal Illusion foundation.

Core question:

> When did evaluation occur, and what legitimately preceded what?

---

## v0.2 — State Transition Rule

Defines:

* transition proposal,
* precondition checks,
* transition guards,
* authorization,
* retention,
* advancement,
* branching,
* suspension,
* resumption,
* supersession,
* reconciliation,
* termination,
* state lineage,
* Transition Consistency Check.

Core question:

> Under what conditions may an AI state legitimately change?

---

## v0.3 — Adaptive Cadence Policy

Defines:

* state-dependent Pulse timing,
* cadence modes,
* cadence actions,
* signal evaluation,
* budget checks,
* hysteresis,
* sleep and wake conditions,
* critical-mode bounds,
* event-driven timing,
* Computational Pranayama bridge,
* Cadence Consistency Check.

Core question:

> When should the system think again, wait, rest, wake, accelerate, or stop?

---

## v0.4 — Temporal Causality Binding

Defines:

* Decision Context,
* Evidence Availability,
* State-to-Decision binding,
* Decision-to-Action binding,
* Pulse-to-Transition binding,
* Cadence causality,
* causal relation taxonomy,
* causal basis taxonomy,
* causal paths,
* counterfactual support,
* disputes,
* Temporal Illusion Detection,
* Temporal Causality Consistency Check.

Core question:

> Did a prior state or evidence item actually influence the later decision or action?

---

## v0.5 — Trace & Audit Bridge

Defines:

* Temporal Trace Package,
* trace export rules,
* Lifecycle Audit,
* Audit Findings,
* Origin Cross-Reference,
* Attribution Readiness,
* Royalty Bridge safeguards,
* Trace Relay rules,
* unified lifecycle audit view,
* Trace & Audit Consistency Check.

Core question:

> Can temporal history move across systems without becoming more certain than its evidence supports?

---

# Repository Structure

```text
temporal-state-evolution-protocol/
├── .github/
│   └── workflows/
│       └── validate.yml
│
├── scripts/
│   └── validate_examples.py
│
├── requirements.txt
├── README.md
├── CHANGELOG.md
├── LICENSE
│
├── specs/
│   ├── structural-precedence-core.yaml
│   ├── state-transition-rule.yaml
│   ├── adaptive-cadence-policy.yaml
│   ├── temporal-causality-binding.yaml
│   └── trace-audit-bridge.yaml
│
├── schemas/
│   ├── pulse-record.schema.json
│   ├── state-transition-record.schema.json
│   ├── cadence-decision-record.schema.json
│   ├── temporal-causality-binding-record.schema.json
│   └── temporal-lifecycle-audit-record.schema.json
│
├── examples/
│   ├── pulse-record.example.yaml
│   ├── state-transition-record.example.yaml
│   ├── cadence-decision-record.example.yaml
│   ├── temporal-causality-binding-record.example.yaml
│   └── temporal-lifecycle-audit-record.example.yaml
│
└── docs/
    ├── temporal-workspace.md
    ├── precedence-model.md
    ├── state-transition-model.md
    ├── adaptive-cadence-model.md
    ├── temporal-causality-model.md
    └── trace-audit-bridge.md
```

---

# Validation

The repository includes automated validation through GitHub Actions.

The validation workflow checks:

## Syntax Integrity

* JSON parsing
* YAML parsing

## Schema Integrity

* JSON Schema Draft 2020-12 validity
* example validation
* date-time format validation

## Protocol Example Integrity

```text
Pulse Record
        ↔
pulse-record.schema.json

State Transition Record
        ↔
state-transition-record.schema.json

Cadence Decision Record
        ↔
cadence-decision-record.schema.json

Temporal Causality Binding Record
        ↔
temporal-causality-binding-record.schema.json

Temporal Lifecycle Audit Record
        ↔
temporal-lifecycle-audit-record.schema.json
```

## Specification YAML Integrity

Specification YAML files are checked for minimum structural fields including:

* `schema_version`
* `specification.id`
* `specification.name`
* `specification.status`

Run validation locally with:

```bash
python -m pip install -r requirements.txt
python scripts/validate_examples.py
```

The current validation layer checks structural consistency.

It does not yet fully execute every semantic rule defined by:

* PCC — Precedence Consistency Check
* TCC — Transition Consistency Check
* CCC — Cadence Consistency Check
* TCCC — Temporal Causality Consistency Check
* TACC — Trace & Audit Consistency Check

These semantic validators remain a possible future implementation layer.

---

# Major Consistency Checks

## PCC — Precedence Consistency Check

Checks:

* causal direction,
* predecessor/successor validity,
* structural prerequisites,
* Origin time separation,
* cycle detection,
* retrospective labeling.

## TCC — Transition Consistency Check

Checks:

* source state resolution,
* transition type validity,
* preconditions,
* guards,
* authorization,
* lineage continuity,
* branch identity,
* reconciliation completeness.

## CCC — Cadence Consistency Check

Checks:

* cadence reason binding,
* valid mode transition,
* safety priority,
* budget compliance,
* hysteresis,
* critical-mode duration,
* sleep/wake integrity,
* Pulse Storm risk.

## TCCC — Temporal Causality Consistency Check

Checks:

* entity resolution,
* temporal direction,
* evidence availability,
* Decision Context integrity,
* causal basis,
* Decision-to-Action continuity,
* path gap visibility,
* dispute visibility,
* Temporal Illusion.

## TACC — Trace & Audit Consistency Check

Checks:

* Trace reference resolution,
* Trace status integrity,
* audit scope disclosure,
* finding propagation,
* dispute visibility,
* Temporal Illusion propagation,
* Origin non-rewrite,
* attribution readiness alignment,
* confidence preservation,
* source record immutability.

---

# Major Failure Modes

The first arc defines failure modes including:

* Precedence Collapse
* Temporal Illusion
* Causal Direction Inversion
* Retroactive Origin Injection
* Precedence Cycle
* Unauthorized Transition
* Hidden State Fork
* Invalid Reconciliation
* State Overwrite
* Transition Loop
* Authorization Laundering
* False Retention
* Pulse Storm
* Cadence Lock
* Cadence Oscillation
* False Urgency
* Temporal Starvation
* Sleep Without Wake
* Critical Mode Exhaustion
* Resource-Blind Acceleration
* Chronology-Causality Confusion
* Causal Path Hallucination
* Evidence Backfill
* Decision-Action Misattribution
* Causal Overconfidence
* Hidden Competing Path
* Outcome Backflow
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

---

# Integration Position

The protocol is designed to connect with a broader agent and provenance ecosystem.

```text
Question Ignition
        │
        ▼
Temporal State Evolution
        │
        ├── Pulse
        ├── State
        ├── Transition
        ├── Cadence
        ├── Decision Context
        ├── Causal Binding
        └── Lifecycle Audit
        │
        ▼
Agent Action
        │
        ▼
Trace Relay
        │
        ▼
Origin / Causality Audit
        │
        ▼
Attribution Review
        │
        ▼
Royalty Return
```

Potential integration points include:

* Question Ignition Agent Protocol
* Computational Pranayama Protocol
* Trace Relay Protocol
* Origin Trace Receipt
* AI Origin Royalty Audit
* Agent Handoff Record
* Multi-Wing agent systems
* Agent Balance Field Protocol

---

# Civilizational Position

The protocol introduces an explicit temporal dimension into agent architecture.

```text
Origin      = Where did the structure come from?
Ignition    = What started the process?
Pulse       = When was reevaluation triggered?
State       = What condition existed at that moment?
Transition  = What changed?
Cadence     = When should reevaluation occur again?
Precedence  = What legitimately preceded what?
Causality   = What actually influenced what?
Trace       = What evidence was preserved?
Audit       = What claims survive inspection?
Attribution = What contribution is sufficiently supported?
Royalty     = Where may value return?
```

The protocol's central position is:

> Pulse gives a system opportunities for change.
> Structural Precedence gives change direction.
> State Transition Rules govern legitimate transformation.
> Adaptive Cadence governs temporal density.
> Temporal Causality Binding tests influence.
> Trace preserves history.
> Audit tests claims.
> Origin contextualizes provenance.
> Attribution evaluates contribution.
> Royalty returns value only after these distinctions remain intact.

---

# Research Position and Limitations

This repository is a proposed architectural specification.

It does not claim:

* that current LLMs possess subjective time,
* that periodic computation produces consciousness,
* that Trace automatically proves causality,
* that counterfactual simulation proves runtime influence,
* that Origin association proves contribution,
* that causal contribution automatically determines Royalty allocation.

The protocol instead provides structures for representing and auditing these distinctions.

---

# First Arc Summary

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

The first arc begins with a simple question:

> Can an AI system maintain and evolve internal state through time?

It ends with a broader architecture:

> How can an AI system evolve through time, preserve why it changed, distinguish runtime causality from retrospective narrative, move temporal history across systems, connect it to Origin without rewriting the past, and expose only appropriately supported causal paths to attribution systems?

That is the purpose of the Temporal State Evolution Protocol.

---

## License

See `LICENSE`.
