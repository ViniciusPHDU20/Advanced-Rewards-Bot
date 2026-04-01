import asyncio
import os
import random
from typing import Dict, Any, List, Optional
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from src.utils.logger import logger

class RewardsEngine:
    """
    Motor de Automação Soberano v5.0.
    Engenharia de Injeção de Pontos validada via Lab de Pesquisa.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self._playwright = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        self.profile_path = os.path.expanduser("~/WORKSPACE_CORE/Advanced-Rewards-Bot/config/bot_profile")

    def _clean_locks(self):
        """Elimina travas de processo para evitar erros de lançamento."""
        lock_files = ["SingletonLock", "SingletonSocket", "SingletonCookie"]
        if os.path.exists(self.profile_path):
            for root, _, files in os.walk(self.profile_path):
                for file in files:
                    if file in lock_files or ".com.google.Chrome" in file:
                        try: os.remove(os.path.join(root, file))
                        except: pass

    async def initialize(self, headless: bool = True, user_agent: str = None):
        """Inicializa o motor em modo furtivo."""
        self._clean_locks()
        if not self._playwright:
            self._playwright = await async_playwright().start()

        ua = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        
        logger.info(f"Iniciando Motor {'OCULTO' if headless else 'VISÍVEL'}...")
        
        try:
            self.context = await self._playwright.chromium.launch_persistent_context(
                user_data_dir=self.profile_path,
                channel="msedge",
                headless=headless,
                user_agent=ua,
                viewport={'width': 1280, 'height': 720},
                ignore_default_args=["--enable-automation"],
                args=[
                    "--no-sandbox",
                    "--disable-blink-features=AutomationControlled",
                    "--disable-infobars",
                    "--hide-scrollbars"
                ]
            )
            
            self.page = self.context.pages[0] if self.context.pages else await self.context.new_page()
            # Script de bypass de detecção de automação
            await self.page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            self.page.set_default_timeout(60000)
            logger.info("Motor sincronizado.")
            
        except Exception as e:
            logger.error(f"Falha no boot do motor: {e}")
            await self.shutdown()
            raise e

    async def perform_search(self, keywords: List[str], is_mobile: bool = False):
        """Executa o padrão de injeção validado no laboratório."""
        if not self.page: raise RuntimeError("Motor não inicializado.")

        reward_param = "ML102W" if not is_mobile else "ML102V"
        mode_str = "MOBILE" if is_mobile else "DESKTOP"
        
        logger.info(f"Iniciando ciclo de farm {mode_str}...")

        for index, term in enumerate(keywords):
            try:
                # URL parametrizada para forçar o crédito dos pontos
                url = f"https://www.bing.com/search?q={term.replace(' ', '+')}&form={reward_param}&OCID={reward_param}&PUBL=REWARDS_DASHBOARD"
                
                await self.page.goto(url, wait_until="domcontentloaded")
                
                # Human-like interaction (Scroll e Pausa)
                delay = random.uniform(15, 25)
                logger.info(f"[{index+1}/{len(keywords)}] {term} | Aguardando {delay:.1f}s")
                
                # Movimentos de mouse e scroll para validar a atividade
                for _ in range(random.randint(2, 4)):
                    await asyncio.sleep(random.uniform(2, 5))
                    await self.page.mouse.wheel(0, random.randint(400, 1000))
                
                await asyncio.sleep(delay / 2)
                
            except Exception as e:
                logger.warning(f"Erro na injeção {term}: {e}")

    async def shutdown(self):
        try:
            if self.context: await self.context.close()
            if self._playwright: await self._playwright.stop()
        except: pass
        finally:
            self.context = None
            self.page = None
            self._playwright = None
            logger.info("Motor em standby.")
