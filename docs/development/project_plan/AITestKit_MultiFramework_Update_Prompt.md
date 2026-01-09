# AITestKit Multi-Framework Architecture Update
## Complete Implementation Prompt for Claude Code
### Version 1.0 | January 2025

---

# CONTEXT

I'm building **AITestKit**, an AI-powered test generation CLI tool using Claude API. The project structure is already created with empty placeholder files. I need to update the architecture to support **multi-framework, multi-language test generation** across all testing categories.

## Current State
- GitHub repository initialized
- Basic folder structure exists
- pyproject.toml has minimal configuration
- Virtual environment created but dependencies not installed
- All Python module files are empty placeholders

## Goal
Transform AITestKit from a 3-framework tool (pytest, robot, playwright) into a comprehensive **multi-framework test generation platform** supporting 18+ frameworks across 6 testing categories, while also setting up proper internal testing for the project itself.

---

# PART 1: FRAMEWORK REGISTRY ARCHITECTURE

## Supported Frameworks (18 Total)

### Priority 0 (Core - Implement First)
| Framework | Category | Language | Extension | Description |
|-----------|----------|----------|-----------|-------------|
| pytest | Unit | Python | `.py` | Python unit/integration testing |
| jest | Unit | TypeScript | `.test.ts` | JavaScript/TypeScript unit testing |
| playwright-py | E2E | Python | `.py` | Cross-browser E2E (Python) |
| playwright-ts | E2E | TypeScript | `.spec.ts` | Cross-browser E2E (TypeScript) |
| pytest-bdd | BDD | Python | `.feature` + `.py` | Gherkin BDD (Python) |
| cucumber-java | BDD | Java | `.feature` + `.java` | Gherkin BDD (Java) |
| locust | Performance | Python | `.py` | Python load testing |
| k6 | Performance | JavaScript | `.js` | Modern load testing |
| nuclei | Security | YAML | `.yaml` | Template-based security scanning |
| httpx | API | Python | `.py` | Python API testing |

### Priority 1 (Important - Implement Second)
| Framework | Category | Language | Extension | Description |
|-----------|----------|----------|-----------|-------------|
| junit | Unit | Java | `.java` | Java unit testing (JUnit 5) |
| cypress | E2E | JavaScript | `.cy.js` | JavaScript E2E testing |
| cucumber-js | BDD | JavaScript | `.feature` + `.js` | Gherkin BDD (JavaScript) |
| jmeter | Performance | XML | `.jmx` | Enterprise performance testing |
| postman | API | JSON | `.postman_collection.json` | API collection testing |
| zap | Security | Python | `.py` | OWASP ZAP security testing |

### Priority 2 (Nice-to-Have - Implement Later)
| Framework | Category | Language | Extension | Description |
|-----------|----------|----------|-----------|-------------|
| nunit | Unit | C# | `.cs` | .NET unit testing |
| gatling | Performance | Scala | `.scala` | High-performance load testing |

---

# PART 2: UPDATED FOLDER STRUCTURE

Create/update the following structure:

```
aitestkit/
├── .github/
│   └── workflows/
│       ├── test.yml                    # Run pytest on PR/push
│       └── prompt-regression.yml       # Validate prompt changes
├── src/
│   └── aitestkit/
│       ├── __init__.py                 # Version: "1.0.0"
│       ├── cli.py                      # Click CLI with dynamic framework choices
│       ├── config.py                   # Pydantic configuration
│       ├── exceptions.py               # Custom exceptions
│       │
│       ├── utils/
│       │   ├── __init__.py
│       │   └── claude_client.py        # Claude API wrapper
│       │
│       ├── frameworks/                 # NEW: Framework registry
│       │   ├── __init__.py
│       │   ├── registry.py             # Framework definitions & lookup
│       │   └── base.py                 # Base framework interface
│       │
│       ├── generator/
│       │   ├── __init__.py
│       │   ├── generator.py            # Main generator orchestrator
│       │   ├── context_builder.py      # Prompt assembly
│       │   └── output_parser.py        # Code extraction & validation
│       │
│       ├── analyzer/
│       │   ├── __init__.py
│       │   ├── analyzer.py             # Failure analysis orchestrator
│       │   ├── log_parser.py           # Log parsing utilities
│       │   └── report_generator.py     # Report formatting
│       │
│       ├── regression/
│       │   ├── __init__.py
│       │   ├── scorer.py               # Output scoring logic
│       │   ├── runner.py               # Regression test runner
│       │   └── comparator.py           # Score comparison
│       │
│       └── prompts/
│           ├── templates/
│           │   ├── code-generation/
│           │   │   ├── system.md       # Base system prompt
│           │   │   ├── unit/
│           │   │   │   ├── pytest.md
│           │   │   │   ├── jest.md
│           │   │   │   └── junit.md
│           │   │   ├── e2e/
│           │   │   │   ├── playwright_python.md
│           │   │   │   ├── playwright_typescript.md
│           │   │   │   └── cypress.md
│           │   │   ├── bdd/
│           │   │   │   ├── pytest_bdd.md
│           │   │   │   ├── cucumber_java.md
│           │   │   │   └── cucumber_js.md
│           │   │   ├── performance/
│           │   │   │   ├── locust.md
│           │   │   │   ├── k6.md
│           │   │   │   └── jmeter.md
│           │   │   ├── security/
│           │   │   │   ├── nuclei.md
│           │   │   │   └── zap.md
│           │   │   └── api/
│           │   │       ├── httpx.md
│           │   │       └── postman.md
│           │   └── failure-analysis/
│           │       └── system.md
│           ├── context/
│           │   └── shared/
│           │       ├── testing_principles.md
│           │       └── coding_standards.md
│           ├── benchmarks/
│           │   ├── unit/
│           │   │   └── scenario_pytest_crud.yaml
│           │   ├── e2e/
│           │   │   └── scenario_playwright_login.yaml
│           │   ├── bdd/
│           │   │   └── scenario_cucumber_checkout.yaml
│           │   ├── performance/
│           │   │   └── scenario_locust_load.yaml
│           │   └── security/
│           │       └── scenario_nuclei_scan.yaml
│           └── examples/
│               ├── pytest_example.py
│               ├── playwright_example.py
│               └── locust_example.py
│
├── tests/                              # Internal project tests
│   ├── __init__.py
│   ├── conftest.py                     # Shared fixtures
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_claude_client.py
│   │   ├── test_config.py
│   │   ├── test_framework_registry.py
│   │   ├── generator/
│   │   │   ├── __init__.py
│   │   │   ├── test_context_builder.py
│   │   │   ├── test_output_parser.py
│   │   │   └── test_generator.py
│   │   ├── analyzer/
│   │   │   ├── __init__.py
│   │   │   ├── test_log_parser.py
│   │   │   └── test_analyzer.py
│   │   └── regression/
│   │       ├── __init__.py
│   │       ├── test_scorer.py
│   │       └── test_runner.py
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_cli_generate.py
│   │   ├── test_cli_analyze.py
│   │   └── test_cli_regression.py
│   └── fixtures/
│       ├── sample_logs/
│       │   └── pytest_failure.log
│       ├── mock_responses/
│       │   └── generate_pytest.txt
│       └── expected_outputs/
│           └── test_example.py
│
├── sample_app/                         # Demo application for testing
│   ├── app.py                          # FastAPI Todo API
│   ├── models.py
│   ├── requirements.txt
│   └── README.md
│
├── docs/
│   ├── frameworks.md                   # Framework documentation
│   ├── prompts.md                      # Prompt engineering guide
│   └── contributing.md
│
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
└── SKILL.md                            # Claude Code skill file
```

