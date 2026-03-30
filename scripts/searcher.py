import random
import time
from scripts.query_generator import generate_smart_query

BASE_TOPICS = [
    "technology", "sports", "health", "movies", "news", "games",
    "travel", "music", "education", "history", "food", "science",
    "AI trends 2026", "Arch Linux optimization", "Hyprland workflow", "cybersecurity news"
]

def perform_searches(page, mobile=False):
    try:
        search_count = 30 if not mobile else 20
        mode = "MOBILE" if mobile else "DESKTOP"
        
        print(f"🚀 Iniciando {search_count} buscas em modo {mode} (Protocolo Humanizado)...")

        for i in range(search_count):
            base_topic = random.choice(BASE_TOPICS)
            query = generate_smart_query(base_topic)

            try:
                # 🌐 Navega para o Bing com timeout longo
                page.goto('https://www.bing.com/', wait_until="domcontentloaded", timeout=60000)
                time.sleep(random.uniform(2, 4))
                
                # ⌨️ Digitação humana (com delay entre teclas)
                search_box = page.locator('input[name="q"], textarea[name="q"], #sb_form_q').first
                search_box.wait_for(state="visible", timeout=15000)
                search_box.click()
                search_box.fill("") # Limpa
                
                # Digita como humano
                for char in query:
                    page.keyboard.type(char)
                    time.sleep(random.uniform(0.05, 0.2))
                
                time.sleep(1)
                page.keyboard.press('Enter')
                
                print(f"🔎 [{mode}] Buscando: {query} ({i+1}/{search_count})")
                
                # 🛡️ BYPASS DE DETECÇÃO: Comportamento Humano Pós-Busca
                time.sleep(random.uniform(3, 6))
                
                # 🖱️ Scroll aleatório para fingir leitura
                scroll_amount = random.randint(300, 800)
                page.mouse.wheel(0, scroll_amount)
                time.sleep(random.uniform(1, 3))
                page.mouse.wheel(0, -scroll_amount)
                
                # 🖱️ Movimento de mouse aleatório
                page.mouse.move(random.randint(100, 500), random.randint(100, 500))
                
                # Espera final para validar a busca no servidor
                time.sleep(random.uniform(5, 10))
                
            except Exception as e:
                print(f"⚠️ Falha na busca {i+1}, tentando recuperar... {e}")
                continue

    except Exception as e:
        print(f"⚠️ Erro fatal nas buscas {mode}: {e}")
