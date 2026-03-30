import time
import random

def complete_daily_set(page):
    try:
        print("🛠️ Completando Daily Set...")
        page.goto('https://rewards.bing.com/', wait_until="networkidle")
        time.sleep(5)

        # Seleciona todos os cards clicáveis
        cards = page.locator("mee-card")
        count = cards.count()
        
        if count == 0:
            print("⚠️ Daily Sets não encontrados!")
            return

        print(f"🔎 Encontrados {count} cards potenciais.")

        for i in range(count):
            try:
                # Verifica se é um card de Daily Set (geralmente tem pontos visíveis)
                card = cards.nth(i)
                if not card.is_visible(): continue
                
                print(f"➡️ Processando card {i+1}...")
                
                # Clica no link do card em uma nova aba
                with page.expect_popup() as popup_info:
                    card.locator("a").first.click(force=True)
                
                new_page = popup_info.value
                new_page.wait_for_load_state("domcontentloaded")
                
                solve_task(new_page)
                new_page.close()
                time.sleep(random.uniform(2, 5))
                
            except Exception as e:
                # print(f"⚠️ Ignorando card {i+1} (provavelmente já concluído ou não-clicável)")
                pass

    except Exception as e:
        print(f"⚠️ Erro no Daily Set: {e}")

def solve_task(page):
    try:
        time.sleep(5)
        # Tenta responder Quizzes/Votações clicando na primeira opção disponível
        options = page.locator("div[class*='rq_option'], .btOption, #btoption, .b_cards")
        if options.count() > 0:
            print("🧠 Interagindo com tarefa interativa...")
            for _ in range(5): 
                if options.count() > 0:
                    try:
                        options.first.click(timeout=5000)
                        time.sleep(3)
                    except: break
                else: break
        else:
            print("📰 Tarefa de leitura ou simples clique concluída.")
            time.sleep(5)

    except Exception as e:
        pass

def complete_promotions(page):
    try:
        print("🎯 Completando promoções extras...")
        page.goto('https://rewards.bing.com/', wait_until="domcontentloaded")
        promos = page.locator(".promotional-container mee-card a")
        for i in range(min(promos.count(), 10)):
            try:
                with page.expect_popup() as popup_info:
                    promos.nth(i).click(force=True)
                new_page = popup_info.value
                time.sleep(random.uniform(3, 6))
                new_page.close()
            except: pass
    except: pass
