import os
import shutil
import tempfile
from playwright.sync_api import sync_playwright

def create_browser(playwright, mobile=False):
    bot_profile = os.path.join(os.path.expanduser("~"), ".config", "rewards_automation_profile")
    edge_path = "/usr/bin/microsoft-edge-stable"
    
    # User-Agents Oficiais
    desktop_ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    mobile_ua = "Mozilla/5.0 (Linux; Android 16; moto g52 Build/BP4A.251205.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 EdgA/122.0.0.0"

    # 🚨 MODO VISÍVEL ATIVADO (Headless=False)
    # Isso abre o navegador na sua tela do Hyprland para bypass total de hardware
    browser_context = playwright.chromium.launch_persistent_context(
        user_data_dir=bot_profile,
        executable_path=edge_path,
        headless=False, # MUDANÇA CRÍTICA
        locale="pt-BR",
        timezone_id="America/Sao_Paulo",
        args=[
            "--password-store=basic",
            "--use-mock-keychain",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--mute-audio",
            "--disable-blink-features=AutomationControlled",
            "--start-maximized"
        ],
        viewport=None, # Usa o tamanho real da janela
        user_agent=desktop_ua if not mobile else mobile_ua
    )

    page = browser_context.pages[0]
    
    # Scripts de Ocultação de Automação
    page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        window.chrome = { runtime: {} };
        Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
    """)
    
    return browser_context, page
