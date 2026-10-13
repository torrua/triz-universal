---
description: >-
  ARIZ-85-V Parts 1-4: Deterministic algorithmic protocol from initial problem situation
  to Product-Tool pair, T1/T2 time demarcation, Macro/Micro Physical Contradiction, and IFR-2.
metadata:
  tags: [triz, ariz, ariz-85v, mini-problem, product-tool, contradiction, ifr, vpr, micro-pc]
  source: ARIZ-85-V (Altshuller, 1985)
---

# ARIZ-85-V. Parts 1–4: Problem Analysis, Model, IFR and Physical Contradiction

## Prerequisites / Cross-references
Before proceeding to the deep ARIZ-85-V cycle, ensure the problem is of level 4–5 complexity and cannot be solved with standard patterns:
- Base ARIZ-AI Algorithm: [references/04-ariz-lite-algorithm.md](../04-ariz-lite-algorithm.md)
- Ideality and IFR formulations: [references/01-ikr-ideality.md](../01-ikr-ideality.md)
- Sharpening Contradictions: [references/02-contradictions.md](../02-contradictions.md)
- Substance-Field Resource Audit (VPR): [references/07-resource-audit-vpr.md](../07-resource-audit-vpr.md)
- Resolution Cycle (Parts 5–9): [references/ariz-deep/01b-ariz-85v-resolution.md](01b-ariz-85v-resolution.md)
- Smart Little People (SLP/MMC) Operator: [references/ariz-deep/02-mmc-operator-protocol.md](02-mmc-operator-protocol.md)
- Step Back from IFR: [references/ariz-deep/03-step-back-from-ifr.md](03-step-back-from-ifr.md)

---

## Part 1. Problem Analysis

The goal of Part 1 is transitioning from a vague problem situation to an ultra-sharp model of the problem with a free X-element.

### Step 1.1. Mini-Problem & De-specialization ("Plain Language")
1. Identify the technical system, its primary useful function, and the undesirable effect.
2. Formulate the **mini-problem**:
   - "Everything remains unchanged or is simplified, but the harmful effect disappears or the required useful action appears without adding new external mechanisms, servers, budget, or personnel."
3. **De-specialization Rule:**
   - Reformulate the problem statement by stripping away narrow technical jargon (protocol names, specialized framework names, obscure library names).
   - Replace them with intuitive conceptual equivalents: *"box", "rope", "signal", "valve", "stream", "queue", "note", "guard"*.
   - **Why for LLMs:** Domain jargon activates overfitted training weights, driving the model toward conventional compromises. De-specialization breaks associative psychological inertia.

### Step 1.2. Identifying the Conflicting Element Pair
Isolate exactly two interacting elements from the system:
1. **Product (Element 1):** The element that must be processed, moved, preserved, protected, or whose state must be changed.
   - *Software/AI:* User payload, network packet, transactional state, prompt text.
   - *Hardware:* Physical workpiece, sensor diode, protected component.
2. **Tool (Element 2):** The element that directly interacts with the Product, producing a useful or harmful effect.
   - *Software/AI:* Execution thread, scheduler, validator, cache layer, LLM parser.
   - *Hardware:* Cutting tool, coolant fluid, laser beam, fastening bolt.

### Step 1.3. Formulating Paired Technical Contradictions (TC-1 and TC-2)
Formulate two diametrically opposed states of the tool:
- **TC-1 (Maximum Useful Action):** If the tool is in state $S_1$ (amplified, accelerated, densified), the required useful action $F_{\text{good}}$ is achieved, but an unacceptable worsening $F_{\text{harm}}$ occurs.
- **TC-2 (Minimum Harmful Action):** If the tool is in state $S_2$ (weakened, removed, dissipated), the harmful effect $F_{\text{harm}}$ is completely eliminated, but the useful action $F_{\text{good}}$ is not performed.

### Step 1.4. Selecting the Primary TC by Main Production Parameter
Choose the TC that preserves the **Main Performance Metric** of the system:
- If the primary goal is maximum throughput or speed, select TC-1 (amplified action), and eliminate the accompanying harm.
- If the primary goal is extreme reliability, safety, or zero cost, select TC-2 (elimination of harm), and restore the useful action.

### Step 1.5. Extreme Sharpening of the Conflict
Push the tool state in the chosen TC to its absolute limit:
- Not "high load", but "one billion concurrent requests per second".
- Not "high temperature", but "instant thermal vaporization".
- Not "low memory", but "zero free bytes".
- Record the extreme state: the tool performs the useful action perfectly, but completely destroys the product (or vice versa).

### Step 1.6. Formulating the Problem Model with the X-Element
Write down the canonical model formulation:
> **Given:** Conflicting pair — Product `[Name]` and Tool `[Name]`.
> **Conflict:** Under extreme tool state, harmful action `[Harm]` occurs.
> **Required:** Find an unknown **X-element** that, while preserving the tool's ability to provide `[Useful Action]`, completely eliminates the harmful effect on the product without complicating the system.

### Step 1.7. Express Check via Standard Solutions
Check if the problem model matches standard Su-Field transformation classes (see [references/09-su-field-and-standards.md](../09-su-field-and-standards.md)). If no standard applies, proceed to Part 2.

---

## Part 2. Analysis of the Problem Model

### Step 2.1. Defining the Operational Zone (OZ)
Define the precise spatial boundary where the conflicting interaction occurs:
- **OZ is the contact surface:** a thin boundary layer, a CPU cache line, a mutex critical section, a single HTTP payload body, a 20-token context window slice.
- Exclude all areas outside the OZ from consideration.

