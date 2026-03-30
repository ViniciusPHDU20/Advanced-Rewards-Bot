import time
import random

def complete_daily_set(page):
    try:
        print("🛠️  Processando Daily Set...")
        page.goto('https://rewards.bing.com/', wait_until="domcontentloaded")
        time.sleep(5)

        cards = page.locator("mee-card")
        count = cards.count()
        
        for i in range(count):
            try:
                card = cards.nth(i)
                # Verifica se o card tem pontos a ganhar (não concluído)
                icon = card.locator(".mee-icon-CheckMark")
                if icon.count() > 0:
                    continue # Já concluído
                
                print(f"➡️  Atividade {i+1} iniciada...")
                with page.expect_popup() as popup_info:
                    card.locator("a").first.click(force=True)
                
                new_page = popup_info.value
                new_page.wait_for_load_state("domcontentloaded")
                solve_task(new_page)
                new_page.close()
                time.sleep(random.uniform(2, 4))
            except:
                continue
    except Exception as e:
        print(f"⚠️  Erro no Daily Set: {e}")

def solve_task(page):
    try:
        time.sleep(4)
        # Quizzes e Enquetes
        options = page.locator("div[class*='rq_option'], .btOption, #btoption, .b_cards, .rqOption")
        for _ in range(10): 
            if options.count() > 0:
                try:
                    options.first.click(timeout=3000)
                    time.sleep(2)
                except: break
            else: break
    except:
        pass

def complete_punch_cards(page):
    try:
        print("🎯  Processando Punch Cards...")
        page.goto('https://rewards.bing.com/', wait_until="domcontentloaded")
        punches = page.locator(".punchcard-container mee-card a")
        for i in range(punches.count()):
            try:
                with page.expect_popup() as popup_info:
                    punches.nth(i).click(force=True)
                new_page = popup_info.value
                time.sleep(5)
                new_page.close()
            except: continue
    except: pass

def complete_promotions(page):
    try:
        print("🎁  Processando Promoções Adicionais...")
        page.goto('https://rewards.bing.com/', wait_until="domcontentloaded")
        promos = page.locator(".promotional-container mee-card a")
        for i in range(promos.count()):
            try:
                if "CheckMark" in promos.nth(i).inner_html(): continue
                with page.expect_popup() as popup_info:
                    promos.nth(i).click(force=True)
                new_page = popup_info.value
                time.sleep(5)
                new_page.close()
            except: continue
    except: pass
