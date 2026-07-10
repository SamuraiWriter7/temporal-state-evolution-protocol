# Changelog

All notable changes to the Temporal State Evolution Protocol will be documented in this file.

The format is based on a versioned candidate specification model.

## [0.1.0-candidate] - 2026-07-08

### Added

* Initial Temporal State Evolution Protocol structure.
* Pulse Record data model.
* Structural Precedence Core specification.
* Three-level precedence hierarchy:

  * Local Precedence
  * Structural Precedence
  * Ontological Precedence
* Pulse trigger model.
* State evaluation result model.
* Transition binding structure.
* Initial cadence mode vocabulary.
* Precedence assertion modes.
* Initial Precedence Consistency Check requirements.
* Failure mode definitions for:

  * Precedence Collapse
  * Temporal Illusion
  * Causal Direction Inversion
  * Retroactive Origin Injection
  * Precedence Cycle
* Example Pulse Record.

### Design Principle

Version 0.1 establishes the minimum relationship:

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

The protocol distinguishes chronological order from causal direction.

A prior timestamp alone does not establish precedence.

Temporal history becomes structurally meaningful only when transitions, prerequisites, and origins can be represented as explicit directed relations.

### Next

Version 0.2 will define the State Transition Rule layer, including:

* state retention,
* authorized transition,
* transition rejection,
* state lineage,
* branching,
* fork semantics,
* supersession,
* reconciliation.