### Step 2.2. Defining Operational Time (OT: $T_1$ and $T_2$)
Divide the process timeline into two non-overlapping intervals:
1. **Conflict Period ($T_1$):** Time of direct harmful or required action (milliseconds of operation execution, CPU clock cycle, moment of impact).
2. **Pre-conflict Period ($T_2$):** Time of preparation, idle state, waiting, or movement before contact.
- *Record durations:* $T_1 = [\dots]$, $T_2 = [\dots]$.

### Step 2.3. Substance-Field Resource Audit (VPR)
Audit available resources strictly within or adjacent to the OZ:
- Resources of the Product itself (internal structure, voids, wastes, parameters).
- Resources of the Tool (fields, heat, electrical potential, timing reserves).
- Resources of the Environment (pressure, dissipated energy, OS kernel syscalls, client-side compute).

---

## Part 3. Formulating IFR and the Physical Contradiction (PC)

### Step 3.1. Canonical IFR-1 Formulation
Formulate IFR-1 using the strict ARIZ equation:
> The **X-element**, without complicating the system or introducing harmful side effects, **by itself** during time **$T_1$** within the **OZ** eliminates `[Harmful action]`, fully preserving the tool's capability to deliver `[Useful action]`.

### Step 3.2. IFR-1 Candidate Hierarchy
No new external components are allowed. Test candidate resources in strict order of priority:
1. Resource of the Product itself.
2. Resource of the Tool.
3. Resource of the Environment / Supersystem.
4. "Void" (vacuum, idle intervals, zero bytes, absence of matter/code).

### Step 3.3. Macro-PC Formulation
Formulate the physical contradiction for the entire Operational Zone:
- "The Operational Zone OZ during time $T_1$ must have macro-property **[P]** to perform the useful function, and must have macro-property **[$\neg P$]** to prevent the harmful effect."

### Step 3.4. Micro-PC Formulation
Translate the contradiction from macro-level to micro-level (particles, bits, events, fibers):
- "Particles of matter/data in the Operational Zone OZ must be in state **$p$** (e.g., free, sparse, unlinked) to ensure property [P], and must be in state **$\neg p$** (linked, dense, monolithic) to ensure property [$\neg P$]."
- **Why this is mandatory:** According to Altshuller's research, transitioning from macro to micro increases difficult problem solvability from 15% to 85%.

### Step 3.5. Formulating IFR-2
Formulate IFR-2 connecting microstate and action:
> "The Operational Zone **OZ itself** via its internal micro-particles transitions to state **$p$** during $T_1$ under condition $C_1$, and returns to state **$\neg p$** during $T_2$ or under condition $C_2$."

### Step 3.6. 6 Rules for Working with an "Immutable" Product
If the Product cannot be modified directly:
1. **Rule 1 (Self-Modification):** The product temporarily modifies itself under an available field or natural process.
2. **Rule 2 (Expendable Micro-fraction):** Modify a thin surface layer or ephemeral memory snapshot, then discard or regenerate it.
3. **Rule 3 (Transfer to Supersystem):** Act on the surrounding medium rather than the product directly (execution context, environment pressure).
4. **Rule 4 (Microstructural Shift):** Change the internal logical/aggregate state (bitmask, polarization, timestamp) rather than external geometry.
5. **Rule 5 (Using Voids):** Localize action in natural cavities, gaps, pauses, or unused padding bits.
6. **Rule 6 (Phase Separation in Time):** Modify the product only in $T_2$ (pre-conflict) and fully restore it by the end of $T_1$.

---

## Part 4. Mobilization and Application of VPR

### Step 4.1. Smart Little People (SLP/MMC) Method
If the particle interaction in the OZ remains unclear:
- Launch the protocol in [references/ariz-deep/02-mmc-operator-protocol.md](02-mmc-operator-protocol.md).
- Model particles as "smart little people" (Groups A, B, C) during $T_1$ and apply troop reorganization rules.

### Step 4.2. Step Back from IFR
If absolute ideality blocks resolution and demands the impossible:
- Launch protocol in [references/ariz-deep/03-step-back-from-ifr.md](03-step-back-from-ifr.md).
- Introduce a minimal controlled dismantling defect or allow an ephemeral compromise in $T_2$ that is eliminated by the end of $T_1$.

### Step 4.3. Mobilizing VPR, Voids, and Derived Resources
| Resource Type | Where to Look in OZ | System / Software Examples |
|---|---|---|
| **Substance / Memory** | Unused fields, calculation waste, cache lines | Ring buffer in RAM, struct padding bytes |
| **Field / Energy** | Heat dissipation, interrupts, backpressure | Backpressure signal as throttle mechanism |
| **Time** | Inter-packet gaps, CPU idle cycles | Pre-computing in background worker during $T_2$ |
| **Space** | Memory boundaries, unused page blocks | Partitioning, NUMA-aware data localization |
| **Information** | Header metadata, stream sequence ordering | Idempotency keys, monotonically increasing counters |

### Step 4.4. Evaluating the Solution Concept
If a concept eliminating the PC without adding new components is found:
- Proceed to **Part 7** (Analysis and Verification) in [01b-ariz-85v-resolution.md](01b-ariz-85v-resolution.md).
If no solution is reached:
- Proceed to **Parts 5 and 6** (Information Fund and Deadlock Protocol) in [01b-ariz-85v-resolution.md](01b-ariz-85v-resolution.md).

---

## Artifact Checklist for Parts 1–4
Before proceeding, record the following artifacts:
- [ ] Mini-problem in plain language.
- [ ] Conflicting pair: Product `[...]` and Tool `[...]`.
- [ ] Primary TC and extreme state.
- [ ] Operational Zone (OZ) and Operational Time ($T_1$ and $T_2$).
- [ ] Macro-PC and Micro-PC statements.
- [ ] IFR-2 formulation.
- [ ] Verified Product Rule (1–6).
