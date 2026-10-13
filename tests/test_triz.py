"""
Unit tests for TRIZ Universal.
"""

import pytest
from triz.matrix import PRINCIPLES, PARAMETERS, lookup_principles, search_parameters
from triz.core import (
    Constraint, ConstraintType, PhysicalContradiction, ResourceVPR,
    VerificationPlan, ARIZStateLock, OutcomeType, StrategyType, ConfidenceLevel
)
from triz.engine import OfflineTRIZEngine, OpenSourceAIEngine
from triz.consultant import ConsultantSession, TEMPLATES, ClientProject

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

def test_offline_triz_engine():
    engine = OfflineTRIZEngine()
    result = engine.solve(
        problem="High database read concurrency locks write transactions",
        param_a="Read Throughput",
        param_b="Database Memory & CPU Cost"
    )
    assert result.state_lock.outcome_type == OutcomeType.ELIMINATE
    assert "### 💡 Inventive Resolution" in result.layer_1
    assert "### 💡 TRIZ Inventive Resolution Passport" in result.layer_2
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
