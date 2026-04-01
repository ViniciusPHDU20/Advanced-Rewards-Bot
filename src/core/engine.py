import asyncio
import os
import shutil
import random
from typing import Dict, Any, List, Optional
from playwright.async_api import async_playwright, BrowserContext, Page
from src.utils.logger import logger

class RewardsEngine:
    """
    Motor de Automação Soberano v4.2.
    Injeção de parâmetros oficiais do Microsoft Rewards para validação de pontos.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self._playwright = None
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

    async def initialize(self, headless: bool = False, user_agent: str = None):
        self._clean_locks()
        if not self._playwright:
            self._playwright = await async_playwright().start()

        ua = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        
        logger.info(f"Lançando Navegador Soberano...")
        try:
            self.context = await self._playwright.chromium.launch_persistent_context(
                user_data_dir=self.profile_path,
                channel="msedge",
                headless=headless,
                user_agent=ua,
                viewport={'width': 1280, 'height': 720},
                args=["--no-sandbox", "--disable-blink-features=AutomationControlled", "--no-first-run"]
            )
            self.page = self.context.pages[0] if self.context.pages else await self.context.new_page()
            self.page.set_default_timeout(60000)
            await self.page.goto("https://www.bing.com", wait_until="domcontentloaded")
            logger.info("Sincronização OK.")
        except Exception as e:
            logger.error(f"Erro no lançamento: {e}")
            await self.shutdown()
            raise e

    async def perform_search(self, keywords: List[str], is_mobile: bool = False):
        """Executa buscas com parâmetros de injeção de pontos (ML102W / ML102V)."""
        if not self.page: raise RuntimeError("Engine não inicializada.")

        # Parâmetros Soberanos para contabilização de pontos
        reward_param = "ML102W" if not is_mobile else "ML102V"
        
        for term in keywords:
            try:
                # URL completa com rastreamento de recompensa
                url = f"https://www.bing.com/search?q={term.replace(' ', '+')}&form={reward_param}&OCID={reward_param}&PUBL=REWARDS_DASHBOARD"
                
                await self.page.goto(url, wait_until="domcontentloaded")
                
                # Jitter humano (Microsoft detecta se for muito rápido)
                await asyncio.sleep(random.uniform(10, 18))
                
                if random.random() > 0.5:
                    await self.page.mouse.wheel(0, random.randint(400, 900))
                    await asyncio.sleep(2)
                
                logger.info(f"Ponto Computado: {term}")
            except Exception as e:
                logger.warning(f"Falha no ponto: {e}")

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