---

# PART 3: FILE IMPLEMENTATIONS

## 3.1 pyproject.toml (Complete)

```toml
[project]
name = "aitestkit"
version = "1.0.0"
description = "AI-Powered Multi-Framework Test Generation Toolkit"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.11"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = [
    "testing", "ai", "automation", "claude", "qa", 
    "test-generation", "pytest", "playwright", "locust",
    "security-testing", "performance-testing", "bdd"
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Testing",
    "Topic :: Software Development :: Quality Assurance",
]

dependencies = [
    # Core
    "anthropic>=0.40.0",
    "click>=8.1.0",
    "pyyaml>=6.0",
    "rich>=13.0.0",
    "pydantic>=2.0.0",
    "python-dotenv>=1.0.0",
    
    # Template rendering
    "jinja2>=3.1.0",
]

[project.optional-dependencies]
dev = [
    # Testing
    "pytest>=8.0.0",
    "pytest-cov>=4.0.0",
    "pytest-mock>=3.12.0",
    "pytest-asyncio>=0.23.0",
    "hypothesis>=6.0.0",
    
    # Code quality
    "ruff>=0.1.0",
    "black>=24.0.0",
    "mypy>=1.0.0",
    "pre-commit>=3.6.0",
    
    # Type stubs
    "types-PyYAML>=6.0.0",
    "types-click>=7.1.0",
]

# Framework validators (optional)
validators = [
    "robotframework>=7.0",
    "gherkin-official>=29.0.0",
]

# Sample app dependencies
sample-app = [
    "fastapi>=0.109.0",
    "uvicorn>=0.27.0",
    "httpx>=0.26.0",
]

# All optional dependencies
all = [
    "aitestkit[dev]",
    "aitestkit[validators]",
    "aitestkit[sample-app]",
]

[project.scripts]
aitestkit = "aitestkit.cli:main"

[project.urls]
Homepage = "https://github.com/yourusername/aitestkit"
Documentation = "https://github.com/yourusername/aitestkit#readme"
Repository = "https://github.com/yourusername/aitestkit"
Issues = "https://github.com/yourusername/aitestkit/issues"

[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
aitestkit = ["prompts/**/*.md", "prompts/**/*.yaml"]

# Ruff configuration
[tool.ruff]
line-length = 100
target-version = "py311"
src = ["src", "tests"]

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # Pyflakes
    "I",      # isort
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "UP",     # pyupgrade
    "ARG",    # flake8-unused-arguments
    "SIM",    # flake8-simplify
]
ignore = [
    "E501",   # line too long (handled by formatter)
    "B008",   # do not perform function calls in argument defaults
]

[tool.ruff.lint.isort]
known-first-party = ["aitestkit"]

# Black configuration
[tool.black]
line-length = 100
target-version = ["py311"]
include = '\.pyi?$'
exclude = '''
/(
    \.git
    | \.venv
    | build
    | dist
)/
'''

# MyPy configuration
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_ignores = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_configs = true
show_error_codes = true
show_column_numbers = true

[[tool.mypy.overrides]]
module = ["anthropic.*", "rich.*"]
ignore_missing_imports = true

# Pytest configuration
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
python_classes = ["Test*"]
addopts = [
    "-v",
    "--tb=short",
    "--strict-markers",
    "-ra",
]
markers = [
    "unit: Unit tests",
    "integration: Integration tests",
    "slow: Slow running tests",
]
filterwarnings = [
    "ignore::DeprecationWarning",
]

# Coverage configuration
[tool.coverage.run]
source = ["src/aitestkit"]
branch = true
omit = [
    "*/tests/*",
    "*/__init__.py",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if TYPE_CHECKING:",
    "if __name__ == .__main__.:",
]
fail_under = 80
show_missing = true
```

## 3.2 Framework Registry (src/aitestkit/frameworks/registry.py)

