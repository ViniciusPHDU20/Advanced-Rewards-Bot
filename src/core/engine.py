import asyncio
import os
import random
from typing import Dict, Any, List, Optional
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from src.utils.logger import logger

class RewardsEngine:
    """
    Motor de Automação Soberano v4.0.
    Utiliza injeção de Storage State para estabilidade máxima e bypass de travas.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.playwright = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        
        # Pasta de configuração blindada
        self.config_dir = os.path.expanduser("~/WORKSPACE_CORE/Advanced-Rewards-Bot/config")
        self.state_path = os.path.join(self.config_dir, "auth_state.json")
        os.makedirs(self.config_dir, exist_ok=True)

    async def initialize(self, headless: bool = False, user_agent: str = None):
        """Lança o navegador e injeta o estado de autenticação."""
        if not self.playwright:
            self.playwright = await async_playwright().start()

        logger.info("Lançando Chromium Engine...")
        self.browser = await self.playwright.chromium.launch(
            headless=headless,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )

        ua = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

        # Carrega o login se o arquivo existir
        storage_state = self.state_path if os.path.exists(self.state_path) else None
        
        self.context = await self.browser.new_context(
            user_agent=ua,
            viewport={'width': 1280, 'height': 720},
            storage_state=storage_state
        )

        self.page = await self.context.new_page()
        self.page.set_default_timeout(60000)
        
        # Visita o Bing para validar a injeção dos cookies
        try:
            await self.page.goto("https://www.bing.com", wait_until="domcontentloaded")
            logger.info("Sessão sincronizada com sucesso.")
        except:
            logger.warning("Timeout na sincronização, mas prosseguindo...")

    async def save_session(self):
        """Captura os cookies atuais e salva como estado de autenticação."""
        if self.context:
            await self.context.storage_state(path=self.state_path)
            logger.info(f"Chave soberana salva em: {self.state_path}")

    async def perform_search(self, keywords: List[str]):
        """Executa buscas simulando comportamento orgânico."""
        if not self.page: raise RuntimeError("Engine não preparada.")

        for term in keywords:
            try:
                url = f"https://www.bing.com/search?q={term.replace(' ', '+')}"
                await self.page.goto(url, wait_until="domcontentloaded")
                await asyncio.sleep(random.uniform(4, 8))
                logger.info(f"Busca Validada: {term}")
            except Exception as e:
                logger.error(f"Erro no termo {term}: {e}")

    async def shutdown(self):
        """Limpa os processos e libera a memória."""
        try:
            if self.context: await self.context.close()
            if self.browser: await self.browser.close()
            if self.playwright: await self.playwright.stop()
        except: pass
        logger.info("Sistema em standby.")
