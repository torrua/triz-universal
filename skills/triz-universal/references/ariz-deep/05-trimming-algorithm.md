---
description: >-
  Trimming Algorithm Protocol: Systematic functional pruning of redundant components,
  subsystems, and architectural layers using canonical Rules A, B, and C to maximize ideality.
metadata:
  tags: [triz, trimming, pruning, ideality, functional-analysis, simplification, architecture]
  source: Modern TRIZ (Litvin, Gerasimov, Axelrod)
---

# Functional Trimming Protocol

## Prerequisites / Cross-references
Trimming is the primary TRIZ mechanism for increasing system ideality by eliminating intermediate components without losing functionality:
- Ideality calculation & IFR equations: [references/01-ikr-ideality.md](../01-ikr-ideality.md)
- Substance-Field Resource Audit (VPR): [references/07-resource-audit-vpr.md](../07-resource-audit-vpr.md)
- Supersystem analysis (9 Screens): [references/06-system-operator-9screens.md](../06-system-operator-9screens.md)

---

## 5-Step Trimming Algorithmic Protocol

```
[Step 1: Functional Model] ──► [Step 2: Target Selection] ──► [Step 3: Test Rules A, B, C]
                                                                        │
[Step 5: Ideality Gain] ◄──── [Step 4: Resolve Secondary PCs] ◄────────┘
```

### Step 1. Constructing the Functional Model
1. Decompose the system into components and map all interactions into triads:
   $$\mathbf{[\text{Subject Component}]} \xrightarrow{\quad\text{Action (Function)}\quad} \mathbf{[\text{Target Object}]}$$
2. Classify each function:
   - **Primary (Useful):** The raison d'être of the system.
   - **Auxiliary (Servicing):** Exists solely to assist or sustain other components.
   - **Harmful (Parasitic):** Introduces latency, consumes memory, produces wear, or induces bugs.

### Step 2. Selecting the Trimming Target
Prioritize trimming candidates in the following order:
1. Components generating the largest number of harmful or parasitic functions.
2. Components performing exclusively auxiliary functions (bridges, adapters, intermediate queues, type converters).
3. Components with the highest cost, power consumption, or maintenance overhead.

### Step 3. Testing the 3 Canonical Trimming Rules

Attempt to trim target component $K$ using one of the three rules:

#### Rule A: Eliminating the Need for the Function
- *Condition:* The useful function of component $K$ is no longer required by the system.
- *Mechanism:* Eliminate the object of the function or restructure the upstream process so that the need for processing vanishes.
- *Example:* If an in-memory cache exists only to mask slow JSON deserialization, switching to flat zero-copy binary formats (FlatBuffers/Cap'n Proto) completely eliminates the need for the caching layer.

#### Rule B: The Object Performs the Function Itself (Self-Service)
- *Condition:* The target object assumes the function of trimmed component $K$.
- *Mechanism:* Mobilize the internal resources, structure, or geometry of the object.
- *Example:* Instead of a centralized token validation service, each downstream worker cryptographically validates JWT signatures locally in 1 microsecond using an embedded public key.

#### Rule C: Function Transferred to Another Component or Supersystem
- *Condition:* Neither Rule A nor Rule B applies; the function is objectively necessary.
- *Mechanism:* Transfer the function of trimmed component $K$ to an existing element (or external environment/supersystem) that has idle capacity.
- *Example:* Trimming a dedicated load balancer reverse-proxy by shifting traffic distribution to DNS round-robin, Anycast BGP routing, or Linux kernel packet filtering (`eBPF` / `XDP`).

### Step 4. Identifying and Resolving Secondary Contradictions
Trimming a component often triggers a secondary defect (e.g., "trimmed RabbitMQ — now sudden traffic bursts overload the database"):
- Restoring the trimmed component is forbidden!
- Formulate the resulting obstacle as a compact secondary technical/physical contradiction.
- Eliminate it using the base ARIZ protocol ([references/ariz-deep/01a-ariz-85v-analysis.md](01a-ariz-85v-analysis.md)) by mobilizing latent VPR resources.

### Step 5. Evaluating Ideality Gain
Evaluate the outcome:
$$I = \frac{\sum F_{\text{useful}}}{\sum C_{\text{cost}} + \sum H_{\text{harm}}}$$
- Verify that node count, external dependencies, and network hops decreased while reliability and latency SLAs remained constant or improved.

---

## Architectural Case Studies

### Case 1: Trimming Kafka/RabbitMQ in Event-Driven Architecture
- **Baseline:** Order service publishes events to Kafka; Analytics service consumes them. Costs: ZooKeeper/Kafka cluster maintenance, network latency, serialization serialization.
- **Trimming via Rule C (Transfer to existing component):**
  - Use the Order database itself as the event delivery engine via Change Data Capture (PostgreSQL WAL Logical Replication).
- **Outcome:** Kafka cluster trimmed (0 dedicated servers, $0 broker hosting cost); events stream at transactional write speed.

### Case 2: Trimming Intermediate Orchestration Subagents
- **Baseline:** Multi-agent pipeline with Planner Agent $\to$ Research Agent $\to$ Writer Agent $\to$ Reviewer Agent. Costs: 4x token burn, high end-to-end latency.
- **Trimming via Rules B & C:**
  - Trim Planner and Reviewer agents. Embed their requirements directly into structured JSON schemas and system guardrails of the core executor agent.
- **Outcome:** 2 agent hops eliminated, end-to-end latency reduced by 65%, context-passing hallucinations prevented.

---

## Trimming Checklist
- [ ] Functional triad model constructed ("Subject $\to$ Action $\to$ Target")?
- [ ] Candidate selection justified (parasitic/auxiliary node)?
- [ ] Winning rule identified: **A** (need eliminated), **B** (self-service), or **C** (function transferred)?
- [ ] Secondary contradictions resolved without re-introducing trimmed components?
- [ ] Measurable ideality increase verified?
