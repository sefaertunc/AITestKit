# Development Tests (dev_tests/)

Quick validation tests for development. **Not part of the official test suite.**

## Purpose

- **Quick Validation**: Test newly implemented features without full test suite
- **Manual Testing**: Test with real API keys and external services (when implemented)
- **Experimental**: Try out approaches before committing
- **Cost Estimation**: Validate Claude API usage and costs (Phase 3+)

## Current Structure (Phase 2: Docker + CLI)

- `unit/` - Unit tests for individual modules
  - `test_config.py` - Tests for configuration module ✅
  - (Future: test_errors.py, test_scenario_loader.py, test_scenario_validator.py)
- `integration/` - End-to-end workflow tests (empty for now, will add when CLI is ready)
- `manual/` - Manual test scripts (empty for now, will add when claude_client.py exists)
- `helpers/` - Test utilities and fixtures

## Running Tests

```bash
# Run all dev tests
pytest dev_tests/ -v

# Run specific test file
pytest dev_tests/unit/test_config.py -v

# Or run as standalone script
python dev_tests/unit/test_config.py
```

## vs tests/ Directory

| Feature | tests/ | dev_tests/ |
|---------|--------|------------|
| Purpose | Official test suite | Development validation |
| CI/CD | ✅ Runs in CI | ❌ Manual only |
| API Key | ❌ Mocked | ✅ Real (optional) |
| Coverage | Full coverage | Key features only |
| Speed | Fast (mocked) | Slower (real API) |

## Adding New Tests

When implementing a new module:
1. Create unit test in `unit/test_<module>.py`
2. Add integration test in `integration/` if needed
3. Run tests: `pytest dev_tests/unit/test_<module>.py`
4. Once stable, add to official `tests/` suite

## Development Workflow

**Current Phase (Phase 2: Docker + CLI):**
- ✅ `config.py` → `unit/test_config.py` (implemented)
- ⏳ `errors.py` → Will add `unit/test_errors.py` after implementation
- ⏳ `scenario/loader.py` → Will add `unit/test_scenario_loader.py` after implementation
- ⏳ `scenario/validator.py` → Will add `unit/test_scenario_validator.py` after implementation
- ⏳ `scenario/migrator.py` → Will add `unit/test_scenario_migrator.py` after implementation
- ⏳ `claude_client.py` → Will add `unit/test_claude_client.py` after implementation
- ⏳ `cli.py` → Will add `integration/test_cli_commands.py` after implementation

Tests are added **parallel to development**, not ahead of time.

## Module Test Priority (Phase 2)

| Module | Test File | Priority | Notes |
|--------|-----------|----------|-------|
| `errors.py` | `test_errors.py` | P0 | Error hierarchy, exit codes |
| `scenario/loader.py` | `test_scenario_loader.py` | P0 | YAML parsing, Pydantic models |
| `scenario/validator.py` | `test_scenario_validator.py` | P0 | Validation tiers |
| `scenario/migrator.py` | `test_scenario_migrator.py` | P1 | Schema migration |
| `cli.py` | `test_cli_commands.py` | P0 | Click commands |
| `feedback/storage.py` | `test_feedback_storage.py` | P1 | JSON storage |
