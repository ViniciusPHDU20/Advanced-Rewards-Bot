#!/bin/bash

# REWARDS AUTOMATION ENGINE - LAUNCHER
# Optimized for Arch Linux environments

echo "🚀 Initializing Rewards Automation Engine..."

# Navigate to script directory
cd "$(dirname "$0")"

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Please run installation steps."
    exit 1
fi

# Run the main engine
python main.py

# Deactivate venv
deactivate

echo "🏁 Automation session finished."
