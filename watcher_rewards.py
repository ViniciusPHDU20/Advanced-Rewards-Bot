import asyncio
import os
import sys
from playwright.async_api import async_playwright
from datetime import datetime

async def watch_points():
    """Monitor de Pontos em Tempo Real - Estilo Cheat Engine."""
    profile_path = os.path.expanduser("~/WORKSPACE_CORE/Advanced-Rewards-Bot/config/bot_profile")
    
    print("\033[95m[WATCHER] Iniciando vigilância de pontos Microsoft Rewards...\033[0m")
    
    async with async_playwright() as pw:
        # Abre o navegador em modo oculto apenas para vigiar os valores
        context = await pw.chromium.launch_persistent_context(
            user_data_dir=profile_path,
            headless=True,
            args=["--no-sandbox"]
        )
        page = await context.new_page()
        
        last_points = 0
        
        while True:
            try:
                # Navega para o dashboard de forma agressiva para forçar atualização
                await page.goto("https://rewards.bing.com/dashboard", wait_until="domcontentloaded")
                
                # Seletor de pontos do Rewards
                points_element = await page.wait_for_selector(".pointsValue", timeout=10000)
                current_points_text = await points_element.inner_text()
                current_points = int(current_points_text.replace(".", "").replace(",", ""))
                
                now = datetime.now().strftime("%H:%M:%S")
                
                if current_points != last_points:
                    diff = current_points - last_points if last_points != 0 else 0
                    color = "\033[92m" if diff > 0 else "\033[94m"
                    print(f"[{now}] \033[1mVALOR ALTERADO:\033[0m {color}{current_points} pts\033[0m (Var: +{diff})")
                    last_points = current_points
                else:
                    print(f"[{now}] Valor estagnado: {current_points} pts", end="\r")
                
                # Aguarda 10 segundos para a próxima varredura para não saturar a conta
                await asyncio.sleep(10)
                
            except Exception as e:
                print(f"\n\033[91m[!] Erro na varredura: {e}\033[0m")
                await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(watch_points())
    except KeyboardInterrupt:
        print("\n\033[95m[WATCHER] Vigilância encerrada por JESUS.\033[0m")
