"""
Core ARIZ-AI Pipeline & Dual-Loop Execution.
Implements the 2-loop architecture and 5-step ARIZ pipeline from SKILL.md.
"""

from enum import Enum
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
from dataclasses import dataclass

class ConstraintType(str, Enum):
    HARD = "hard"              # Physical, mathematical, regulatory, safety, contractual
    SOFT = "soft"              # Preferences, optimization goals (can be traded off with permission)
    ASSUMPTION = "assumption"  # Unverified assumptions, needs evidence

class OutcomeType(str, Enum):
    ELIMINATE = "Contradiction Eliminated"
    PROVEN_LIMIT = "Proven Irreducible Limit"
    MANAGED_TRADEOFF = "Authorized Managed Trade-off"

class StrategyType(str, Enum):
    SPACE = "Separation in Space"
    TIME = "Separation in Time"
    CONDITION = "Separation by Condition"
    STRUCTURE = "Separation by Structure"
    SATISFY = "Satisfy (Coexistence)"
    BYPASS = "Bypass (Reformulation)"
    ALTERNATIVE_SYSTEM = "Alternative System"
    PROVEN_LIMIT = "Proven Limit (Boundary Engineering)"
    MANAGED_TRADEOFF = "Managed Trade-off (Authorized)"

class ConfidenceLevel(str, Enum):
    FACT = "Fact (Primary doc / Formal proof / Benchmark)"
    PATTERN = "Pattern (Known engineering/business architecture)"
    HYPOTHESIS = "Hypothesis (Untested, requires validation experiment)"

class Constraint(BaseModel):
    name: str
    ctype: ConstraintType
    description: str

class PhysicalContradiction(BaseModel):
    element: str
    property_p: str
    not_property_p: str
    requirement_for_p: str
    requirement_for_not_p: str

    def to_statement(self) -> str:
        return (
            f"Element '{self.element}' must have property [{self.property_p}] to satisfy [{self.requirement_for_p}], "
            f"AND must have property [{self.not_property_p}] to satisfy [{self.requirement_for_not_p}]."
        )

class ResourceVPR(BaseModel):
    name: str
    domain: str  # software, business, hardware, cognitive
    availability: str
    cost: str = "Zero added cost (internal resource)"

class VerificationPlan(BaseModel):
    baseline: str
    experiment: str
    success_threshold: str
    verifier_role: str = "QA / Benchmark Suite"

class ARIZStateLock(BaseModel):
    """
    Loop 1: Internal State Lock (Anti-Post-Hoc Guarantee).
    Before emitting Layer 1 or Layer 2, all 6 state variables are locked.
    """
    constraints: List[Constraint]
    outcome_type: OutcomeType
    physical_contradiction: PhysicalContradiction
    mobilized_vpr: List[ResourceVPR]
    selected_strategy: StrategyType
    selected_principles: List[int]
    verification_plan: VerificationPlan

class DualLoopResult(BaseModel):
    """
    Loop 2: Contextual Output Delivery.
    - layer_1: Plain-Language Core (Zero Jargon, solution-first for clients)
    - layer_2: Professional TRIZ Passport (Deep methodological breakdown)
    """
    state_lock: ARIZStateLock
    layer_1: str
    layer_2: str
    confidence: ConfidenceLevel
    residual_risks: List[str]

    def render_layer_1(self) -> str:
        return self.layer_1

    def render_layer_2(self) -> str:
        return self.layer_2