```python
"""
Framework registry for multi-framework test generation support.

This module defines all supported testing frameworks with their metadata,
enabling dynamic framework selection and validation in the CLI and generator.

Supported Categories:
- Unit Testing: pytest, jest, junit, nunit
- E2E Testing: playwright (py/ts), cypress, selenium
- BDD Testing: pytest-bdd, cucumber (java/js)
- Performance Testing: locust, k6, jmeter, gatling
- Security Testing: nuclei, owasp-zap
- API Testing: httpx, postman

Example Usage:
    from aitestkit.frameworks.registry import get_framework, list_frameworks
    
    # Get specific framework
    fw = get_framework("pytest")
    print(fw.extension)  # ".py"
    
    # List all performance frameworks
    perf_frameworks = list_frameworks(category=FrameworkCategory.PERFORMANCE)
"""

from dataclasses import dataclass
from enum import Enum
from typing import Literal


class FrameworkCategory(str, Enum):
    """Testing framework categories."""
    UNIT = "unit"
    API = "api"
    E2E = "e2e"
    BDD = "bdd"
    PERFORMANCE = "performance"
    SECURITY = "security"
    MOBILE = "mobile"


@dataclass(frozen=True)
class FrameworkInfo:
    """
    Framework metadata for test generation.
    
    Attributes:
        name: Display name of the framework
        category: Testing category (unit, e2e, performance, etc.)
        language: Primary programming language
        extension: Output file extension
        prompt_template: Path to prompt template (relative to prompts/templates/code-generation/)
        description: Human-readable description
        priority: Implementation priority (0=core, 1=important, 2=nice-to-have)
        multi_file: Whether framework generates multiple files (e.g., BDD feature + steps)
        secondary_extension: Extension for secondary file (if multi_file=True)
    """
    name: str
    category: FrameworkCategory
    language: str
    extension: str
    prompt_template: str
    description: str
    priority: int = 0
    multi_file: bool = False
    secondary_extension: str | None = None


# =============================================================================
# FRAMEWORK DEFINITIONS
# =============================================================================

FRAMEWORKS: dict[str, FrameworkInfo] = {
    # -------------------------------------------------------------------------
    # UNIT TESTING
    # -------------------------------------------------------------------------
    "pytest": FrameworkInfo(
        name="pytest",
        category=FrameworkCategory.UNIT,
        language="Python",
        extension=".py",
        prompt_template="unit/pytest.md",
        description="Python unit and integration testing framework",
        priority=0,
    ),
    "jest": FrameworkInfo(
        name="Jest",
        category=FrameworkCategory.UNIT,
        language="TypeScript",
        extension=".test.ts",
        prompt_template="unit/jest.md",
        description="JavaScript/TypeScript testing framework",
        priority=0,
    ),
    "junit": FrameworkInfo(
        name="JUnit 5",
        category=FrameworkCategory.UNIT,
        language="Java",
        extension=".java",
        prompt_template="unit/junit.md",
        description="Java unit testing framework",
        priority=1,
    ),
    "nunit": FrameworkInfo(
        name="NUnit",
        category=FrameworkCategory.UNIT,
        language="C#",
        extension=".cs",
        prompt_template="unit/nunit.md",
        description=".NET unit testing framework",
        priority=2,
    ),
    
    # -------------------------------------------------------------------------
    # E2E / WEB TESTING
    # -------------------------------------------------------------------------
    "playwright-py": FrameworkInfo(
        name="Playwright",
        category=FrameworkCategory.E2E,
        language="Python",
        extension=".py",
        prompt_template="e2e/playwright_python.md",
        description="Cross-browser E2E testing (Python)",
        priority=0,
    ),
    "playwright-ts": FrameworkInfo(
        name="Playwright",
        category=FrameworkCategory.E2E,
        language="TypeScript",
        extension=".spec.ts",
        prompt_template="e2e/playwright_typescript.md",
        description="Cross-browser E2E testing (TypeScript)",
        priority=0,
    ),
    "cypress": FrameworkInfo(
        name="Cypress",
        category=FrameworkCategory.E2E,
        language="JavaScript",
        extension=".cy.js",
        prompt_template="e2e/cypress.md",
        description="JavaScript E2E testing framework",
        priority=1,
    ),
    "selenium-py": FrameworkInfo(
        name="Selenium",
        category=FrameworkCategory.E2E,
        language="Python",
        extension=".py",
        prompt_template="e2e/selenium_python.md",
        description="Browser automation (Python)",
        priority=2,
    ),
    
    # -------------------------------------------------------------------------
    # BDD / ACCEPTANCE TESTING
    # -------------------------------------------------------------------------
    "pytest-bdd": FrameworkInfo(
        name="pytest-bdd",
        category=FrameworkCategory.BDD,
        language="Python",
        extension=".feature",
        prompt_template="bdd/pytest_bdd.md",
        description="BDD with Gherkin syntax (Python)",
        priority=0,
        multi_file=True,
        secondary_extension="_steps.py",
    ),
    "cucumber-java": FrameworkInfo(
        name="Cucumber",
        category=FrameworkCategory.BDD,
        language="Java",
        extension=".feature",
        prompt_template="bdd/cucumber_java.md",
        description="BDD with Gherkin syntax (Java)",
        priority=0,
        multi_file=True,
        secondary_extension="Steps.java",
    ),
    "cucumber-js": FrameworkInfo(
        name="Cucumber",
        category=FrameworkCategory.BDD,
        language="JavaScript",
        extension=".feature",
        prompt_template="bdd/cucumber_js.md",
        description="BDD with Gherkin syntax (JavaScript)",
        priority=1,
        multi_file=True,
        secondary_extension=".steps.js",
    ),
    "behave": FrameworkInfo(
        name="Behave",
        category=FrameworkCategory.BDD,
        language="Python",
        extension=".feature",
        prompt_template="bdd/behave.md",
        description="BDD framework for Python",
        priority=2,
        multi_file=True,
        secondary_extension="_steps.py",
    ),
    
    # -------------------------------------------------------------------------
    # PERFORMANCE TESTING
    # -------------------------------------------------------------------------
    "locust": FrameworkInfo(
        name="Locust",
        category=FrameworkCategory.PERFORMANCE,
        language="Python",
        extension=".py",
        prompt_template="performance/locust.md",
        description="Python load testing framework",
        priority=0,
    ),
    "k6": FrameworkInfo(
        name="k6",
        category=FrameworkCategory.PERFORMANCE,
        language="JavaScript",
        extension=".js",
        prompt_template="performance/k6.md",
        description="Modern load testing tool",
        priority=0,
    ),
    "jmeter": FrameworkInfo(
        name="JMeter",
        category=FrameworkCategory.PERFORMANCE,
        language="XML",
        extension=".jmx",
        prompt_template="performance/jmeter.md",
        description="Enterprise performance testing tool",
        priority=1,
    ),
    "gatling": FrameworkInfo(
        name="Gatling",
        category=FrameworkCategory.PERFORMANCE,
        language="Scala",
        extension=".scala",
        prompt_template="performance/gatling.md",
        description="High-performance load testing",
        priority=2,
    ),
    "artillery": FrameworkInfo(
        name="Artillery",
        category=FrameworkCategory.PERFORMANCE,
        language="YAML",
        extension=".yml",
        prompt_template="performance/artillery.md",
        description="Cloud-scale load testing",
        priority=2,
    ),
    
    # -------------------------------------------------------------------------
    # SECURITY TESTING
    # -------------------------------------------------------------------------
    "nuclei": FrameworkInfo(
        name="Nuclei",
        category=FrameworkCategory.SECURITY,
        language="YAML",
        extension=".yaml",
        prompt_template="security/nuclei.md",
        description="Template-based vulnerability scanner",
        priority=0,
    ),
    "zap": FrameworkInfo(
        name="OWASP ZAP",
        category=FrameworkCategory.SECURITY,
        language="Python",
        extension=".py",
        prompt_template="security/zap.md",
        description="Web application security scanner",
        priority=1,
    ),
    "bandit": FrameworkInfo(
        name="Bandit",
        category=FrameworkCategory.SECURITY,
        language="Python",
        extension=".py",
        prompt_template="security/bandit.md",
        description="Python security linter",
        priority=2,
    ),
    
    # -------------------------------------------------------------------------
    # API TESTING
    # -------------------------------------------------------------------------
    "httpx": FrameworkInfo(
        name="pytest + httpx",
        category=FrameworkCategory.API,
        language="Python",
        extension=".py",
        prompt_template="api/httpx.md",
        description="Python API testing with httpx",
        priority=0,
    ),
    "postman": FrameworkInfo(
        name="Postman/Newman",
        category=FrameworkCategory.API,
        language="JSON",
        extension=".postman_collection.json",
        prompt_template="api/postman.md",
        description="API collection testing",
        priority=1,
    ),
    "rest-assured": FrameworkInfo(
        name="REST Assured",
        category=FrameworkCategory.API,
        language="Java",
        extension=".java",
        prompt_template="api/rest_assured.md",
        description="Java REST API testing",
        priority=2,
    ),
    "supertest": FrameworkInfo(
        name="Supertest",
        category=FrameworkCategory.API,
        language="JavaScript",
        extension=".test.js",
        prompt_template="api/supertest.md",
        description="Node.js API testing",
        priority=2,
    ),
}


# =============================================================================
# REGISTRY FUNCTIONS
# =============================================================================

def get_framework(name: str) -> FrameworkInfo:
    """
    Get framework information by name.
    
    Args:
        name: Framework identifier (e.g., "pytest", "playwright-py")
    
    Returns:
        FrameworkInfo dataclass with framework metadata
    
    Raises:
        ValueError: If framework name is not found
    
    Example:
        >>> fw = get_framework("pytest")
        >>> fw.language
        'Python'
    """
    if name not in FRAMEWORKS:
        available = ", ".join(sorted(FRAMEWORKS.keys()))
        raise ValueError(
            f"Unknown framework: '{name}'. "
            f"Available frameworks: {available}"
        )
    return FRAMEWORKS[name]


def list_frameworks(
    category: FrameworkCategory | None = None,
    language: str | None = None,
    priority: int | None = None,
) -> list[FrameworkInfo]:
    """
    List frameworks with optional filtering.
    
    Args:
        category: Filter by testing category
        language: Filter by programming language
        priority: Filter by implementation priority (0, 1, or 2)
    
    Returns:
        List of matching FrameworkInfo objects, sorted by priority then name
    
    Example:
        >>> perf = list_frameworks(category=FrameworkCategory.PERFORMANCE)
        >>> [fw.name for fw in perf]
        ['Locust', 'k6', 'JMeter', 'Gatling', 'Artillery']
    """
    frameworks = list(FRAMEWORKS.values())
    
    if category is not None:
        frameworks = [f for f in frameworks if f.category == category]
    
    if language is not None:
        frameworks = [f for f in frameworks if f.language.lower() == language.lower()]
    
    if priority is not None:
        frameworks = [f for f in frameworks if f.priority == priority]
    
    return sorted(frameworks, key=lambda f: (f.priority, f.name))


def get_framework_choices() -> list[str]:
    """
    Get list of all framework identifiers for CLI choices.
    
    Returns:
        Sorted list of framework names
    
    Example:
        >>> choices = get_framework_choices()
        >>> "pytest" in choices
        True
    """
    return sorted(FRAMEWORKS.keys())


def get_frameworks_by_category() -> dict[FrameworkCategory, list[FrameworkInfo]]:
    """
    Get all frameworks organized by category.
    
    Returns:
        Dictionary mapping categories to framework lists
    
    Example:
        >>> by_cat = get_frameworks_by_category()
        >>> len(by_cat[FrameworkCategory.UNIT])
        4
    """
    result: dict[FrameworkCategory, list[FrameworkInfo]] = {
        cat: [] for cat in FrameworkCategory
    }
    
    for framework in FRAMEWORKS.values():
        result[framework.category].append(framework)
    
    # Sort each category by priority then name
    for cat in result:
        result[cat] = sorted(result[cat], key=lambda f: (f.priority, f.name))
    
    return result


def get_core_frameworks() -> list[FrameworkInfo]:
    """
    Get priority 0 (core) frameworks that should be implemented first.
    
    Returns:
        List of core frameworks sorted by name
    """
    return list_frameworks(priority=0)


def validate_framework(name: str) -> bool:
    """
    Check if a framework name is valid.
    
    Args:
        name: Framework identifier to validate
    
    Returns:
        True if valid, False otherwise
    """
    return name in FRAMEWORKS


# =============================================================================
# CLI HELPER
# =============================================================================

def format_framework_table() -> str:
    """
    Format all frameworks as a table for CLI display.
    
    Returns:
        Formatted string table of all frameworks
    """
    lines = [
        "Supported Frameworks:",
        "-" * 80,
        f"{'Framework':<15} {'Category':<12} {'Language':<12} {'Extension':<20} {'Priority'}",
        "-" * 80,
    ]
    
    for name, fw in sorted(FRAMEWORKS.items(), key=lambda x: (x[1].priority, x[0])):
        priority_label = {0: "Core", 1: "Standard", 2: "Extended"}.get(fw.priority, "?")
        lines.append(
            f"{name:<15} {fw.category.value:<12} {fw.language:<12} {fw.extension:<20} {priority_label}"
        )
    
    lines.append("-" * 80)
    lines.append(f"Total: {len(FRAMEWORKS)} frameworks")
    
    return "\n".join(lines)
```

