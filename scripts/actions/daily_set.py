import time
import random

def solve_daily_set(session):
    page = session.page
    try:
        print("🛠️  Processando Daily Set com Verificação de Validação...")
        page.goto('https://rewards.bing.com/', wait_until="networkidle")
        time.sleep(5)

        cards = page.locator("mee-card")
        count = cards.count()
        
        for i in range(count):
            try:
                card = cards.nth(i)
                # Verifica se o card é interativo (tem link) e visível
                if not card.is_visible() or card.locator("a").count() == 0:
                    continue

                # Verifica checkmark (se já concluiu)
                if card.locator(".mee-icon-CheckMark").count() > 0:
                    continue 

                title_locator = card.locator("h3")
                if title_locator.count() == 0: continue
                title = title_locator.inner_text()
                
                print(f"➡️  Iniciando atividade: {title}")
                
                # Tenta scroll com timeout menor para não travar
                try:
                    card.scroll_into_view_if_needed(timeout=5000)
                except: pass

                with page.expect_popup() as popup_info:
                    card.locator("a").first.evaluate("el => el.click()")
                
                new_page = popup_info.value
                new_page.wait_for_load_state("domcontentloaded")
                
                process_activity_page(new_page)
                
                new_page.close()
                time.sleep(random.uniform(6, 10)) # Aumentado para validar pontos
                session.log_activity(title, "Concluído")
                
            except Exception as e:
                # Se falhar em um card, pula para o próximo rapidamente
                continue
    except Exception as e:
        print(f"⚠️ Erro fatal no Daily Set: {e}")

def process_activity_page(page):
    try:
        # Espera carregar os elementos de interação
        time.sleep(8) 
        
        # Seletores de Quiz/Enquete em ordem de probabilidade
        selectors = [
            ".btOption", "#btoption", ".rqOption", ".rq_option", 
            ".b_cards", ".options", ".it_voted", "div[class*='rq_option']"
        ]
        
        for _ in range(15): 
            found = False
            for sel in selectors:
                options = page.locator(sel)
                if options.count() > 0:
                    # Tenta clicar no primeiro que for clicável
                    for i in range(options.count()):
                        opt = options.nth(i)
                        try:
                            if opt.is_visible():
                                opt.click(timeout=3000, force=True)
                                time.sleep(random.uniform(3, 5))
                                found = True
                                break
                        except: continue
                    if found: break
            if not found: break
                
        time.sleep(random.uniform(5, 8))
    except Exception as e:
        pass
