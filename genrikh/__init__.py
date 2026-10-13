"""
Генрих (Genrikh): Универсальный Изобретательский Партнер на Open-Source AI.
Назван в честь Генриха Сауловича Альтшуллера (1926-1998), создателя ТРИЗ.
"""

from genrikh.core import (
    Constraint, ConstraintType, PhysicalContradiction, ResourceVPR,
    VerificationPlan, ARIZStateLock, DualLoopResult, OutcomeType,
    StrategyType, ConfidenceLevel
)
from genrikh.matrix import PRINCIPLES, PARAMETERS, lookup_principles, search_parameters
from genrikh.engine import OpenSourceAIEngine, OfflineTRIZEngine
from genrikh.consultant import ConsultantSession, ClientProject, ConsultingReport, TEMPLATES
from genrikh.tracing import init_sentry, trace_step, record_state_lock_trace
from genrikh.gemma import format_gemma_chat_prompt
from genrikh.voice import ElevenLabsVoice

__version__ = "1.0.0"

__all__ = [
    "Constraint", "ConstraintType", "PhysicalContradiction", "ResourceVPR",
    "VerificationPlan", "ARIZStateLock", "DualLoopResult", "OutcomeType",
    "StrategyType", "ConfidenceLevel",
    "PRINCIPLES", "PARAMETERS", "lookup_principles", "search_parameters",
    "OpenSourceAIEngine", "OfflineTRIZEngine",
    "ConsultantSession", "ClientProject", "ConsultingReport", "TEMPLATES",
    "init_sentry", "trace_step", "record_state_lock_trace",
    "format_gemma_chat_prompt", "ElevenLabsVoice"
]