## 3.3 Test Fixtures (tests/conftest.py)

```python
"""
Shared test fixtures for AITestKit internal testing.

This module provides reusable fixtures for mocking the Claude API,
creating test configurations, and setting up the CLI test runner.

Usage:
    # In any test file
    def test_something(mock_client, cli_runner):
        result = cli_runner.invoke(main, ["generate", "test scenario"])
        assert result.exit_code == 0
"""

import pytest
from pathlib import Path
from typing import Generator
from unittest.mock import MagicMock, patch
from click.testing import CliRunner

from aitestkit.config import Config
from aitestkit.utils.claude_client import ClaudeClient


# =============================================================================
# MOCK RESPONSES
# =============================================================================

MOCK_PYTEST_RESPONSE = '''```python
"""Test user authentication."""

import pytest


class TestUserLogin:
    """Tests for user login functionality."""

    def test_user_can_login_with_valid_credentials(self) -> None:
        """Test successful login with valid username and password."""
        # Arrange
        username = "testuser"
        password = "validpassword123"
        
        # Act
        result = login(username, password)
        
        # Assert
        assert result.success is True, "Login should succeed with valid credentials"
        assert result.user.username == username
```

# Suggested filename: test_user_login.py
'''

MOCK_LOCUST_RESPONSE = '''```python
"""Load test for API endpoints."""

