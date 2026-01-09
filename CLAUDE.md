# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AITestKit is an AI-powered test development toolkit that uses Claude API to:
- **Generate test code** from natural language descriptions (Claude Opus 4.5)
- **Analyze test failures** and suggest fixes (Claude Sonnet 4.5)
- **Validate prompt quality** through regression testing (Claude Haiku 4.5)

Core principle: AI generates, human reviews and approves. AI does not self-learn; humans improve prompts based on output.

## Commands

```bash
# Install (development)
pip install -e ".[dev]"

# Run tests
pytest tests/ -v
pytest tests/test_generator.py -v  # single test file

# Lint
ruff check src/ tests/

# Type check
mypy src/

# Format
black src/ tests/

# CLI commands (requires ANTHROPIC_API_KEY env var)
aitestkit generate "Test user can login" -f pytest
aitestkit generate --framework robot --output ./output/ "Test scenario"
aitestkit analyze ./logs/failed_test.log
aitestkit analyze ./log.txt -o report.md -f markdown
aitestkit regression --all
aitestkit regression --prompt ./prompts/system.md
aitestkit info  # Show configuration
```

## Architecture

```
src/aitestkit/
├── cli.py                 # Click-based CLI entry point
├── config.py              # Pydantic configuration (env vars, paths)
├── utils/
│   └── claude_client.py   # Anthropic API wrapper (model selection, usage tracking)
├── generator/             # Test code generation
│   ├── generator.py       # Main TestGenerator class
│   ├── context_builder.py # Builds prompts from templates + context
│   └── output_parser.py   # Extracts code from AI response
├── analyzer/              # Failure analysis
│   ├── analyzer.py        # Main FailureAnalyzer class
│   ├── log_parser.py      # Extracts errors/traces from logs
│   └── report_generator.py
├── regression/            # Prompt regression testing
│   ├── runner.py          # Orchestrates regression tests
│   ├── scorer.py          # Scores generated code against benchmarks (structural/40, content/40, quality/20)
│   └── comparator.py      # Compares old vs new prompt outputs
└── prompts/               # Prompt library
    ├── templates/         # System prompts per feature
    │   ├── code-generation/  # system.md, pytest.md, robot_framework.md, playwright.md
    │   └── failure_analysis/ # system.md
    ├── context/           # Shared context files
    │   ├── shared/        # coding_standarts.md, testing_principles.md
    │   └── sample_app/    # api_reference.md
    ├── examples/          # Few-shot examples for prompts
    └── benchmarks/        # Regression test scenarios (YAML)

sample_app/                # Demo FastAPI Todo app for testing
tests/fixtures/            # Sample logs and scenarios for testing
```

## Data Flow

- **Test Generation**: User scenario → ContextBuilder (loads prompts) → Claude Opus → OutputParser → Test file
- **Failure Analysis**: Log file → LogParser → Claude Sonnet → ReportGenerator → Markdown report
- **Prompt Regression**: Benchmark YAML → Generate with old/new prompts → Score both → Compare → Pass/Fail

## Model Configuration

| Task | Model | Model ID | Method |
|------|-------|----------|--------|
| Code generation | Opus 4.5 | claude-opus-4-5-20250514 | `ClaudeClient.generate_code()` |
| Failure analysis | Sonnet 4.5 | claude-sonnet-4-5-20250514 | `ClaudeClient.analyze()` |
| Regression tests | Haiku 4.5 | claude-haiku-4-5-20250514 | `ClaudeClient.quick_check()` |

## Benchmark Scenario Format

Regression test scenarios are defined in YAML (`src/aitestkit/prompts/benchmarks/`):

```yaml
scenario_id: "crud_001"
name: "CRUD Operations - Create Item"
framework: pytest
input:
  scenario: |
    Test that a user can create a new todo item...
expected_elements:
  must_contain: ["def test_", "assert", "POST", "/todos"]
  must_not_contain: ["time.sleep", "TODO"]
  structure:
    has_docstring: true
    has_assertions: true
    min_assertions: 2
quality_checks:
  - name: "No hardcoded waits"
    pattern: "time\\.sleep"
    should_match: false
baseline_score: 85
```

## Key Conventions

- Python 3.11+ required
- Line length: 100 characters (ruff, black)
- Type hints required (mypy strict mode)
- Test frameworks supported: pytest, Robot Framework, Playwright
- Prompts stored as Markdown files in `src/aitestkit/prompts/`
- Generated code should NOT contain: `time.sleep`, `TODO`, `pass  #` placeholders
- Regression threshold: 85 (minimum passing score), tolerance: 5 (max allowed score drop)

## Environment Variables

- `ANTHROPIC_API_KEY` - Required for Claude API access
- `AITESTKIT_PROMPTS_DIR` - Override prompts directory (default: src/aitestkit/prompts)
- `AITESTKIT_OUTPUT_DIR` - Override output directory (default: ./output)
- `AITESTKIT_DEFAULT_FRAMEWORK` - Default test framework (pytest/robot/playwright)
- `AITESTKIT_REGRESSION_THRESHOLD` - Minimum passing score (default: 85)
- `AITESTKIT_REGRESSION_TOLERANCE` - Max allowed score drop (default: 5)

## Error Handling

```python
from anthropic import APIError, RateLimitError, AuthenticationError

# Handle API errors appropriately:
# - AuthenticationError: Invalid API key
# - RateLimitError: Wait and retry
# - APIError: General API issues
```
