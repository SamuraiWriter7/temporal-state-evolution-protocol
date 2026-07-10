# Adaptive Cadence Model

## 1. Purpose

The Adaptive Cadence Model defines how a temporal agent determines when its next Pulse should occur.

The model rejects two extremes:

1. permanent high-frequency evaluation,
2. passive inactivity with no reliable wake mechanism.

Instead, cadence is treated as a policy decision derived from state and environmental conditions.

---

## 2. Core Model

```text
State
  +
Risk
  +
Urgency
  +
Unresolvedness
  +
Load
  +
Resource Pressure
  +
External Events
  ↓
Cadence Evaluation
  ↓
Next Pulse Policy

The next Pulse may be:

scheduled,
bounded within a time interval,
triggered by events,
controlled by a hybrid policy,
suspended pending authorization.
3. Clock versus Pulse

A clock advances uniformly.

A Pulse is conditional.

Clock:

tick──tick──tick──tick──tick


Adaptive Pulse:

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

The protocol therefore distinguishes external time measurement from internal temporal policy.

4. State-Dependent Time

The key relation is:

Current State
      ↓
Cadence Decision
      ↓
Next Pulse Timing

A temporal agent does not merely move through time.

Its current condition influences when it evaluates itself again.

This creates a feedback relation:

State(t)
   ↓
Cadence(t)
   ↓
Pulse(t+1)
   ↓
Evaluation(t+1)
   ↓
State(t+1)
5. Computational Pranayama

Adaptive Cadence connects temporal state evolution with computation pacing.

Continuous reasoning is not always optimal.

The system may instead:

reduce Pulse frequency,
enter quiet mode,
enter sleep,
wait for an event,
delegate processing,
release computation pressure,
suspend autonomous activity.

The purpose is not inactivity.

The purpose is proportionate activity.

6. Safety

Adaptive cadence can fail in several directions.

Excessive acceleration may create a Pulse Storm.

Excessive deceleration may create Temporal Starvation.

Rapid mode switching may create Cadence Oscillation.

Permanent activity may exhaust resources.

Permanent sleep may prevent necessary action.

Therefore cadence decisions require:

explicit causes,
policy references,
budget checks,
hysteresis,
wake conditions,
critical-mode limits,
trace binding.
7. Principle

An intelligent system should not think continuously merely because it can.

A temporal system requires the ability to decide:

when to act,
when to observe,
when to reconsider,
when to wait,
when to rest,
when to wake.
