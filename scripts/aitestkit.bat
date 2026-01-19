@echo off
REM AITestKit Docker wrapper for Windows CMD
REM
REM Usage: aitestkit.bat [command] [args...]
REM Example: aitestkit.bat generate -s scenarios/login.yaml -f pytest
REM
REM Environment:
REM   ANTHROPIC_API_KEY - Required for Claude API access
REM
REM Volume mounts:
REM   %cd% -> /workspace (user's project)
REM   %USERPROFILE%\.aitestkit -> /home/aitestkit/.aitestkit (persistent config)

docker run --rm ^
    -v "%cd%":/workspace ^
    -v "%USERPROFILE%\.aitestkit":/home/aitestkit/.aitestkit ^
    -e ANTHROPIC_API_KEY ^
    ghcr.io/sefaertunc/aitestkit:latest %*