from locust import HttpUser, task, between


class APILoadTest(HttpUser):
    """Load test user for API testing."""
    
    wait_time = between(1, 3)
    
    @task(3)
    def get_todos(self) -> None:
        """Test GET /todos endpoint."""
        self.client.get("/todos")
    
    @task(1)
    def create_todo(self) -> None:
        """Test POST /todos endpoint."""
        self.client.post("/todos", json={"title": "Test Todo"})
```

# Suggested filename: locustfile.py
'''

MOCK_ANALYSIS_RESPONSE = '''
## Root Cause Analysis

**Root Cause:** Database connection timeout due to connection pool exhaustion

**Confidence:** High (85%)

**Category:** Environment Issue

## Evidence
- Connection timeout error in stack trace
- Multiple concurrent requests detected
- Pool size set to default (5)

## Suggested Actions
1. Increase connection pool size to 20
2. Add connection retry logic
3. Implement circuit breaker pattern

## Investigation Steps
1. Check database server logs
2. Monitor connection pool metrics
3. Review concurrent request patterns
'''


# =============================================================================
# FIXTURES: MOCKING
# =============================================================================

@pytest.fixture
def mock_claude_response() -> str:
    """Standard mock response from Claude API for pytest generation."""
    return MOCK_PYTEST_RESPONSE


@pytest.fixture
def mock_locust_response() -> str:
    """Mock response for Locust performance test generation."""
    return MOCK_LOCUST_RESPONSE


@pytest.fixture
def mock_analysis_response() -> str:
    """Mock response for failure analysis."""
    return MOCK_ANALYSIS_RESPONSE


@pytest.fixture
def mock_anthropic(mock_claude_response: str) -> Generator[MagicMock, None, None]:
    """
    Mock the Anthropic client to prevent real API calls.
    
    Yields:
        Mocked Anthropic class
    """
    with patch("aitestkit.utils.claude_client.Anthropic") as mock_cls:
        mock_instance = MagicMock()
        mock_instance.messages.create.return_value = MagicMock(
            content=[MagicMock(text=mock_claude_response)],
            usage=MagicMock(input_tokens=150, output_tokens=300),
        )
        mock_cls.return_value = mock_instance
        yield mock_cls


@pytest.fixture
def mock_client(mock_anthropic: MagicMock) -> ClaudeClient:
    """
    Create a ClaudeClient with mocked API.
    
    Returns:
        ClaudeClient instance that won't make real API calls
    """
    with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "test-key-12345"}):
        return ClaudeClient()


# =============================================================================
# FIXTURES: CONFIGURATION
# =============================================================================

@pytest.fixture
def test_config(tmp_path: Path) -> Config:
    """
    Create a test configuration with temporary paths.
    
    Args:
        tmp_path: Pytest temporary directory fixture
    
    Returns:
        Config instance for testing
    """
    prompts_dir = tmp_path / "prompts"
    output_dir = tmp_path / "output"
    
    prompts_dir.mkdir(parents=True)
    output_dir.mkdir(parents=True)
    
    return Config(
        anthropic_api_key="test-key-12345",
        prompts_dir=prompts_dir,
        output_dir=output_dir,
        default_framework="pytest",
        regression_threshold=85,
        regression_tolerance=5,
    )


@pytest.fixture
def sample_prompts_dir(tmp_path: Path) -> Path:
    """
    Create a sample prompts directory structure with minimal content.
    
    Returns:
        Path to the prompts directory
    """
    prompts = tmp_path / "prompts"
    
    # Create directory structure
    dirs = [
        "templates/code-generation/unit",
        "templates/code-generation/e2e",
        "templates/code-generation/bdd",
        "templates/code-generation/performance",
        "templates/code-generation/security",
        "templates/code-generation/api",
        "templates/failure-analysis",
        "context/shared",
        "benchmarks/unit",
        "examples",
    ]
    
    for d in dirs:
        (prompts / d).mkdir(parents=True, exist_ok=True)
    
    # Create minimal prompt files
    (prompts / "templates/code-generation/system.md").write_text(
        "You are a senior QA engineer. Generate test code based on the scenario."
    )
    (prompts / "templates/code-generation/unit/pytest.md").write_text(
        "Use pytest framework. Include type hints and docstrings."
    )
    (prompts / "templates/failure-analysis/system.md").write_text(
        "Analyze the test failure and provide root cause analysis."
    )
    (prompts / "context/shared/testing_principles.md").write_text(
        "Follow AAA pattern: Arrange, Act, Assert."
    )
    
    return prompts


# =============================================================================
# FIXTURES: CLI
# =============================================================================

@pytest.fixture
def cli_runner() -> CliRunner:
    """
    Create a Click CLI test runner.
    
    Returns:
        CliRunner instance for testing CLI commands
    """
    return CliRunner(mix_stderr=False)


# =============================================================================
# FIXTURES: SAMPLE DATA
# =============================================================================

@pytest.fixture
def sample_log_content() -> str:
    """Sample pytest failure log for analyzer tests."""
    return """
============================= FAILED =============================
tests/test_api.py::TestTodoAPI::test_create_todo - AssertionError

    def test_create_todo(self):
        response = client.post("/todos", json={"title": "Test"})
>       assert response.status_code == 201
E       AssertionError: assert 500 == 201
E        +  where 500 = <Response [500]>.status_code

tests/test_api.py:25: AssertionError
---------------------------- Captured log ----------------------------
ERROR    app:app.py:45 Database connection failed: timeout
========================= short test summary =========================
FAILED tests/test_api.py::TestTodoAPI::test_create_todo - AssertionError
========================= 1 failed in 0.52s ==========================
"""


@pytest.fixture
def sample_benchmark_yaml(tmp_path: Path) -> Path:
    """Create a sample benchmark scenario file."""
    benchmark = tmp_path / "benchmark.yaml"
    benchmark.write_text("""
scenario_id: "test_001"
name: "CRUD Create Test"
description: "Test creating a new item"
framework: pytest

input:
  scenario: |
    Test that a user can create a new todo item.
    Send POST to /todos with title.
    Verify 201 response.

expected_elements:
  must_contain:
    - "def test_"
    - "assert"
    - "POST"
    - "201"
  must_not_contain:
    - "time.sleep"
    - "TODO"
  structure:
    has_docstring: true
    has_assertions: true
    min_assertions: 2

quality_checks:
  - name: "No hardcoded waits"
    pattern: "time\\\\.sleep|sleep\\\\("
    should_match: false

baseline_score: 85
""")
    return benchmark


# =============================================================================
# FIXTURES: ENVIRONMENT
# =============================================================================

@pytest.fixture(autouse=True)
def clean_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Ensure clean environment for each test.
    
    Removes any existing API key to prevent accidental real API calls.
    """
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)


@pytest.fixture
def with_api_key(monkeypatch: pytest.MonkeyPatch) -> str:
    """
    Set a test API key in the environment.
    
    Returns:
        The test API key
    """
    key = "test-api-key-for-testing"
    monkeypatch.setenv("ANTHROPIC_API_KEY", key)
    return key
```

