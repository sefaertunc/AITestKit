#!/bin/bash
# AITestKit Installation Script
#
# Installs the AITestKit Docker wrapper script to ~/.local/bin
# and pulls the latest Docker image.
#
# Usage: curl -fsSL https://raw.githubusercontent.com/sefaertunc/aitestkit/main/scripts/install.sh | bash

set -e

INSTALL_DIR="${HOME}/.local/bin"
SCRIPT_URL="https://raw.githubusercontent.com/sefaertunc/aitestkit/main/scripts/aitestkit.sh"
IMAGE="ghcr.io/sefaertunc/aitestkit:latest"

echo "Installing AITestKit..."

# Create install directory
mkdir -p "$INSTALL_DIR"

# Download wrapper script
echo "Downloading wrapper script..."
curl -fsSL "$SCRIPT_URL" -o "$INSTALL_DIR/aitestkit"
chmod +x "$INSTALL_DIR/aitestkit"

# Pull Docker image
echo "Pulling Docker image..."
docker pull "$IMAGE"

# Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo ""
    echo "Add ~/.local/bin to your PATH:"
    echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo ""
    echo "Add this line to your ~/.bashrc or ~/.zshrc"
fi

echo ""
echo "AITestKit installed successfully!"
echo "Run: aitestkit --help"
