# main.py - REWARDS AUTOMATION ENGINE v3.0 (PRO CONSOLE)

import time
import json
import os
import sys
from playwright.sync_api import sync_playwright

# Core Imports
from scripts.browser_manager import create_browser
from scripts.login_manager import login
from scripts.models.session import RewardSession
from scripts.actions.daily_set import solve_daily_set
from scripts.actions.searches import execute_searches, execute_ghost_searches
from scripts.core.reporter import generate_report
from scripts.notifier import send_discord_notification

def start_browser_session(p, account, mobile=False):
    """Auxiliar para abrir o navegador e iniciar a sessão de pontos."""
    context, page = create_browser(p, mobile=mobile)
    session = RewardSession(page, account['email'])
    if login(page, account['email'], account['password']):
        session.start_session()
        return context, page, session
    return context, page, None

def run_menu():
    print("="*50)
    print("      🚀 REWARDS AUTOMATION ENGINE - PRO v3.0")
    print("="*50)
    print("1) 📊 Consultar Saldo & Status Atual")
    print("2) 🖥️ Iniciar Farming Desktop (Ghost Engine)")
    print("3) 📱 Iniciar Farming Mobile (Playwright Engine)")
    print("4) 🛠️ Executar Daily Set (Quizzes/Atividades)")
    print("5) 🚀 Operação Completa (All-in-One)")
    print("0) ❌ Sair")
    print("="*50)
    
    choice = input("\n👉 Selecione a operação: ")
    return choice

def process_choice(p, account, choice):
    if choice == '1':
        print(f"\n🔍 Consultando saldo para: {account['email']}")
        context, page, session = start_browser_session(p, account)
        if session:
            print(f"✅ Saldo Atual: {session.start_points} pts")
        context.close()

    elif choice == '2':
        print(f"\n🖥️ Iniciando Farming Desktop (Ghost Edition)...")
        context, page, session = start_browser_session(p, account)
        if session:
            execute_ghost_searches(session)
            earned = session.end_session()
            generate_report(session, earned)
        context.close()

    elif choice == '3':
        print(f"\n📱 Iniciando Farming Mobile (Moto G52 Edition)...")
        context, page, session = start_browser_session(p, account, mobile=True)
        if session:
            execute_searches(session, mobile=True)
            earned = session.end_session()
            generate_report(session, earned)
        context.close()

    elif choice == '4':
        print(f"\n🛠️ Executando Daily Set (Quizzes e Promoções)...")
        context, page, session = start_browser_session(p, account)
        if session:
            solve_daily_set(session)
            earned = session.end_session()
            generate_report(session, earned)
        context.close()

    elif choice == '5':
        print(f"\n🚀 Iniciando Operação Completa (All-in-One)...")
        # Desktop + Daily Set
        context, page, session = start_browser_session(p, account)
        if session:
            solve_daily_set(session)
            execute_ghost_searches(session)
            context.close()
            # Mobile
            context, page, session = start_browser_session(p, account, mobile=True)
            if session:
                execute_searches(session, mobile=True)
                earned = session.end_session()
                generate_report(session, earned)
        context.close()

def main():
    config_path = os.path.join("config", "accounts.json")
    try:
        with open(config_path, "r") as f:
            accounts = json.load(f)
    except:
        print("❌ Erro ao ler config/accounts.json")
        return

    while True:
        choice = run_menu()
        if choice == '0': break
        
        with sync_playwright() as p:
            for account in accounts:
                process_choice(p, account, choice)
        
        input("\nPressione Enter para voltar ao menu...")
        os.system('clear')

if __name__ == "__main__":
    main()
