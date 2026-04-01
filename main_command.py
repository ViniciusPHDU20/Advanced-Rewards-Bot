# main_command.py - Backend Bridge para GUI

import sys
import json
import os
from playwright.sync_api import sync_playwright

# Core Imports
from scripts.browser_manager import create_browser
from scripts.login_manager import login
from scripts.models.session import RewardSession
from scripts.actions.daily_set import solve_daily_set
from scripts.actions.searches import execute_searches, execute_ghost_searches
from scripts.core.reporter import generate_report

def start_browser_session(p, account, mobile=False):
    context, page = create_browser(p, mobile=mobile)
    session = RewardSession(page, account['email'])
    if login(page, account['email'], account['password']):
        session.start_session()
        return context, page, session
    return context, page, None

def main():
    if len(sys.argv) < 2:
        return

    choice = sys.argv[1]
    
    config_path = os.path.join("config", "accounts.json")
    with open(config_path, "r") as f:
        accounts = json.load(f)
    
    account = accounts[0] # Processa a conta principal

    with sync_playwright() as p:
        if choice == '1': # Status
            context, page, session = start_browser_session(p, account)
            if session:
                print(f"✅ Saldo Atual: {session.start_points} pts")
            context.close()

        elif choice == '2': # Desktop
            context, page, session = start_browser_session(p, account)
            if session:
                execute_ghost_searches(session)
                session.end_session()
            context.close()

        elif choice == '3': # Mobile
            context, page, session = start_browser_session(p, account, mobile=True)
            if session:
                execute_searches(session, mobile=True)
                session.end_session()
            context.close()

        elif choice == '4': # Daily
            context, page, session = start_browser_session(p, account)
            if session:
                solve_daily_set(session)
                session.end_session()
            context.close()

        elif choice == '5': # Full
            context, page, session = start_browser_session(p, account)
            if session:
                solve_daily_set(session)
                execute_ghost_searches(session)
                context.close()
                context, page, session = start_browser_session(p, account, mobile=True)
                if session:
                    execute_searches(session, mobile=True)
                    session.end_session()
            context.close()

if __name__ == "__main__":
    main()
