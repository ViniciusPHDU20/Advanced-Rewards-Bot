# main.py - AUTONOMOUS REWARDS ENGINE

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
    # 🖥️ SESSION START
    print(f"🖥️  Starting farming for {account['email']}...")
    try:
        context, page = create_browser(p, mobile=False)
        if login(page, account['email'], account['password']):
            # 🏁 Capture initial balance
            starting_pts = get_current_points(page)
            print(f"💰 Initial Balance: {starting_pts} pts")

            # Execute Desktop tasks
            complete_daily_set(page)
            complete_punch_cards(page)
            complete_promotions(page)
            perform_searches(page, mobile=False)
            
            # Execute Mobile tasks
            context.close()
            
            print(f"📱 Switching to MOBILE mode...")
            context, page = create_browser(p, mobile=True)
            if login(page, account['email'], account['password']):
                perform_searches(page, mobile=True)
            
            # 🏁 Capture final balance and calculate earnings
            final_pts = get_current_points(page)
            earned = final_pts - starting_pts
            
            print(f"\n💎 POINTS EARNED THIS SESSION: {earned}")
            log_points(page, session_earned=earned)
            
            send_discord_notification(account['email'], f"Session completed! Earned: +{earned} pts | Total: {final_pts} pts ✅")
            
        context.close()
    except Exception as e:
        print(f"⚠️  Session Error: {e}")

def main():
    try:
        with open("config/accounts.json", "r") as f:
            accounts = json.load(f)
    except Exception as e:
        print(f"❌ Error reading accounts.json: {e}")
        return

    with sync_playwright() as p:
        for account in accounts:
            print(f"\n🚀 [AUTONOMOUS] Processing account: {account['email']}")
            farm_account(p, account)

if __name__ == "__main__":
    print("🤖 AUTOMATION BOT - SYSTEM ONLINE")
    main()
    print("\n🏁 PROCESS FINISHED.")
