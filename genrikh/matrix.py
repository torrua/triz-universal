"""
TRIZ Contradiction Matrix & 40 Inventive Principles catalog.
Adapted for modern Software Engineering, Hardware, AI Agents, and Business Systems.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class Principle:
    id: int
    name_en: str
    classical: str
    software: str
    business: str

@dataclass
class Parameter:
    id: int
    name_en: str
    software: str
    business: str

# 40 Inventive Principles Catalog
PRINCIPLES: Dict[int, Principle] = {
    1: Principle(
        1, "Segmentation",
        "Divide an object into independent parts; make it sectional.",
        "Microservices, database sharding, pagination, SIMD data parallelism.",
        "Modular subscription pricing, dividing large projects into autonomous squads."
    ),
    2: Principle(
        2, "Taking Out / Extraction",
        "Extract only the necessary part or property; separate disturbing parts.",
        "Separation of Concerns (SoC); offload CPU tasks to worker threads; GraphQL sparse fields.",
        "Outsourcing non-core commoditized operations; unbundling complex product suites."
    ),
    3: Principle(
        3, "Local Quality",
        "Transition from uniform to non-uniform structure; give each part specialized function.",
        "Hot/cold memory tiering; indexing only active rows (partial indexes); inner loops in Rust/C.",
        "VIP customer onboarding tracks; tier-based service level agreements (SLAs)."
    ),
    4: Principle(
        4, "Asymmetry",
        "Replace symmetrical form with asymmetrical.",
        "CQRS (asymmetric read vs write data models); public/private keys; read replicas.",
        "Freemium monetization asymmetry (free for consumers, paid for merchants)."
    ),
    5: Principle(
        5, "Merging / Consolidation",
        "Combine identical or related objects; perform parallel operations.",
        "Bulk database operations; HTTP/2 stream multiplexing; connection pooling.",
        "Mergers & acquisitions; co-marketing partnerships; bundling complementary services."
    ),
    6: Principle(
        6, "Universality",
        "Make an object perform multiple functions, eliminating other parts.",
        "Generic programming (generics, templates); multi-purpose protocols (gRPC).",
        "Full-stack cross-functional teams; multi-purpose mobile super-apps (WeChat)."
    ),
    7: Principle(
        7, "'Nested Doll' (Matryoshka)",
        "Place one object inside another, which is placed inside another.",
        "Middleware chains; layered network protocols (OSI stack); containers in VMs.",
        "Subsidiarity in corporate hierarchy; nested product ecosystems (Apple ecosystem)."
    ),
    8: Principle(
        8, "Anti-Weight / Counterweight",
        "Compensate for weight by combining with lifting force.",
        "Reactive Streams backpressure; circuit breakers shedding load; GC reference balancing.",
        "Hedging financial downside with inverse derivatives; escrow milestone releases."
    ),
    9: Principle(
        9, "Preliminary Anti-Action",
        "If action causes harmful effects, apply opposing action beforehand.",
        "Defensive input sanitization; Zod schema validation; token bucket rate limiting.",
        "Non-disclosure agreements (NDAs) before pitches; pre-mortems before project launch."
    ),
    10: Principle(
        10, "Preliminary Action",
        "Perform required action (fully or partially) in advance.",
        "Static Site Generation (SSG); pre-fetching; JIT warm-up; materialized views.",
        "Pre-ordering and Kickstarter campaigns to validate demand before manufacturing."
    ),
    11: Principle(
        11, "Cushion in Advance",
        "Compensate for low reliability by preparing emergency countermeasures.",
        "Retry with exponential backoff and jitter; dead-letter queues (DLQ); fallback cache.",
        "Emergency credit lines; contingency disaster recovery protocols; indemnity clauses."
    ),
    12: Principle(
        12, "Equipotentiality",
        "Avoid lifting or lowering objects in potential field.",
        "Zero-copy kernel buffers (sendfile, io_uring); stateless web tiers behind balancers.",
        "Flat organizational hierarchy; lateral internal career mobility without salary cliffs."
    ),
    13: Principle(
        13, "The Other Way Around",
        "Invert the action; make moving parts fixed and fixed parts moving.",
        "Inversion of Control (IoC); Dependency Injection; Reactive pull streams; TDD.",
        "Reverse auctions (buyers set price, suppliers bid); user-generated content models."
    ),
    14: Principle(
        14, "Spheroidality / Curvature",
        "Replace flat surfaces with curved; linear motion with rotary.",
        "Ring buffers (LMAX Disruptor) for lock-free IPC; circular event loops; token buckets.",
        "Continuous feedback loops instead of annual reviews; cyclical product release trains."
    ),
    15: Principle(
        15, "Dynamics",
        "Make an object or process adapt dynamically to changing conditions.",
        "Feature flags; dynamic config reload without restart; autoscaling compute pods.",
        "Surge pricing (Uber); agile sprint reallocation based on live customer metrics."
    ),
    16: Principle(
        16, "Partial or Excessive Action",
        "If 100% is hard, do slightly less or slightly more to simplify.",
        "Optimistic UI updates; Bloom filters (probabilistic set testing); branch prediction.",
        "Minimal Viable Product (MVP) testing; over-subscribing initial waitlist invites."
    ),
    17: Principle(
        17, "Another Dimension",
        "Move from 1D to 2D/3D; use multi-story or spatial arrangements.",
        "Switching row-oriented to columnar storage (ClickHouse/DuckDB); GPU vectorization.",
        "Pivoting from 1D transactional sales to 2D platform marketplace ecosystem."
    ),
    18: Principle(
        18, "Mechanical Vibration",
        "Cause an object to oscillate or vibrate.",
        "Random jitter in network retries; node heartbeats; replacing polling with events.",
        "Pulse surveys to measure employee morale; periodic flash promotions."
    ),
    19: Principle(
        19, "Periodic Action",
        "Replace continuous action with periodic or pulsed action.",
        "Scheduled cron jobs; micro-batching flushes every 10ms; controller reconciliation.",
        "Bi-weekly sprint retrospectives; quarterly board reviews; seasonal marketing drops."
    ),
    20: Principle(
        20, "Continuity of Useful Action",
        "Keep all parts working at full capacity without idle intervals.",
        "Streaming data pipelines; non-blocking async I/O (epoll, io_uring); pipelining.",
        "24/7 global follow-the-sun customer support across distributed timezones."
    ),
    21: Principle(
        21, "Skipping / Hurrying Through",
        "Conduct process at high speed to pass through dangerous stages.",
        "Short-circuit boolean evaluation; fail-fast validation; speculative fast-path bypass.",
        "Blitzscaling to achieve network effects before competitors can react."
    ),
    22: Principle(
        22, "Blessing in Disguise",
        "Use harmful factors to achieve positive effect.",
        "Chaos engineering (breaking nodes to expose bugs); traffic spikes warming caches.",
        "Turning a public PR crisis into a transparency showcase that builds customer trust."
    ),
    23: Principle(
        23, "Feedback",
        "Introduce feedback to improve process or action.",
        "Closed-loop PID autoscalers; TCP congestion control (BBR); adaptive query planning.",
        "Net Promoter Score (NPS) telemetry driving product roadmap prioritizations."
    ),
    24: Principle(
        24, "Intermediary",
        "Use intermediate carrier or process to transfer action.",
        "Reverse proxies (Envoy/Nginx); message brokers (Kafka); Adapter/Facade patterns.",
        "Merchant of Record (Stripe/Paddle) handling global VAT compliance for SaaS."
    ),
    25: Principle(
        25, "Self-Service",
        "Make object service itself by performing auxiliary operations.",
        "Kubernetes self-healing restarts; autonomous index defragmentation; OpenAPI.",
        "Customer self-serve knowledge base; automated password reset flows."
    ),
    26: Principle(
        26, "Copying",
        "Use simple/cheap copy instead of fragile or expensive original.",
        "Read replicas; CDN edge caching; database snapshots; digital twin test environments.",
        "Staging environments mirroring production; simulation war-games for executive strategy."
    ),
    27: Principle(
        27, "Cheap Short-Living Objects",
        "Replace expensive durable object with multiple cheap, ephemeral ones.",
        "Ephemeral serverless functions (AWS Lambda); immutable data structures.",
        "Disposable pop-up stores; temporary contractor teams for exploratory spikes."
    ),
    28: Principle(
        28, "Mechanics Substitution",
        "Replace mechanical system with optical, acoustic, or electrical.",
        "Replacing busy polling with WebSockets; replacing context switches with eBPF.",
        "Replacing physical paper signatures with cryptographic electronic signatures."
    ),
    29: Principle(
        29, "Pneumatics & Hydraulics",
        "Use gas or liquid parts instead of solid parts.",
        "Elastic reactive stream buffers; fluid traffic shaping with leaky bucket algorithms.",
        "Elastic compensation budgets that adjust fluidly to team performance."
    ),
    30: Principle(
        30, "Flexible Shells & Thin Films",
        "Use flexible shells and thin films instead of 3D structures.",
        "Lightweight WebAssembly (Wasm) sandboxes; thin API facades; micro-frontends.",
        "Lightweight landing page funnels testing demand before developing the core product."
    ),
    31: Principle(
        31, "Porous Materials",
        "Make an object porous or introduce porous elements.",
        "Sparse matrices and sparse files; bitmasks (Roaring Bitmaps); sparse indexes.",
        "Open-door policy allowing informal cross-department communication channels."
    ),
    32: Principle(
        32, "Color Changes",
        "Change color or transparency; use color additives.",
        "State tagging; Blue-Green / Canary deployment traffic tagging; color-coded log levels.",
        "Transparent salary bands; public roadmaps demonstrating product trust."
    ),
    33: Principle(
        33, "Homogeneity",
        "Make objects interacting with primary object from identical material.",
        "Monorepos enforcing uniform standards; Protobuf serialization; uniform Linux images.",
        "Standardized corporate OKRs and shared company cultural values across all offices."
    ),
    34: Principle(
        34, "Discarding & Recovering",
        "Discard portions that fulfilled function; restore consumable parts.",
        "Generational Garbage Collection; cycling unhealthy pods; session token refresh.",
        "Sunset obsolete legacy product tiers; rotating quarterly executive assignments."
    ),
    35: Principle(
        35, "Parameter Changes",
        "Change physical state, concentration, density, or temperature.",
        "Transpilation; payload compression (Zstandard); switching JSON to binary format.",
        "Shifting pricing from upfront perpetual license to recurring monthly SaaS subscription."
    ),
    36: Principle(
        36, "Phase Transitions",
        "Utilize phenomena occurring during phase transitions.",
        "JIT compilation (bytecode -> native); object freezing (mutable -> immutable).",
        "Transitioning a viral product from invite-only private beta to public general availability."
    ),
    37: Principle(
        37, "Thermal Expansion",
        "Use expansion or contraction of materials.",
        "Elastic autoscaling expanding under CPU load; dynamic array geometric resizing.",
        "Elastic hiring surges during seasonal retail demand followed by post-holiday normalization."
    ),
    38: Principle(
        38, "Strong Oxidants",
        "Accelerate oxidation; use enriched or active environments.",
        "Aggressive compiler inlining & Dead Code Elimination; Chaos Monkey; -Werror.",
        "High-intensity incubator hackathons forcing rapid 48-hour prototype delivery."
    ),
    39: Principle(
        39, "Inert Atmosphere",
        "Replace normal environment with inert medium to prevent degradation.",
        "Read-only container root filesystems; isolated microVM sandboxes (Firecracker).",
        "Regulatory sandbox environments allowing fintech experimentation without license exposure."
    ),
    40: Principle(
        40, "Composite Materials",
        "Replace uniform material with composite (multi-layered) structure.",
        "Polyglot persistence (SQL + Cache + Search); hybrid Python + Rust FFI extensions.",
        "Hybrid business models combining automated software margins with premium human advisory."
    )
}

# The 39 TRIZ Parameters mapped to Software and Business
PARAMETERS: Dict[int, Parameter] = {
    1: Parameter(1, "Weight of moving object", "Memory footprint of active process", "Variable cost per transaction"),
    2: Parameter(2, "Weight of stationary object", "Storage footprint at rest", "Fixed cost / infrastructure overhead"),
    3: Parameter(3, "Length of moving object", "Request payload size", "Customer journey length"),
    4: Parameter(4, "Length of stationary object", "Codebase size / schema width", "Organizational hierarchy depth"),
    5: Parameter(5, "Area of moving object", "Network bandwidth consumed", "Market reach per campaign"),
    6: Parameter(6, "Area of stationary object", "Disk / storage area allocated", "Office / infrastructure footprint"),
    7: Parameter(7, "Volume of moving object", "Data volume in transit", "Batch size per operation"),
    8: Parameter(8, "Volume of stationary object", "Data volume at rest", "Inventory / backlog size"),
    9: Parameter(9, "Speed", "Throughput / requests per second", "Time-to-market / cycle time"),
    10: Parameter(10, "Force (intensity)", "CPU/GPU compute intensity", "Marketing spend / sales pressure"),
    11: Parameter(11, "Stress or pressure", "System load / queue depth", "Deadline pressure / workload"),
    12: Parameter(12, "Shape", "Data schema / API contract shape", "Org structure / team topology"),
    13: Parameter(13, "Stability of object's composition", "Code stability / backward compat", "Team retention / culture stability"),
    14: Parameter(14, "Strength", "Fault tolerance / resilience", "Brand strength / competitive moat"),
    15: Parameter(15, "Duration of action (moving)", "Request latency / response time", "Service delivery time"),
    16: Parameter(16, "Duration of action (stationary)", "Uptime / availability", "Contract duration / retention"),
    17: Parameter(17, "Temperature", "System thermal load / CPU temp", "Market 'heat' / competitive intensity"),
    18: Parameter(18, "Illumination intensity", "Observability / logging verbosity", "Transparency / reporting detail"),
    19: Parameter(19, "Use of energy by moving object", "CPU cycles per request", "Cost per acquisition (CPA)"),
    20: Parameter(20, "Use of energy by stationary object", "Idle resource consumption", "Overhead cost / maintenance spend"),
    21: Parameter(21, "Power", "Processing power / FLOPS", "Revenue generation capacity"),
    22: Parameter(22, "Loss of energy", "Wasted compute / dropped packets", "Customer churn / revenue leakage"),
    23: Parameter(23, "Loss of substance", "Data loss / information decay", "Talent attrition / knowledge loss"),
    24: Parameter(24, "Loss of information", "Signal degradation / precision loss", "Communication loss / misalignment"),
    25: Parameter(25, "Loss of time", "Latency / wait time / blocking", "Lead time waste / bureaucratic delay"),
    26: Parameter(26, "Quantity of substance", "Number of components / services", "Headcount / inventory quantity"),
    27: Parameter(27, "Reliability", "MTBF / error rate / data integrity", "Service reliability / promise keeping"),
    28: Parameter(28, "Measurement accuracy", "Monitoring precision / granularity", "KPI accuracy / forecast precision"),
    29: Parameter(29, "Manufacturing precision", "Build reproducibility / CI determinism", "Process consistency / quality control"),
    30: Parameter(30, "Object-affected harmful factors", "Attack surface / vulnerability exposure", "Regulatory risk / compliance burden"),
    31: Parameter(31, "Object-generated harmful factors", "Side effects / pollution / tech debt", "Negative externalities / technical debt"),
    32: Parameter(32, "Ease of manufacture", "Development velocity / time to code", "Ease of onboarding / hiring speed"),
    33: Parameter(33, "Ease of operation", "UX simplicity / API ergonomics", "Ease of use / customer effort score"),
    34: Parameter(34, "Ease of repair", "Debuggability / MTTR", "Issue resolution speed / support cost"),
    35: Parameter(35, "Adaptability / versatility", "Extensibility / plugin architecture", "Pivot capability / market flexibility"),
    36: Parameter(36, "Device complexity", "Architectural complexity / LoC", "Org complexity / process complexity"),
    37: Parameter(37, "Difficulty of detecting/measuring", "Debugging difficulty / root cause analysis", "Problem detection / early warning"),
    38: Parameter(38, "Extent of automation", "CI/CD maturity / auto-scaling", "Process automation / self-service"),
    39: Parameter(39, "Productivity", "Output per unit of compute/time", "Revenue per employee / ROI")
}

# Curated Top Contradiction Pairs (improving_param_id, worsening_param_id) -> list of principle IDs
CONTRADICTION_PAIRS: Dict[Tuple[int, int], List[int]] = {
    (9, 1): [2, 28, 13, 38],    # Speed vs Memory
    (9, 27): [10, 35, 28, 21],  # Speed vs Reliability
    (9, 36): [1, 28, 15, 35],   # Speed vs Complexity
    (9, 25): [10, 28, 38, 34],  # Speed vs Latency/Time loss
    (27, 9): [21, 35, 11, 28],  # Reliability vs Speed
    (27, 36): [13, 35, 1, 25],  # Reliability vs Complexity
    (27, 32): [11, 13, 1, 35],  # Reliability vs Dev Velocity
    (39, 36): [1, 28, 15, 35],  # Productivity vs Complexity
    (39, 27): [10, 35, 28, 37],  # Productivity vs Reliability
    (33, 35): [15, 34, 1, 16],  # Ease of use vs Adaptability
    (33, 36): [2, 5, 13, 16],   # Ease of use vs Complexity
    (14, 19): [3, 35, 10, 40],  # Resilience vs Cost/Request
    (14, 36): [13, 35, 1, 25],  # Resilience vs Complexity
    (32, 27): [1, 35, 11, 10],  # Dev Velocity vs Reliability
    (32, 29): [28, 35, 10, 23], # Dev Velocity vs CI Precision
    (35, 13): [15, 35, 1, 28],  # Adaptability vs Stability
    (35, 36): [15, 1, 28, 35],  # Adaptability vs Complexity
    (38, 36): [28, 15, 10, 37], # Automation vs Complexity
    (38, 33): [25, 2, 13, 35],  # Automation vs Ease of use
    (30, 33): [22, 35, 13, 24], # Security vs Ease of use
    (30, 9): [24, 28, 35, 30],  # Security vs Speed
    (34, 36): [1, 13, 25, 28],  # Debuggability vs Complexity
    (34, 9): [10, 28, 35, 37],  # Debuggability vs Speed
    (24, 9): [10, 28, 35, 24],  # Data integrity vs Speed
    (26, 36): [2, 6, 13, 1],    # Components count vs Complexity
    (16, 19): [35, 10, 28, 3],  # Uptime vs Cost
    (22, 9): [35, 28, 2, 10],   # Waste reduction vs Speed
    (31, 32): [10, 35, 13, 2],  # Tech debt vs Dev velocity
    (28, 25): [28, 6, 35, 10],  # Metric accuracy vs Time loss
    (12, 13): [15, 35, 28, 1],  # API contract shape vs Stability
}

def lookup_principles(improving_id: int, worsening_id: int) -> List[Principle]:
    """Look up recommended TRIZ principles for a given contradiction pair."""
    pair = (improving_id, worsening_id)
    if pair in CONTRADICTION_PAIRS:
        return [PRINCIPLES[pid] for pid in CONTRADICTION_PAIRS[pair]]
    # Fallback heuristic: general principles for contradiction resolution
    fallback_ids = [1, 15, 28, 35]
    return [PRINCIPLES[pid] for pid in fallback_ids]

def search_parameters(query: str) -> List[Parameter]:
    """Find parameters matching a text query matching keyword."""
    q = query.lower()
    results = []
    for param in PARAMETERS.values():
        if (q in param.name_en.lower() or 
            q in param.software.lower() or 
            q in param.business.lower()):
            results.append(param)
    return results
