#!/bin/bash

# set_python_version.sh

# Usage: ./set_python_version.sh 3.11
# This script sets up aliases for the specified Python version.
# Example: ./set_python_version.sh 3.11 will create aliases for python3.11, pip3.11, etc.

# Check if the version is passed as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <python_version>"
    echo "Example: $0 3.11"
    exit 1
fi

PYTHON_VERSION=$1
PYTHON_BIN_PATH="/usr/local/bin"

# Define the alias commands
ALIASES=$(cat <<EOF
# Aliases for Python $PYTHON_VERSION
alias python=$PYTHON_BIN_PATH/python$PYTHON_VERSION
alias python3=$PYTHON_BIN_PATH/python$PYTHON_VERSION
alias pip=$PYTHON_BIN_PATH/pip$PYTHON_VERSION
alias pip3=$PYTHON_BIN_PATH/pip$PYTHON_VERSION
alias ipython=$PYTHON_BIN_PATH/ipython$PYTHON_VERSION
alias jupyter=$PYTHON_BIN_PATH/jupyter$PYTHON_VERSION
EOF
)

# Append aliases to .bashrc
echo "Adding aliases to ~/.bashrc..."
echo "$ALIASES" >> ~/.bashrc

# Append aliases to .zshrc
echo "Adding aliases to ~/.zshrc..."
echo "$ALIASES" >> ~/.zshrc

# Apply changes to the current shell session
if [[ $SHELL == *"zsh"* ]]; then
    echo "Applying changes for zsh..."
    source ~/.zshrc
else
    echo "Applying changes for bash..."
    source ~/.bashrc
fi

echo "Aliases have been set for Python $PYTHON_VERSION."
echo "To verify, run 'python --version' and 'pip --version'."
