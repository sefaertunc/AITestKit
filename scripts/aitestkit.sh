#!/bin/bash
# AITestKit Docker wrapper for Linux/macOS
#
# Usage: ./aitestkit.sh [command] [args...]
# Example: ./aitestkit.sh generate -s scenarios/login.yaml -f pytest
#
# Environment:
#   ANTHROPIC_API_KEY - Required for Claude API access
#
# Volume mounts:
#   $(pwd) -> /workspace (user's project)
#   ~/.aitestkit -> /home/aitestkit/.aitestkit (persistent config)

docker run --rm \
    -v "$(pwd)":/workspace \
    -v "${HOME}/.aitestkit":/home/aitestkit/.aitestkit \
    -e ANTHROPIC_API_KEY \
    ghcr.io/sefaertunc/aitestkit:latest "$@"
