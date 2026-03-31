import os
import shutil
import tempfile
from playwright.sync_api import sync_playwright

def create_browser(playwright, mobile=False):
    # Usamos o perfil persistente que acabamos de selar
    bot_profile = os.path.join(os.path.expanduser("~"), ".config", "rewards_automation_profile")
    
    edge_path = "/usr/bin/microsoft-edge-stable"
    
    # 🕵️ MODO FANTASMA ATIVADO (HEADLESS = TRUE)
    browser_context = playwright.chromium.launch_persistent_context(
        user_data_dir=bot_profile,
        executable_path=edge_path,
        headless=True, 
        args=[
            "--password-store=basic",
            "--use-mock-keychain",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--mute-audio",
            "--ozone-platform-hint=auto"
        ],
        viewport={"width": 1280, "height": 720} if not mobile else {"width": 412, "height": 915},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0" if not mobile else "Mozilla/5.0 (Linux; Android 16; moto g52 Build/BP4A.251205.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 EdgA/122.0.0.0"
    )

    page = browser_context.pages[0]
    page.add_init_script("Object.defineProperty(navigator, 'webdriver', { get: () => undefined });")
    
    return browser_context, page
