import asyncio
import os
from src.core.engine import RewardsEngine

async def debug_mobile():
    engine = RewardsEngine({})
    mobile_ua = "Mozilla/5.0 (Linux; Android 13; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    
    print("[DEBUG] Lançando motor mobile visível para análise...")
    await engine.initialize(headless=True, user_agent=mobile_ua, is_mobile=True)
    page = engine.page
    
    await page.goto("https://www.bing.com", wait_until="networkidle")
    await asyncio.sleep(5)
    
    # Captura a estrutura para eu ver os seletores reais
    content = await page.content()
    with open("/tmp/bing_mobile.html", "w") as f:
        f.write(content)
        
    await page.screenshot(path="/tmp/bing_mobile.png")
    print("[DEBUG] Estrutura e Print salvos em /tmp/bing_mobile.*")
    
    await engine.shutdown()

if __name__ == "__main__":
    asyncio.run(debug_mobile())
