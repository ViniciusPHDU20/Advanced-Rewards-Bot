import json
from datetime import datetime

def generate_report(session, earned_points):
    report_data = {
        "email": session.email,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "start_time": session.session_start_time.strftime("%H:%M:%S"),
        "end_time": datetime.now().strftime("%H:%M:%S"),
        "points_balance": {
            "initial": session.start_points,
            "final": session.end_points,
            "earned": earned_points
        },
        "activities": session.activities_log
    }

    # Gera Log no terminal
    print("\n" + "="*40)
    print("📊 RELATÓRIO DE SESSÃO CORPORATIVO")
    print("="*40)
    print(f"📧 Conta: {session.email}")
    print(f"💰 Saldo Inicial: {session.start_points}")
    print(f"💎 Saldo Final: {session.end_points}")
    print(f"✅ GANHOS TOTAIS: +{earned_points} pts")
    print("-" * 20)
    print("🛠️ ATIVIDADES REALIZADAS:")
    for act in session.activities_log:
        print(f" - [{act['timestamp']}] {act['activity']}: {act['status']}")
    print("="*40 + "\n")

    # Salva relatório em JSON para histórico
    try:
        filename = "session_history.json"
        try:
            with open(filename, "r") as f:
                history = json.load(f)
        except:
            history = []
        
        history.append(report_data)
        with open(filename, "w") as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        print(f"⚠️ Falha ao salvar histórico de sessão: {e}")

    return report_data
