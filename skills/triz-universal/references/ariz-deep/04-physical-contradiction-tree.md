---
description: >-
  Deterministic Decision Tree for Physical Contradictions (ARIZ Table 2): Precise branching logic,
  micro-level particle rules 8-10, phase transitions, and vacuum/void mobilization.
metadata:
  tags: [triz, ariz, table-2, physical-contradiction, decision-tree, particles, vacuum, phase-transition]
  source: ARIZ-85-V (Table 2 & Particle Rules 8-10, Altshuller 1985)
---

# Physical Contradiction Tree (Table 2): Resolving Physical Contradictions

## Prerequisites / Cross-references
This module provides a strict algorithmic protocol for selecting physical and system mechanisms to eliminate Micro-PCs. Basic conceptual descriptions of the 7 separation strategies are documented in [references/03-separation-principles.md](../03-separation-principles.md). This document provides the **deterministic decision tree**, particle rules 8–10, and the void/vacuum mobilization protocol.

---

## Deterministic Decision Tree

```
                       [MICRO-PC: X must be p and NOT-p]
                                       │
         ┌─────────────────────────────┴─────────────────────────────┐
         ▼                                                           ▼
[Spaces Z1 and Z2 SEPARABLE?]                               [Spaces Z1 and Z2 COINCIDE?]
         │                                                           │
         ├─► YES: Branch 1 (Space)                                   │
         │       • Gradients, boundaries                             ▼
         │       • Particle Rule #8                         [Times T1 and T2 SEPARABLE?]
         │                                                           │
         │                                                           ├─► YES: Branch 2 (Time)
         │                                                           │       • Phases, clock cycles
         │                                                           │       • Particle Rule #9
         │                                                           │
         │                                                           ▼
         │                                                  [Times T1 and T2 COINCIDE?]
         │                                                           │
         │                                                           ├─► Branch 3 (Phase Transitions)
         │                                                           │   • Bistability, polymorphism
         │                                                           │
         └───────────────────────────────────────────────────────────┴─► Branch 4 (System Transition)
                                                                         • Mono-Bi-Poly
                                                                         • Particle Rule #10 (Void/Vacuum)
```

---

## Branch 1: Separation in Space ($Z_1 \ne Z_2$)

Condition: Property $p$ is required in sub-zone $Z_1$, while property $\neg p$ is required in sub-zone $Z_2$.

### Algorithmic Protocol:
1. **Localization:** Define boundary between $Z_1$ and $Z_2$ (transition thickness $\to 0$).
2. **Particle Rule #8 (ARIZ-85-V):**
   - "If a macro-object must be simultaneously rigid and permeable (or dense and sparse), it is divided into micro-particles. In zone $Z_1$, particles concentrate into dense clusters, while in zone $Z_2$ they disperse or align edge-on to the flow."
3. **Implementation Examples:**
   - *Software:* Isolating mutable hot-path state into an L1 cache line ($Z_1$), while immutable reference tables sit in read-only shared memory ($Z_2$).
   - *AI Agents:* Working scratchpad workspace ($Z_1$) isolated from tool-calling context ($Z_2$).
   - *Hardware:* Anisotropic materials (conducting heat along fibers, insulating across them).

---

## Branch 2: Separation in Time ($T_1 \ne T_2$)

Condition: Space coincides ($Z_1 = Z_2$), but conflicting requirements occur at different times.

### Algorithmic Protocol:
1. **Clocking:** Fix strict intervals for the active operating phase ($T_1$) and preparatory phase ($T_2$).
2. **Particle Rule #9 (ARIZ-85-V):**
   - "If particles cannot continuously maintain property $p$, replace continuous action with pulsed action (duty cycle $\theta$). During the short pulse $\tau \ll T_1$, particles exhibit extreme property $p$, and return to relaxed state $\neg p$ during the interval. The pulse frequency matches the natural resonance of the system."
3. **Implementation Examples:**
   - *Software:* Batching and Time-slicing — accumulating packets during background window $T_2$ and flushing in parallel bursts during $T_1$.
   - *AI Agents:* Asynchronous pre-caching of vector embeddings during off-peak hours ($T_2$) and sub-millisecond retrieval during peak hours ($T_1$).
   - *Hardware:* Pulsed laser welding or intermittent ultrasonic cavitation.

---

## Branch 3: Separation by Condition and Phase Transitions ($Z_1 = Z_2 \land T_1 = T_2$)

Condition: Space and time coincide strictly; separation across dimensions is impossible.

### Algorithmic Protocol:
1. **Finding Transition Trigger:** Identify an environmental parameter (pressure, temperature, request rate, payload volume) whose shift triggers a step-function phase transition.
2. **Employing Bistable Structures:**
   - Transition elements into a metastable state where a tiny perturbation flips the system from $p$ to $\neg p$.
3. **Implementation Examples:**
   - *Software:* Adaptive data structures (e.g., SkipList shifting into a B-Tree once size crosses a threshold; adaptive spinlocks parking threads under sustained contention).
   - *AI Agents:* Dynamic Chain-of-Thought (CoT) depth: 0 reasoning tokens for routine prompts, switching abruptly to 32k tokens when ambiguity markers appear.
   - *Hardware:* Shape memory alloys (nitinol), ferromagnetic fluids, liquid $\leftrightarrow$ vapor phase change.

---

## Branch 4: System Transition and the Rule of the Void ($Z_1 = Z_2 \land T_1 = T_2$)

Condition: Phase transitions are impossible or physically constrained.

### Algorithmic Protocol:
1. **Level Shift (Micro $\leftrightarrow$ Macro):**
   - At the level of each individual element, property $p$ holds; but the collective forms a supersystem exhibiting property $\neg p$ (or vice versa).
2. **Particle Rule #10 (ARIZ-85-V): Mobilizing the Void:**
   - "If substance or code cannot possess the required property, replace substance/code with **void** (vacuum, air pockets, pauses, null pointers, absence of computation). The void creates zero friction, consumes zero energy, and does not wear out."
3. **Implementation Examples:**
   - *Software:* Sparse bit arrays (Roaring Bitmaps) — storing only non-zero bits; void is omitted from indexing, reducing RAM by 99.9%. Lazy evaluation — computation does not exist until accessed.
   - *AI Agents:* Sparse Attention — attention mechanism leaves voids between unrelated context blocks rather than connecting all tokens to all tokens.
   - *Hardware:* Honeycomb structures, metal foams, vacuum thermal insulation.

---

## Table 2 Decision Matrix

| Operational Zone State | $Z$ and $T$ Relationship | Recommended Mechanism | Key Governing Rule |
|---|---|---|---|
| Conflict localized in space | $Z_1 \ne Z_2$, any $T$ | Zoning, membranes, barriers | **Rule #8 (Particle Clustering)** |
| Conflict localized in time | Any $Z$, $T_1 \ne T_2$ | Clocking, pulses, pauses | **Rule #9 (Pulsed Resonance)** |
| Strict spatial/temporal overlap | $Z_1 = Z_2 \land T_1 = T_2$ | Phase transition, trigger | **Polymorphism / Bistability** |
| Material / code limits exhausted | Boundary condition | Mono $\to$ Poly-system, void | **Rule #10 (Mobilizing the Void)** |