## 3.4 CLI with Dynamic Framework Choices (src/aitestkit/cli.py)

```python
"""
AITestKit Command Line Interface.

A multi-framework test generation toolkit powered by Claude AI.

Usage:
    aitestkit generate "Test user login" -f pytest
    aitestkit generate "Load test API" -f locust
    aitestkit analyze ./failed.log -o report.md
    aitestkit regression --all
    aitestkit frameworks --list
    aitestkit info

Commands:
    generate    Generate test code from natural language scenario
    analyze     Analyze test failure and suggest fixes
    regression  Run prompt regression tests
    frameworks  List and manage supported frameworks
    info        Show configuration and status
"""

import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from aitestkit import __version__
from aitestkit.config import config
from aitestkit.frameworks.registry import (
    get_framework,
    get_framework_choices,
    get_frameworks_by_category,
    FrameworkCategory,
    format_framework_table,
)

console = Console()


# =============================================================================
# MAIN GROUP
# =============================================================================

@click.group()
@click.version_option(version=__version__, prog_name="aitestkit")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.pass_context
def main(ctx: click.Context, verbose: bool) -> None:
    """
    AITestKit - AI-Powered Multi-Framework Test Generation Toolkit
    
    Generate tests for 18+ frameworks including pytest, Playwright, Locust,
    Cucumber, k6, Nuclei, and more using Claude AI.
    """
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


# =============================================================================
# GENERATE COMMAND
# =============================================================================

@main.command()
@click.argument("scenario", type=str)
@click.option(
    "--framework", "-f",
    type=click.Choice(get_framework_choices(), case_sensitive=False),
    default="pytest",
    help="Target testing framework",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default="./output",
    help="Output directory for generated tests",
)
@click.option(
    "--context", "-c",
    type=click.Path(exists=True),
    default=None,
    help="Additional context file (API docs, specs, etc.)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be generated without calling API",
)
@click.pass_context
def generate(
    ctx: click.Context,
    scenario: str,
    framework: str,
    output: str,
    context: str | None,
    dry_run: bool,
) -> None:
    """
    Generate test code from a natural language scenario.
    
    SCENARIO: Description of what to test (in quotes)
    
    Examples:
    
        aitestkit generate "Test user can create todo" -f pytest
        
        aitestkit generate "Load test with 100 users" -f locust
        
        aitestkit generate "Check for SQL injection" -f nuclei
    """
    fw_info = get_framework(framework)
    
    console.print(Panel(
        f"[bold]Generating {fw_info.name} test[/bold]\n\n"
        f"Framework: {fw_info.name} ({fw_info.language})\n"
        f"Category: {fw_info.category.value}\n"
        f"Output: {output}/",
        title="[cyan]AITestKit Generate[/cyan]",
    ))
    
    if dry_run:
        console.print("[yellow]Dry run - no API call made[/yellow]")
        return
    
    if not config.validate_api_key():
        console.print("[red]Error: ANTHROPIC_API_KEY not set[/red]")
        console.print("Set it with: export ANTHROPIC_API_KEY=your-key")
        raise SystemExit(1)
    
    # Import here to avoid loading until needed
    from aitestkit.generator import TestGenerator
    
    generator = TestGenerator()
    
    with console.status("[bold green]Generating test code..."):
        result = generator.generate(
            scenario=scenario,
            framework=framework,
            context_file=Path(context) if context else None,
        )
    
    # Save output
    output_path = Path(output)
    output_path.mkdir(parents=True, exist_ok=True)
    
    output_file = output_path / result.suggested_filename
    output_file.write_text(result.code)
    
    # Display results
    console.print(f"\n[green]✓[/green] Generated: {output_file}")
    console.print(f"  Tokens: {result.tokens_used:,}")
    console.print(f"  Cost: ${result.cost:.4f}")
    
    if result.validation_issues:
        console.print("\n[yellow]Validation warnings:[/yellow]")
        for issue in result.validation_issues:
            console.print(f"  • {issue}")
    
    if ctx.obj.get("verbose"):
        console.print("\n[dim]Generated code:[/dim]")
        console.print(result.code)


# =============================================================================
# ANALYZE COMMAND
# =============================================================================

@main.command()
@click.argument("log_file", type=click.Path(exists=True))
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output file for analysis report",
)
@click.option(
    "--format", "-f",
    type=click.Choice(["markdown", "json", "console"]),
    default="console",
    help="Output format",
)
@click.pass_context
def analyze(
    ctx: click.Context,
    log_file: str,
    output: str | None,
    format: str,
) -> None:
    """
    Analyze test failure and suggest fixes.
    
    LOG_FILE: Path to test failure log or output
    
    Examples:
    
        aitestkit analyze ./pytest_output.log
        
        aitestkit analyze ./failed.log -f markdown -o report.md
    """
    if not config.validate_api_key():
        console.print("[red]Error: ANTHROPIC_API_KEY not set[/red]")
        raise SystemExit(1)
    
    log_content = Path(log_file).read_text()
    
    from aitestkit.analyzer import FailureAnalyzer
    
    analyzer = FailureAnalyzer()
    
    with console.status("[bold green]Analyzing failure..."):
        result = analyzer.analyze(log_content)
    
    if format == "console":
        console.print(result.to_rich_panel())
    elif format == "markdown":
        md_content = result.to_markdown()
        if output:
            Path(output).write_text(md_content)
            console.print(f"[green]✓[/green] Report saved: {output}")
        else:
            console.print(md_content)
    elif format == "json":
        import json
        json_content = json.dumps(result.to_dict(), indent=2)
        if output:
            Path(output).write_text(json_content)
            console.print(f"[green]✓[/green] Report saved: {output}")
        else:
            console.print(json_content)


# =============================================================================
# REGRESSION COMMAND
# =============================================================================

@main.command()
@click.option(
    "--prompt", "-p",
    type=click.Path(exists=True),
    default=None,
    help="Specific prompt file to test",
)
@click.option(
    "--all", "-a", "run_all",
    is_flag=True,
    default=False,
    help="Run all benchmark scenarios",
)
@click.option(
    "--category", "-c",
    type=click.Choice([c.value for c in FrameworkCategory]),
    default=None,
    help="Run benchmarks for specific category",
)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    help="Show detailed scoring breakdown",
)
@click.pass_context
def regression(
    ctx: click.Context,
    prompt: str | None,
    run_all: bool,
    category: str | None,
    verbose: bool,
) -> None:
    """
    Run prompt regression tests to validate prompt quality.
    
    Examples:
    
        aitestkit regression --all
        
        aitestkit regression --category unit -v
        
        aitestkit regression -p ./prompts/templates/pytest.md
    """
    if not run_all and not prompt and not category:
        console.print("[yellow]Specify --all, --category, or --prompt[/yellow]")
        raise SystemExit(1)
    
    if not config.validate_api_key():
        console.print("[red]Error: ANTHROPIC_API_KEY not set[/red]")
        raise SystemExit(1)
    
    from aitestkit.regression import RegressionRunner
    
    runner = RegressionRunner()
    
    with console.status("[bold green]Running regression tests..."):
        if run_all:
            result = runner.run_all()
        elif category:
            result = runner.run_category(FrameworkCategory(category))
        else:
            result = runner.run_prompt(Path(prompt))
    
    runner.display_results(result, verbose=verbose)
    
    if not result.passed:
        raise SystemExit(1)


# =============================================================================
# FRAMEWORKS COMMAND
# =============================================================================

@main.command()
@click.option(
    "--list", "-l", "list_all",
    is_flag=True,
    help="List all supported frameworks",
)
@click.option(
    "--category", "-c",
    type=click.Choice([c.value for c in FrameworkCategory]),
    default=None,
    help="Filter by category",
)
@click.option(
    "--language", "-lang",
    type=str,
    default=None,
    help="Filter by language (Python, Java, etc.)",
)
def frameworks(
    list_all: bool,
    category: str | None,
    language: str | None,
) -> None:
    """
    List and explore supported testing frameworks.
    
    Examples:
    
        aitestkit frameworks --list
        
        aitestkit frameworks --category performance
        
        aitestkit frameworks --language Python
    """
    if not list_all and not category and not language:
        console.print(format_framework_table())
        return
    
    # Build filter
    frameworks_dict = get_frameworks_by_category()
    
    table = Table(title="Supported Frameworks")
    table.add_column("Framework", style="cyan")
    table.add_column("Category", style="green")
    table.add_column("Language")
    table.add_column("Extension")
    table.add_column("Description")
    
    for cat, fw_list in frameworks_dict.items():
        if category and cat.value != category:
            continue
        
        for fw in fw_list:
            if language and fw.language.lower() != language.lower():
                continue
            
            table.add_row(
                fw.name,
                cat.value,
                fw.language,
                fw.extension,
                fw.description,
            )
    
    console.print(table)


# =============================================================================
# INFO COMMAND
# =============================================================================

@main.command()
def info() -> None:
    """Show configuration and status."""
    api_status = "[green]✓ Configured[/green]" if config.validate_api_key() else "[red]✗ Missing[/red]"
    
    from aitestkit.frameworks.registry import FRAMEWORKS
    
    panel_content = f"""
[bold]Version:[/bold] {__version__}
[bold]API Key:[/bold] {api_status}

[bold]Paths:[/bold]
  Prompts: {config.prompts_dir}
  Output:  {config.output_dir}

[bold]Defaults:[/bold]
  Framework: {config.default_framework}
  Threshold: {config.regression_threshold}
  Tolerance: {config.regression_tolerance}

[bold]Frameworks:[/bold] {len(FRAMEWORKS)} supported
  Core (P0):     {len([f for f in FRAMEWORKS.values() if f.priority == 0])}
  Standard (P1): {len([f for f in FRAMEWORKS.values() if f.priority == 1])}
  Extended (P2): {len([f for f in FRAMEWORKS.values() if f.priority == 2])}
"""
    
    console.print(Panel(
        panel_content.strip(),
        title="[bold cyan]AITestKit Configuration[/bold cyan]",
    ))


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()
```

