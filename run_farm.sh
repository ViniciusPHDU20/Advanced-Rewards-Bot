#!/bin/bash
# JESUS REWARDS BOT - LAUNCHER
# MODO SOBERANO ATIVADO

BASE_DIR="$HOME/WORKSPACE_CORE/rewards_farm"
cd "$BASE_DIR"

if [ ! -d "venv" ]; then
    echo "⚙️ Criando ambiente virtual..."
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    playwright install chromium
else
    source venv/bin/activate
fi

echo "🚀 INICIANDO FARMING (DESKTOP + MOBILE)..."
python main.py
echo "🏁 SESSÃO CONCLUÍDA."
