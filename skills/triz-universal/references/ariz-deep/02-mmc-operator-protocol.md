---
description: >-
  MMC Operator Protocol (Modeling with Little People / Smart Little People): Structured role-prompting algorithm
  for microscopic visualization, agentic decomposition, and deadlock resolution in software, AI, and physical systems.
metadata:
  tags: [triz, mmc, slp, little-people, modeling, role-prompting, agentic, micro-level]
  source: ARIZ-85-V (Step 4.5), Altshuller MMC
---

# Smart Little People (SLP / MMC) Operator Protocol

## Prerequisites / Cross-references
The SLP operator is activated at Step 4.5 of ARIZ-85-V or whenever a micro-level physical contradiction is difficult to analyze directly:
- Base ARIZ Protocol: [references/ariz-deep/01a-ariz-85v-analysis.md](01a-ariz-85v-analysis.md)
- Contradictions Guide: [references/02-contradictions.md](../02-contradictions.md)
- Physical Contradiction Tree: [references/ariz-deep/04-physical-contradiction-tree.md](04-physical-contradiction-tree.md)

---

## Method Essence & Multi-Agent Mapping

The Smart Little People (SLP / MMC) method was formulated by Genrikh Altshuller to overcome psychological inertia caused by the perceived indivisibility of macro-objects.
In modern AI agent and software architectures, SLP operates as **Structured Role-Prompting / Multi-Agent Simulation**:
- Instead of analyzing monolithic blocks, the system is modeled as a collective of independent, intelligent micro-agents ("little people").
- Each agent has localized vision, local memory, and simple operational rules.
- This immediately reveals race conditions, deadlocks, lock contention, and coordination bottlenecks.

---

## 5-Step SLP Algorithmic Protocol

```
[Step 1: Group Demarcation] ──► [Step 2: Conflict Schema] ──► [Step 3: Ideal Action]
                                                                        │
[Step 5: Reverse Translation] ◄── [Step 4: Reorganization Rules 1–4] ◄──┘
```

### Step 1. Demarcating Conflict Zone & Populating with Little People
1. Bound the Operational Zone (OZ).
2. Replace conflicting macro-objects with collectives of smart little people:
   - **Group A (Product People):** Constitute the body or structure of the Product (data bytes, database rows, pixels, crystal lattice atoms).
   - **Group B (Tool People):** Apply the action (worker threads, heat flux, validators, network packets).
   - **Group C (Environment People):** Populate the space around the OZ (OS page buffer, background traffic, ambient thermal flux).

### Step 2. Constructing Static Conflict Schema
Answer from the perspective of the little people:
- Where are Group A and Group B standing?
- What are their hands and feet doing?
- Why does a crush or collision occur? (e.g., "Group B people try to grab Group A people's hands, but Group A people run too fast and stumble").
- Record: **What constitutes the physical obstacle at the micro-level**.

### Step 3. Constructing Dynamic Ideal Action Schema
Visualize the ideal interaction:
- How should the little people coordinate so that useful work completes instantaneously without harm?
- *Canonical IFR image in SLP:* "The little people step aside spontaneously to let the stream through, or pass items hand-to-hand down a chain without moving from their positions."

### Step 4. Applying 4 Canonical Reorganization Rules
If the ideal state does not emerge automatically, apply the 4 rules sequentially:

1. **Sub-group Specialization:**
   - Divide the homogeneous crowd into two specialized squads: one holds the defensive perimeter, the other performs useful work (or alternate even/odd clock cycles).
2. **Freeing Hands (Remote Action):**
   - If agents are tied up wrestling with each other, switch to remote interactions: throwing balls (fields, events, interrupts) instead of hand-to-hand contact.
3. **Engaging Intermediaries (Free Environment People):**
   - Insert neutral Group C agents between fighting Groups A and B to absorb friction or buffer throughput.
4. **Turning Saboteurs into Helpers:**
   - Channel aggressive disruptive agents into productive work (e.g., using impact energy for self-locking, using parasitic traffic for pre-warming caches).

### Step 5. Reverse Decoding into Engineering Architecture
Translate little people behavior back into technical specifications:
- *"People step aside"* $\longrightarrow$ Logical sharding, sparse matrices, spatial data partitioning.
- *"Pass hand-to-hand without moving"* $\longrightarrow$ Ring buffer, zero-copy pointer handoff, task pipelining.
- *"Throwing balls instead of fighting"* $\longrightarrow$ Event-driven architecture, asynchronous message queues, signals.
- *"Wearing frictionless suits"* $\longrightarrow$ Anti-friction layers, namespace isolation, virtualization boundaries.

---

## Practical Scenarios

### Scenario 1: Resolving Lock Contention in Concurrent Hash Maps
- **Conflict:** 100 threads write concurrently into a single table.
- **SLP Model:** A crowd of 100 thread-agents rushes to enter a single warehouse door (mutex).
- **Ideal SLP Action:** Cut 16 distinct doors into the warehouse (Striping), or have agents leave notes in mailboxes outside without entering.
- **Decoding:** Striped Locking or lock-free atomic queues based on Compare-And-Swap (CAS) instructions.

### Scenario 2: Hallucination & System Prompt Drift in Long-Context LLMs
- **Conflict:** Across long contexts, the agent drops security constraints during complex queries.
- **SLP Model:** An agent-reader reads a 20-meter scroll. By the time it reaches the end, the security instruction agent at the top has fallen asleep out of view.
- **Ideal SLP Action:** The security guard agent does not sit at the scroll top; it perches directly on the reader's glasses, inspecting each word exiting its mouth.
- **Decoding:** Extracting safety verification from prompt tokens into an independent runtime output guardrail layer analyzing generated tokens via fast AST/token filters.

---

## SLP Prompt Template for AI Agents

```markdown
### 👥 Smart Little People (SLP / MMC) Modeling
1. **Agent Groups:**
   - Group A (Product): [Identity, population count, objects in hands]
   - Group B (Tool): [Identity, origin, operating objective]
   - Group C (Environment): [Resources around the conflict zone]
2. **Micro-level Conflict Dynamics:** [Why little people collide / what impedes them]
3. **Ideal Coordinated Action:** [How little people coordinate effortlessly without delay]
4. **Applied Reorganization Rule (1–4):** [Specialization | Remote Action | Intermediary | Saboteur-to-Helper]
5. **Engineering Implementation:** [Technical mechanism realizing the little people behavior]
```