---

# PART 4: GITHUB ACTIONS WORKFLOWS

## 4.1 Test Workflow (.github/workflows/test.yml)

```yaml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e ".[dev]"
      
      - name: Run linting
        run: |
          ruff check src/ tests/
          black --check src/ tests/
      
      - name: Run type checking
        run: mypy src/
      
      - name: Run tests
        run: |
          pytest tests/ -v --cov=aitestkit --cov-report=xml --cov-report=term-missing
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage.xml
          fail_ci_if_error: false

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install dependencies
        run: |
          pip install ruff black
      
      - name: Run ruff
        run: ruff check src/ tests/
      
      - name: Run black
        run: black --check src/ tests/
```

## 4.2 Prompt Regression Workflow (.github/workflows/prompt-regression.yml)

```yaml
name: Prompt Regression

on:
  pull_request:
    paths:
      - 'src/aitestkit/prompts/**'

jobs:
  regression:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install dependencies
        run: |
          pip install -e ".[dev]"
      
      - name: Run prompt regression
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          aitestkit regression --all --verbose
      
      - name: Comment PR with results
        if: always()
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            
            let comment = '## Prompt Regression Results\n\n';
            comment += 'Regression tests completed. Check the workflow logs for details.';
            
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

---

# PART 5: INSTRUCTIONS FOR CLAUDE CODE

## Execution Order

1. **Update pyproject.toml** with the complete configuration above
2. **Create/update folder structure** - ensure all directories exist
3. **Implement frameworks/registry.py** - the framework registry
4. **Implement tests/conftest.py** - shared test fixtures
5. **Update cli.py** - with dynamic framework choices
6. **Create GitHub workflows** - test.yml and prompt-regression.yml
7. **Run pip install -e ".[dev]"** to install with dev dependencies
8. **Run pytest tests/ -v** to verify test setup works

## Commands to Run After Implementation

```bash
# Install dependencies
pip install -e ".[dev]"

