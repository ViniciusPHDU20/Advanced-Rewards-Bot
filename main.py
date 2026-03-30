# main.py - MODO SOBERANO AUTÔNOMO

import time
import json
from playwright.sync_api import sync_playwright
from scripts.browser_manager import create_browser
from scripts.login_manager import login
from scripts.promotions import complete_daily_set, complete_promotions
from scripts.searcher import perform_searches

def farm_account(p, account):
    # 🖥️ ETAPA 1: DESKTOP
    print(f"🖥️ [1/2] Iniciando modo DESKTOP para {account['email']}...")
    try:
        context, page = create_browser(p, mobile=False)
        if login(page, account['email'], account['password']):
            complete_daily_set(page)
            complete_promotions(page)
            perform_searches(page, mobile=False)
            print("✅ Desktop concluído.")
        context.close()
    except Exception as e:
        print(f"⚠️ Falha no modo Desktop: {e}")

    # 📱 ETAPA 2: MOBILE
    print(f"📱 [2/2] Iniciando modo MOBILE para {account['email']}...")
    try:
        context, page = create_browser(p, mobile=True)
        if login(page, account['email'], account['password']):
            perform_searches(page, mobile=True)
            print("✅ Mobile concluído.")
        context.close()
    except Exception as e:
        print(f"⚠️ Falha no modo Mobile: {e}")

def main():
    with open("config/accounts.json", "r") as f:
        accounts = json.load(f)

    with sync_playwright() as p:
        for account in accounts:
            print(f"\n🚀 [AUTÔNOMO] Processando conta: {account['email']}")
            farm_account(p, account)

if __name__ == "__main__":
    print("🤖 JESUS REWARDS BOT - INVISÍVEL & DUPLO MODO")
    main()
    print("\n🏁 MISSÃO FINALIZADA.")
