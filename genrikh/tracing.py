"""
Sentry Agent Tracing Integration for Genrikh.
Implements fine-grained observability across the ARIZ-AI pipeline steps,
recording state locks, VPR resource audits, and Dual-Loop execution.
"""

import os
from contextlib import contextmanager
from typing import Optional, Dict, Any

try:
    import sentry_sdk
    SENTRY_AVAILABLE = True
except ImportError:
    SENTRY_AVAILABLE = False

_INITIALIZED = False

def init_sentry(dsn: Optional[str] = None):
    """Initialize Sentry Agent Tracing if DSN is configured."""
    global _INITIALIZED
    dsn = dsn or os.getenv("SENTRY_DSN")
    if dsn and SENTRY_AVAILABLE and not _INITIALIZED:
        sentry_sdk.init(
            dsn=dsn,
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
            environment=os.getenv("ENVIRONMENT", "production"),
            release="genrikh@1.0.0"
        )
        _INITIALIZED = True
        return True
    return False

@contextmanager
def trace_step(op: str, description: str, data: Optional[Dict[str, Any]] = None):
    """
    Context manager to trace an ARIZ reasoning step.
    Emits Sentry spans if Sentry is active, otherwise operates as a no-op.
    """
    if SENTRY_AVAILABLE and _INITIALIZED:
        with sentry_sdk.start_span(op=op, description=description) as span:
            if data:
                for k, v in data.items():
                    span.set_data(k, v)
            yield span
    else:
        yield None

def record_state_lock_trace(state_lock):
    """
    Record the Loop 1 State Lock in Sentry transaction context.
    Provides verifiable proof that the state lock occurred before Layer 1 / Layer 2 output.
    """
    if SENTRY_AVAILABLE and _INITIALIZED:
        sentry_sdk.set_tag("genrikh.outcome_type", state_lock.outcome_type.value)
        sentry_sdk.set_tag("genrikh.strategy", state_lock.selected_strategy.value)
        sentry_sdk.set_context("genrikh_state_lock", {
            "physical_contradiction": state_lock.physical_contradiction.to_statement(),
            "constraints_count": len(state_lock.constraints),
            "vpr_resources": [r.name for r in state_lock.mobilized_vpr],
            "principles": state_lock.selected_principles,
            "verification_experiment": state_lock.verification_plan.experiment
        })