# Verify installation
aitestkit --version
aitestkit info
aitestkit frameworks --list

# Run internal tests
pytest tests/ -v

# Check code quality
ruff check src/ tests/
black --check src/ tests/
mypy src/
```

## Key Files to Create/Update

| File | Priority | Description |
|------|----------|-------------|
| `pyproject.toml` | P0 | Complete project configuration |
| `src/aitestkit/frameworks/registry.py` | P0 | Framework definitions |
| `src/aitestkit/cli.py` | P0 | CLI with framework support |
| `tests/conftest.py` | P0 | Test fixtures |
| `.github/workflows/test.yml` | P1 | CI testing |
| `.github/workflows/prompt-regression.yml` | P1 | Prompt validation |

## Validation Checklist

- [ ] `aitestkit --version` shows version
- [ ] `aitestkit frameworks --list` shows 18+ frameworks
- [ ] `aitestkit info` shows configuration
- [ ] `pytest tests/ -v` passes (with mocked API)
- [ ] `ruff check src/` passes
- [ ] `mypy src/` passes

---

# SUMMARY

This prompt transforms AITestKit from a basic 3-framework tool into a comprehensive multi-framework test generation platform supporting:

- **6 Categories**: Unit, E2E, BDD, Performance, Security, API
- **18+ Frameworks**: pytest, Jest, JUnit, Playwright, Cypress, Cucumber, Locust, k6, JMeter, Nuclei, and more
- **Multiple Languages**: Python, JavaScript/TypeScript, Java, YAML, Scala, C#
- **Internal Testing**: Complete pytest setup with fixtures for testing AITestKit itself

The architecture is extensible - new frameworks can be added by:
1. Adding entry to `FRAMEWORKS` dict in registry.py
2. Creating prompt template in appropriate category folder
3. Adding benchmark scenario for regression testing
