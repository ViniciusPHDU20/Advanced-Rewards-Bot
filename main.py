# main.py - MODO SOBERANO AUTÔNOMO

import time
import json
from playwright.sync_api import sync_playwright
from scripts.browser_manager import create_browser
from scripts.login_manager import login
from scripts.promotions import complete_daily_set, complete_promotions, complete_punch_cards
from scripts.searcher import perform_searches
from scripts.points_logger import log_points, get_current_points
from scripts.notifier import send_discord_notification

def farm_account(p, account):
    # 🖥️ INÍCIO DA SESSÃO
    print(f"🖥️  Iniciando farming para {account['email']}...")
    try:
        context, page = create_browser(p, mobile=False)
        if login(page, account['email'], account['password']):
            # 🏁 Captura saldo inicial
            starting_pts = get_current_points(page)
            print(f"💰 Saldo Inicial: {starting_pts} pts")

            # Executa tarefas Desktop
            complete_daily_set(page)
            complete_punch_cards(page)
            complete_promotions(page)
            perform_searches(page, mobile=False)
            
            # Executa tarefas Mobile (reaproveitando o contexto se possível ou abrindo novo)
            # Para mobile, o ideal é um novo contexto para trocar o User-Agent
            context.close()
            
            print(f"📱 Mudando para modo MOBILE...")
            context, page = create_browser(p, mobile=True)
            if login(page, account['email'], account['password']):
                perform_searches(page, mobile=True)
            
            # 🏁 Captura saldo final e calcula ganhos
            final_pts = get_current_points(page)
            earned = final_pts - starting_pts
            
            print(f"\n💎 PONTOS GANHOS NESTA SESSÃO: {earned}")
            log_points(page, session_earned=earned)
            
            send_discord_notification(account['email'], f"Sessão finalizada! Ganhos: +{earned} pts | Total: {final_pts} pts ✅")
            
        context.close()
    except Exception as e:
        print(f"⚠️  Erro durante a sessão: {e}")

def main():
    try:
        with open("config/accounts.json", "r") as f:
            accounts = json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler accounts.json: {e}")
        return

    with sync_playwright() as p:
        for account in accounts:
            print(f"\n🚀 [AUTÔNOMO] Processando conta: {account['email']}")
            farm_account(p, account)

if __name__ == "__main__":
    print("🤖 JESUS REWARDS BOT - SISTEMA 100% OPERACIONAL")
    main()
    print("\n🏁 MISSÃO FINALIZADA.")
