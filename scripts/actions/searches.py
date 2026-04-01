import random
import time
from scripts.query_generator import generate_smart_query
from scripts.core.wayland_engine import WaylandEngine

def execute_searches(session, mobile=False):
    # Se for Desktop, usamos o Motor Ghost (Wayland Native) para bypass total
    if not mobile:
        execute_ghost_searches(session)
        return

    # Se for Mobile, mantemos o motor Playwright (que costuma pontuar bem)
    page = session.page
    try:
        search_count = 65 # Cota Nível 2 Mobile
        print(f"🚀 Iniciando motor de busca MOBILE (Playwright)...")
        
        for i in range(search_count):
            query = generate_smart_query()
            try:
                # URL Nativa para Mobile
                search_url = f"https://www.bing.com/search?q={query.replace(' ', '+')}&form=ML102V&OCID=ML102V&PUBL=REWARDS_DASHBOARD"
                page.goto(search_url, wait_until="domcontentloaded", timeout=60000)
                print(f"🔎 [MOBILE] ({i+1}/{search_count}) : {query}")
                time.sleep(random.uniform(12, 18))
                page.mouse.wheel(0, random.randint(300, 600))
                time.sleep(random.uniform(2, 4))
            except: continue
        session.log_activity("Buscas MOBILE", "Concluído")
    except Exception as e:
        print(f"⚠️ Erro no motor Mobile: {e}")

def execute_ghost_searches(session):
    """Motor Fantasma para Desktop (Wayland/Hyprland)"""
    search_count = 95 # Cota Nível 2 PC
    print(f"👻 Iniciando motor de busca GHOST (Wayland Native)...")
    
    engine = WaylandEngine()
    address = engine.get_edge_address()
    
    if not address:
        print("❌ Janela do Edge não encontrada. Certifique-se que o Edge está aberto.")
        return

    for i in range(search_count):
        query = generate_smart_query()
        try:
            # Foca e digita via OS
            engine.focus_window(address)
            engine.type_query(query)
            
            print(f"🔎 [GHOST] ({i+1}/{search_count}) : {query}")
            
            # Interação profunda e retenção (Bypass Nível 2)
            engine.human_interaction()
            
            # Pausa de fadiga
            if (i + 1) % 15 == 0:
                wait = random.randint(45, 90)
                print(f"😴 Pausa de fadiga humana: {wait}s...")
                time.sleep(wait)
        except Exception as e:
            print(f"⚠️ Erro na busca {i+1}: {e}")
            continue

    session.log_activity("Buscas DESKTOP (GHOST)", "Concluído")
