""" Unit tests for utility functions module. """

import pytest
from aitestkit.utils import ClaudeClient, UsageStats

def estimated_cost_real(input_tokens: int, output_tokens: int) -> float:
    """Helper function to calculate estimated cost for comparison in tests."""
    avg_input_price = (5.00 + 3.00 + 1.00) / 3
    avg_output_price = (25.00 + 15.00 + 5.00) / 3
    input_cost = (input_tokens / 1_000_000) * avg_input_price
    output_cost = (output_tokens / 1_000_000) * avg_output_price
    return input_cost + output_cost

def test_estimated_cost_rational():
    """Test estimated cost calculation in UsageStats."""
    usage = UsageStats(input_tokens=3_000_000, output_tokens=2_000_000)
    assert usage.estimated_cost == estimated_cost_real(3_000_000, 2_000_000)
    
def test_estimated_approx():
    usage = UsageStats(input_tokens=2_348_464, output_tokens=5_763_275)
    assert usage.estimated_cost == pytest.approx(estimated_cost_real(2_348_464, 5_763_275), rel=1e-3)
def test_estimated_zero():
    usage = UsageStats(input_tokens=0, output_tokens=0)
    assert usage.estimated_cost == 0.0
    
def test_estimated_large():
    usage = UsageStats(input_tokens=10_000_000, output_tokens=20_000_000)
    assert usage.estimated_cost == estimated_cost_real(10_000_000, 20_000_000)
    
def test_estimated_negative():
    with pytest.raises(ValueError):
        UsageStats(input_tokens=-1_000_000, output_tokens=500_000)
        
def test_usage_stats_addition():
    usage1 = UsageStats(input_tokens=1_000_000, output_tokens=2_000_000, api_calls=5)
    usage2 = UsageStats(input_tokens=3_000_000, output_tokens=4_000_000, api_calls=10)
    combined = usage1 + usage2
    assert combined.input_tokens == 4_000_000
    assert combined.output_tokens == 6_000_000
    assert combined.api_calls == 15
    
def test_usage_stats_addition_zero():
    usage1 = UsageStats(input_tokens=0, output_tokens=0, api_calls=0)
    usage2 = UsageStats(input_tokens=0, output_tokens=0, api_calls=0)
    combined = usage1 + usage2
    assert combined.input_tokens == 0
    assert combined.output_tokens == 0
    assert combined.api_calls == 0

def test_claude_client_initialization():
    client = ClaudeClient()
    assert isinstance(client, ClaudeClient)

def test_claude_client_anthropic_key():
    client = ClaudeClient()
    assert client._settings.anthropic_api_key is not None
    
def test_claude_client_api_key_check_env(monkeypatch):
    from aitestkit.config import get_settings
    get_settings.cache_clear()
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key-123")
    client = ClaudeClient()
    assert client._settings.anthropic_api_key == "test-key-123"
    get_settings.cache_clear()