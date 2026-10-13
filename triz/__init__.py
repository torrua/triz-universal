"""
TRIZ Universal: Universal Inventive Problem Solver & Architectural Consultant.
Built with Classical TRIZ (ARIZ-AI) and Open-Source AI.
"""

from triz.core import (
    Constraint, ConstraintType, PhysicalContradiction, ResourceVPR,
    VerificationPlan, ARIZStateLock, DualLoopResult, OutcomeType,
    StrategyType, ConfidenceLevel
)
from triz.matrix import PRINCIPLES, PARAMETERS, lookup_principles, search_parameters
from triz.engine import OpenSourceAIEngine, OfflineTRIZEngine
from triz.consultant import ConsultantSession, ClientProject, ConsultingReport, TEMPLATES

__version__ = "1.0.0"

__all__ = [
    "Constraint", "ConstraintType", "PhysicalContradiction", "ResourceVPR",
    "VerificationPlan", "ARIZStateLock", "DualLoopResult", "OutcomeType",
    "StrategyType", "ConfidenceLevel",
    "PRINCIPLES", "PARAMETERS", "lookup_principles", "search_parameters",
    "OpenSourceAIEngine", "OfflineTRIZEngine",
    "ConsultantSession", "ClientProject", "ConsultingReport", "TEMPLATES"
]
