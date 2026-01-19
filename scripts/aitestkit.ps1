# AITestKit Docker wrapper for Windows PowerShell
#
# Usage: ./aitestkit.ps1 [command] [args...]
# Example: ./aitestkit.ps1 generate -s scenarios/login.yaml -f pytest
#
# Environment:
#   ANTHROPIC_API_KEY - Required for Claude API access
#
# Volume mounts:
#   $PWD -> /workspace (user's project)
#   $env:USERPROFILE\.aitestkit -> /home/aitestkit/.aitestkit (persistent config)

docker run --rm `
    -v "${PWD}:/workspace" `
    -v "${env:USERPROFILE}\.aitestkit:/home/aitestkit/.aitestkit" `
    -e ANTHROPIC_API_KEY `
    ghcr.io/sefaertunc/aitestkit:latest @args
