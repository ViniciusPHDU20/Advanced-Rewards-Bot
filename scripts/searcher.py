import random
import time
from scripts.query_generator import generate_smart_query

BASE_TOPICS = [
    "technology", "sports", "health", "movies", "news", "games",
    "travel", "music", "education", "history", "food", "science",
    "AI news", "Arch Linux tips", "Hyprland config", "crypto trends"
]

def perform_searches(page, mobile=False):
    try:
        search_count = 30 if not mobile else 20
        mode = "MOBILE" if mobile else "DESKTOP"
        
        print(f"🚀 Iniciando {search_count} buscas em modo {mode}...")

        for i in range(search_count):
            base_topic = random.choice(BASE_TOPICS)
            query = generate_smart_query(base_topic)

            page.goto('https://www.bing.com/', wait_until="domcontentloaded")
            
            # Seletor robusto: tenta vários nomes comuns de input do Bing
            search_box = page.locator('input[name="q"], textarea[name="q"], #sb_form_q').first
            
            try:
                search_box.wait_for(state="visible", timeout=10000)
                search_box.fill(query)
                search_box.press('Enter')
                print(f"🔎 [{mode}] Buscando: {query} ({i+1}/{search_count})")
            except:
                print(f"⚠️ Campo de busca não encontrado no loop {i+1}. Tentando próxima...")
                continue

            time.sleep(random.uniform(5, 12))

    except Exception as e:
        print(f"⚠️ Erro nas buscas {mode}: {e}")
