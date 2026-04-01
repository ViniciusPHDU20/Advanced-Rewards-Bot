import asyncio
import os
import shutil
import random
from typing import Dict, Any, List, Optional
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from src.utils.logger import logger

class RewardsEngine:
    """
    Motor de Automação Soberano v5.2.
    Evasão HID Avançada e URL Spoofing Validado.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self._playwright = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        self.profile_path = os.path.expanduser("~/WORKSPACE_CORE/Advanced-Rewards-Bot/config/bot_profile")

    def _clean_locks(self):
        lock_files = ["SingletonLock", "SingletonSocket", "SingletonCookie"]
        if os.path.exists(self.profile_path):
            for root, _, files in os.walk(self.profile_path):
                for file in files:
                    if file in lock_files or ".com.google.Chrome" in file:
                        try: os.remove(os.path.join(root, file))
                        except: pass

    async def initialize(self, headless: bool = True, user_agent: str = None, is_mobile: bool = False):
        self._clean_locks()
        if not self._playwright:
            self._playwright = await async_playwright().start()

        ua = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        
        # Configuração de hardware autêntico
        viewport = {'width': 360, 'height': 800} if is_mobile else {'width': 1280, 'height': 720}
        
        logger.info(f"Lançando Motor {'MOBILE' if is_mobile else 'DESKTOP'} ({'Oculto' if headless else 'Visível'})...")
        
        try:
            self.context = await self._playwright.chromium.launch_persistent_context(
                user_data_dir=self.profile_path,
                channel="msedge",
                headless=headless,
                user_agent=ua,
                viewport=viewport,
                is_mobile=is_mobile,
                has_touch=is_mobile,
                ignore_default_args=["--enable-automation"],
                args=[
                    "--no-sandbox",
                    "--disable-blink-features=AutomationControlled",
                    "--no-first-run",
                    "--disable-infobars"
                ]
            )
            
            self.page = self.context.pages[0] if self.context.pages else await self.context.new_page()
            await self.page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.page.set_default_timeout(60000)
            
            # Validação rápida de sessão
            await self.page.goto("https://www.bing.com", wait_until="domcontentloaded")
            logger.info("Motor Sincronizado.")
            
        except Exception as e:
            logger.error(f"Erro no boot: {e}")
            await self.shutdown()
            raise e

    async def perform_search(self, keywords: List[str], is_mobile: bool = False):
        """Executa buscas com o método de URL validado e interação HID."""
        if not self.page: raise RuntimeError("Engine não preparada.")

        reward_param = "ML102W" if not is_mobile else "ML102V"
        
        for index, term in enumerate(keywords):
            try:
                # URL Soberana: Padrão validado no laboratório para crédito de pontos
                url = f"https://www.bing.com/search?q={term.replace(' ', '+')}&form={reward_param}&OCID={reward_param}&PUBL=REWARDS_DASHBOARD"
                
                logger.info(f"[{index+1}/{len(keywords)}] Injetando: {term}")
                await self.page.goto(url, wait_until="domcontentloaded")
                
                # Humanização: Delay randômico e Scroll dinâmico
                # Delays entre 15-22s são o 'sweet spot' da Microsoft agora
                await asyncio.sleep(random.uniform(15, 22))
                
                # Simula leitura orgânica
                if random.random() > 0.3:
                    for _ in range(random.randint(1, 3)):
                        await self.page.mouse.wheel(0, random.randint(300, 800))
                        await asyncio.sleep(random.uniform(1, 2))
                
            except Exception as e:
                logger.warning(f"Falha na injeção {term}: {e}")

    async def shutdown(self):
        try:
            if self.context: await self.context.close()
            if self._playwright: await self._playwright.stop()
        except: pass
        finally:
            self.context = None
            self.page = None
            self._playwright = None
            logger.info("Sistema em standby.")
