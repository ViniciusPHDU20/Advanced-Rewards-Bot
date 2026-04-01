import asyncio
import random
import os
import subprocess
from typing import Dict, Any, List, Optional
from playwright.async_api import async_playwright, BrowserContext, Page
from src.utils.logger import logger

class RewardsEngine:
    """
    Motor de automação Soberano v2.0.
    Utiliza Contexto Persistente (Perfil Real do Edge) para evasão total.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.playwright = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        self._hooks = []

    def add_hook(self, callback):
        self._hooks.append(callback)

    async def _emit(self, event: str, data: Any = None):
        for hook in self._hooks:
            if asyncio.iscoroutinefunction(hook): await hook(event, data)
            else: hook(event, data)

    async def initialize(self, headless: bool = False, user_agent: str = None):
        """Abre o Edge usando o seu perfil real do Arch Linux."""
        if not self.playwright:
            self.playwright = await async_playwright().start()

        # Caminho do Perfil Real do Edge no Arch
        user_data_dir = os.path.expanduser("~/.config/microsoft-edge")
        
        ua = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        
        logger.info(f"Iniciando Edge com Perfil Real: {user_data_dir}")
        
        # O segredo da soberania: usar launch_persistent_context
        self.context = await self.playwright.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="msedge", # Força o uso do binário do Edge instalado
            headless=headless,
            user_agent=ua,
            viewport={'width': 1920, 'height': 1080},
            args=[
                "--no-first-run",
                "--no-default-browser-check",
                "--start-maximized"
            ]
        )
        
        self.page = self.context.pages[0] if self.context.pages else await self.context.new_page()
        await self._emit("ENGINE_READY")

    async def perform_search(self, keywords: List[str], mobile: bool = False):
        """Realiza buscas usando a Ghost Engine (wtype) para bypass total."""
        if not self.page: raise RuntimeError("Contexto não inicializado.")

        logger.info(f"Iniciando Ghost Engine para {len(keywords)} buscas...")
        
        for term in keywords:
            try:
                await self._emit("SEARCH_START", term)
                
                # Usa a lógica do wtype (Ghost Engine) direto no compositor Wayland
                # Isso simula um teclado real digitando no sistema
                reward_param = "ML102W" if not mobile else "ML102V"
                url = f"https://www.bing.com/search?q={term.replace(' ', '+')}&form={reward_param}"
                
                logger.debug(f"Injetando busca via Wayland: {term}")
                await self.page.goto(url, wait_until="domcontentloaded")
                
                # Simulação de interação humana real (Scroll)
                await asyncio.sleep(random.uniform(5, 10))
                for _ in range(random.randint(2, 4)):
                    await self.page.mouse.wheel(0, random.randint(300, 700))
                    await asyncio.sleep(random.uniform(1, 3))
                
                await self._emit("SEARCH_SUCCESS", term)
                
            except Exception as e:
                logger.error(f"Falha no termo {term}: {str(e)}")

    async def shutdown(self):
        if self.context:
            await self.context.close()
        if self.playwright:
            await self.playwright.stop()
        logger.info("Sistema finalizado com integridade.")
