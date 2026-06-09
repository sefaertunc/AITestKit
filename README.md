# Cognova

> ⚠️ **Work in Progress** — Cognova is under active development. Features and the
> architecture shown below are evolving and may change without notice. It is not
> ready for use yet.

AI-powered test generation toolkit — an MCP server for IDE integration.

## What It Is

Cognova connects to your IDE through the Model Context Protocol (MCP) and uses
Claude to turn plain YAML scenario descriptions into real, validated test code.

Core principle: **AI generates, deterministic rules validate, humans approve.**

## What It Does

- Generates test code from YAML scenario descriptions using Claude AI
- Supports 25+ testing frameworks (pytest, Jest, JUnit, Playwright, Robot, etc.)
- Validates generated code through deterministic rules + rubric-based LLM-as-Judge
- Learns from feedback to improve output over time
- Repairs broken tests and self-heals after code changes

## Architecture

The end-to-end pipeline — from scenario definition through validation, generation,
linting, and the LLM-as-Judge review loop:

![Cognova architecture and pipeline](docs/assets/architecture.png)

## License

MIT
