"""
Unit tests for Genrikh.
"""

import pytest
from genrikh.matrix import PRINCIPLES, PARAMETERS, lookup_principles, search_parameters
from genrikh.core import (
    Constraint, ConstraintType, PhysicalContradiction, ResourceVPR,
    VerificationPlan, ARIZStateLock, OutcomeType, StrategyType, ConfidenceLevel
)
from genrikh.engine import OfflineTRIZEngine, OpenSourceAIEngine
from genrikh.consultant import ConsultantSession, TEMPLATES, ClientProject
from genrikh.gemma import format_gemma_chat_prompt
from genrikh.tracing import trace_step, record_state_lock_trace
from genrikh.voice import ElevenLabsVoice

def test_principles_catalog():
    assert len(PRINCIPLES) == 40
    p1 = PRINCIPLES[1]
    assert p1.name_en == "Segmentation"
    assert p1.name_ru == "Дробление"
    assert "Microservices" in p1.software

def test_parameters_catalog():
    assert len(PARAMETERS) == 39
    p9 = PARAMETERS[9]
    assert p9.name_en == "Speed"
    assert "Throughput" in p9.software

def test_matrix_lookup():
    # 9 Speed vs 1 Memory
    principles = lookup_principles(9, 1)
    ids = [p.id for p in principles]
    assert 2 in ids # Taking out
    assert 28 in ids # Mechanics substitution

def test_matrix_search():
    results = search_parameters("latency")
    assert len(results) > 0
    ids = [r.id for r in results]
    assert 15 in ids or 25 in ids

def test_offline_genrikh_engine():
    engine = OfflineTRIZEngine()
    result = engine.solve(
        problem="High database read concurrency locks write transactions",
        param_a="Read Throughput",
        param_b="Database Memory & CPU Cost"
    )
    assert result.state_lock.outcome_type == OutcomeType.ELIMINATE
    assert "### 💡 Решение от Генриха" in result.layer_1
    assert "### 💡 ТРИЗ-Паспорт Решения" in result.layer_2
    assert len(result.state_lock.mobilized_vpr) > 0
    assert result.confidence == ConfidenceLevel.PATTERN

def test_consultant_session():
    consultant = ConsultantSession()
    report = consultant.run_template("freelancer_offline_sync")
    assert report.project.client_name == "LocalCraft Freelance Services"
    md = report.to_markdown()
    assert "# 🏛️ TRIZ Inventive Audit & Architectural Roadmap" in md
    assert "Executive Summary" in md
    assert "Latent Resource Ledger (VPR" in md

def test_gemma_prompt_formatting():
    prompt = format_gemma_chat_prompt("High latency vs memory", "Speed", "Memory")
    assert "<start_of_turn>user" in prompt
    assert "<end_of_turn>" in prompt
    assert "<start_of_turn>model" in prompt
    assert "Genrikh" in prompt

def test_sentry_tracing_step():
    with trace_step("genrikh.test_step", "Testing Sentry Span") as span:
        assert True

def test_voice_fallback():
    voice = ElevenLabsVoice()
    # Without API key, generate_audio safely returns None
    if not voice.is_available():
        res = voice.generate_audio("Test audio")
        assert res is None
