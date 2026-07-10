# Temporal State Evolution Protocol

**A protocol for time-evolving AI agent states, adaptive pulse cadence, structural precedence, causal transitions, and auditable temporal histories.**

## Overview

Most AI systems can preserve data, retrieve memories, and execute sequences of actions.

However, memory is not the same as temporal continuity.

A system may remember a previous event without representing:

* why the previous state led to the current state,
* what structure enabled the transition,
* what caused the system to evaluate itself at that moment,
* which causal relation should be preserved for later audit.

The **Temporal State Evolution Protocol** defines a protocol layer for representing AI agent state as an evolving temporal process.

Its foundational model is:

```text
Ignition
    ↓
Pulse
    ↓
State Evaluation
    ↓
Transition
    ↓
Next State
    ↓
Trace
    ↓
Next Pulse
```

The protocol does not claim that an AI system possesses subjective time or consciousness.

Instead, it defines a machine-readable structure for:

* explicit pulse events,
* versioned state evolution,
* directed state transitions,
* structural precedence,
* causal evidence binding,
* future temporal audit.

---

## Core Principle

> Time order alone is not causality.

The fact that event A occurred before event B does not prove that A caused B.

Temporal State Evolution therefore separates:

### Local Precedence

Direct state transition causality.

```text
State(t)
    ↓
Transition
    ↓
State(t+1)
```

### Structural Precedence

A prerequisite structure enables, constrains, authorizes, or conditions a later transition.

```text
Policy
    ↓
Allowed Transition Space
    ↓
Action
```

### Ontological Precedence

An origin, source, foundational rule, or contribution basis makes a later derivative process possible.

```text
Origin
    ↓
Derivative Structure
    ↓
Temporal State Evolution
```

These three levels form the basis of the **Structural Precedence Model**.

---

## Why Pulse?

A timestamp tells us when a record was written.

A Pulse Record tells us:

* why evaluation occurred,
* which state was active,
* whether the state changed,
* what caused the transition,
* what should happen next.

The protocol therefore treats a pulse as:

> A discrete opportunity for an agent or system to evaluate its current state and determine whether to retain, transform, accelerate, slow, suspend, or escalate its activity.

A pulse does not require a state change.

A valid result may be:

```text
retain
transition
accelerate
decelerate
sleep
wake
escalate
request_human_review
```

The important requirement is that meaningful temporal decisions remain traceable.

---

## v0.1 Scope

Version 0.1 introduces two foundations:

### Pulse Record

A machine-readable record describing:

* pulse identity,
* temporal sequence,
* trigger,
* previous state,
* evaluation,
* transition result,
* next state,
* cadence mode,
* precedence claims.

### Structural Precedence Foundation

A model for expressing directed relations between:

* states,
* transitions,
* structures,
* policies,
* origins,
* actions,
* traces,
* audits,
* future value attribution.

Version 0.1 does not define a complete autonomous scheduling engine.

It defines the records and causal relationships required for later temporal orchestration.

---

## Example

```yaml
schema_version: "0.1.0"

pulse:
  pulse_id: "pulse-0001"
  agent_id: "agent-alpha"
  sequence_number: 1
  observed_at: "2026-07-08T03:30:00Z"

  trigger:
    type: "external_input"
    reference: "question-0001"

  previous_state_ref: "state-0000"

  evaluation:
    result: "transition"
    reason: >
      A new structural question requires the agent
      to create a temporal causal model.

  transition:
    transition_id: "transition-0001"
    from_state_ref: "state-0000"
    to_state_ref: "state-0001"

  cadence:
    mode: "active"
    next_pulse_policy: "evaluation_required"

  precedence_claims:
    - claim_id: "precedence-0001"
      precedence_level: "local"
      predecessor_ref: "state-0000"
      successor_ref: "state-0001"
      relation_type: "transitions_to"
```

---

## Protocol Position

Temporal State Evolution is designed to connect with other protocol layers.

```text
Question Ignition
        │
        ▼
Temporal State Evolution
        │
        ├── Pulse
        ├── State
        ├── Evaluation
        ├── Transition
        └── Precedence
        │
        ▼
Agent Action
        │
        ▼
Trace Relay
        │
        ▼
Causality Audit
        │
        ▼
Origin Attribution
        │
        ▼
Royalty Return
```

The protocol introduces a missing dimension into agent architecture:

> not only what happened, but how a system moved from one state to another through time.

---

## Design Philosophy

An AI system does not obtain meaningful temporal structure merely by counting ticks.

Meaningful temporal history begins when the system can preserve:

1. what existed before,
2. what triggered evaluation,
3. what changed,
4. what enabled the change,
5. what resulted from the change,
6. what evidence preserves the relationship.

The goal of this repository is to make that history explicit, interoperable, and auditable.

---

## Version Roadmap

### v0.1 — Pulse Record & Structural Precedence Foundation

Define the minimum temporal event and causal direction model.

### v0.2 — State Transition Rule

Define transition authorization, retention, branching, and state lineage.

### v0.3 — Adaptive Cadence Policy

Define state-aware pulse frequency, rest, acceleration, and computational breathing.

### v0.4 — Temporal Causality Binding

Bind temporal states, decisions, actions, and causal evidence.

### v0.5 — Trace & Audit Bridge

Connect temporal histories with Trace, Origin, Causality Audit, and attribution systems.

---

## Status

Experimental specification.

The protocol is intended for research, architectural exploration, and interoperability experiments involving AI agents, multi-agent systems, temporal state machines, causal trace systems, and auditable agent infrastructure.

## License

See `LICENSE`.
