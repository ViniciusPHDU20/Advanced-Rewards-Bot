#!/bin/bash

# REWARDS AUTOMATION ENGINE - LAUNCHER PRO v1.3
# Full CLI Argument Support

BASE_DIR="/home/viniciusphdu/WORKSPACE_CORE/Advanced-Rewards-Bot"
cd "$BASE_DIR"

PYTHON_VENV="$BASE_DIR/venv/bin/python"

if [ ! -f "$PYTHON_VENV" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    exit 1
fi

echo "🎯 Iniciando Advanced Rewards Bot..."
export PYTHONPATH="$BASE_DIR"

# Passar todos os argumentos do bash para o Python
"$PYTHON_VENV" -m src.main "$@"

echo "🏁 Operação finalizada."
