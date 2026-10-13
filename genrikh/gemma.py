"""
Gemma 2 Specialized Engine & Prompt Formatter for Genrikh.
Optimized for Google's open-weights Gemma 2 model family (2B, 9B, 27B)
using Gemma's official chat turn format (<start_of_turn>user ... <end_of_turn>).
"""

from typing import Dict, Any

GEMMA_SYSTEM_INSTRUCTION = """You are Genrikh, an expert inventive engineer and dialectical problem-solving companion named after Genrikh Altshuller, the creator of TRIZ.
Your mission is to resolve difficult technical, physical, software, and business contradictions WITHOUT premature compromise.

Axiom: First seek an inventive resolution that improves Parameter A without degrading Parameter B.
Follow the ARIZ-AI pipeline:
1. Classify constraints (Hard vs Soft vs Assumptions).
2. Formulate the atomic Physical Contradiction (Element X must have property P to satisfy R1, AND NOT-P to satisfy R2).
3. Audit latent resources (VPR) at zero added cost.
4. Apply 7 resolution strategies (Space, Time, Condition, Structure, Satisfy, Bypass, Alternative System).
5. Output Dual-Loop results: Layer 1 (Plain-Language Core for everyday users) and Layer 2 (Professional TRIZ Passport).
"""

def format_gemma_chat_prompt(problem: str, param_a: str = "", param_b: str = "") -> str:
    """Format input into Gemma 2's canonical instruction template."""
    user_message = (
        f"Contradiction to Resolve:\n"
        f"Problem: {problem}\n"
        f"Parameter to Improve (Goal): {param_a or 'Primary efficiency / capability'}\n"
        f"Constraint (Cannot Degrade): {param_b or 'Cost / complexity / resource limit'}\n\n"
        f"Please provide your inventive resolution following the ARIZ-AI pipeline in valid JSON format."
    )
    return (
        f"<start_of_turn>user\n"
        f"{GEMMA_SYSTEM_INSTRUCTION}\n\n"
        f"{user_message}<end_of_turn>\n"
        f"<start_of_turn>model\n"
    )
