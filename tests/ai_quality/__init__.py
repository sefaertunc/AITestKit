"""
AI quality tests for AITestKit.

AI quality tests:
- Use real Claude API (requires ANTHROPIC_API_KEY)
- Run only pre-release or on-demand
- Test generation quality and consistency
- Are inherently non-deterministic

Test modules to implement:
- test_generation_quality.py: Generated code quality metrics
- test_scot_effectiveness.py: SCoT prompting improvements
- test_llm_judge_accuracy.py: LLM-as-Judge validation

Directories:
- golden_scenarios/: Input scenarios for testing
- golden_outputs/: Expected output samples

See MASTER_SPEC.md Section 13.1 for test categories.
"""
