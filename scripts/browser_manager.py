import os
import shutil
import tempfile
from playwright.sync_api import sync_playwright

def create_browser(playwright, mobile=False):
    original_profile = os.path.expanduser("~/.config/microsoft-edge")
    temp_profile = os.path.join(tempfile.gettempdir(), f"playwright_rewards_{'mobile' if mobile else 'desktop'}")
    
    def ignore_patterns(path, names):
        return [n for name in names if n.startswith('Singleton') or n.startswith('Cache') or n in ['Code Cache', 'GPUCache', 'lock']]

    try:
        if os.path.exists(temp_profile):
            shutil.rmtree(temp_profile, ignore_errors=True)
        shutil.copytree(original_profile, temp_profile, ignore=ignore_patterns, dirs_exist_ok=True)
    except: pass

    edge_path = "/usr/bin/microsoft-edge-stable"
    
    # 🕵️ MODO HEADLESS ATIVADO (INVISÍVEL)
    browser_context = playwright.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        executable_path=edge_path,
        headless=True,
        args=[
            "--password-store=basic",
            "--use-mock-keychain",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--mute-audio"
        ],
        viewport={"width": 1280, "height": 720} if not mobile else {"width": 412, "height": 915},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0" if not mobile else "Mozilla/5.0 (Linux; Android 16; moto g52 Build/BP4A.251205.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 EdgA/122.0.0.0"
    )

    page = browser_context.pages[0]
    page.add_init_script("Object.defineProperty(navigator, 'webdriver', { get: () => undefined });")
    
    return browser_context, page
