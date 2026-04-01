import asyncio
import os
import subprocess
import random
from playwright.async_api import async_playwright

async def type_via_wayland(text: str):
    """Digita via Wayland simulando hardware real."""
    print(f"[GHOST] Injetando Teclas: {text}")
    # Foca na barra de endereços via hardware (Ctrl+L)
    subprocess.run(["wtype", "-M", "ctrl", "l", "-m", "ctrl"])
    await asyncio.sleep(1)
    
    # Digita o termo
    for char in text:
        subprocess.run(["wtype", char])
        await asyncio.sleep(random.uniform(0.02, 0.08))
    
    await asyncio.sleep(0.5)
    subprocess.run(["wtype", "-k", "Return"])

async def run_ghost_test():
    profile = os.path.expanduser("~/WORKSPACE_CORE/Advanced-Rewards-Bot/config/bot_profile")
    print("\033[96m[INJECTOR-HID] Iniciando injeção via Compositor (Wayland)...\033[0m")
    
    async with async_playwright() as pw:
        context = await pw.chromium.launch_persistent_context(
            user_data_dir=profile,
            headless=False,
            channel="msedge"
        )
        page = await context.new_page()
        
        # Teste 1: Busca via digitação na barra de endereço
        term = "tecnologia_soberana_" + str(random.randint(1000, 9999))
        print(f"[TESTE HID] Abrindo Bing e preparando digitação...")
        await page.goto("https://www.bing.com", wait_until="domcontentloaded")
        await asyncio.sleep(3)
        
        # Injeção física
        await type_via_wayland(term)
        
        print("[GHOST] Aguardando 20s para contabilização...")
        await asyncio.sleep(20)
        
        await context.close()
        print("\033[96m[INJECTOR-HID] Teste concluído.\033[0m")

if __name__ == "__main__":
    asyncio.run(run_ghost_test())
