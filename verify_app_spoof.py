import asyncio
import os
import random
from src.core.engine import RewardsEngine
from src.automation.stats import StatsAutomation

async def run_app_spoof_test():
    engine = RewardsEngine({})
    stats = StatsAutomation(engine)
    
    await engine.initialize(headless=True)
    pts_start = await stats.get_current_points()
    await engine.shutdown()
    print(f"SALDO INICIAL: {pts_start}")

    # SIMULAÇÃO DE APP REAL (ANDROID BING APP)
    mobile_ua = "Mozilla/5.0 (Linux; Android 16; Moto G52 Build/S1RMS32.68-43-11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 SearchApp/Bing/15.9.411228302"
    
    await engine.initialize(headless=False, user_agent=mobile_ua, is_mobile=True)
    
    # Injeta cabeçalhos extras que o App real envia
    await engine.context.set_extra_http_headers({
        "X-MS-Bing-App-Version": "15.9.411228302",
        "X-Requested-With": "com.microsoft.bing"
    })
    
    term = f"noticia_urgente_mobile_{random.randint(1000, 9999)}"
    url = f"https://www.bing.com/search?q={term}&form=ML102V&OCID=ML102V&PUBL=REWARDS_DASHBOARD"
    
    print(f"Injetando via App Spoofing: {url}")
    await engine.page.goto(url, wait_until="domcontentloaded")
    await asyncio.sleep(25)
    await engine.page.mouse.wheel(0, 500)
    await asyncio.sleep(10)
    
    await engine.shutdown()
    print("[!] Aguardando sincronização (60s)...")
    await asyncio.sleep(60)
    
    await engine.initialize(headless=True)
    pts_final = await stats.get_current_points()
    await engine.shutdown()
    
    print(f"SALDO FINAL: {pts_final}")
    if pts_final > pts_start:
        print("!!! SUCESSO: APP SPOOFING VALIDADO !!!")
    else:
        print("--- FALHA: A MICROSOFT EXIGE DISPOSITIVO FÍSICO ---")

if __name__ == "__main__":
    asyncio.run(run_app_spoof_test())
