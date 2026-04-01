import asyncio
import random
from src.core.engine import RewardsEngine
from src.utils.logger import logger

class SearchAutomation:
    """Módulo de automação de buscas com cadência humana."""
    
    def __init__(self, engine: RewardsEngine):
        self.engine = engine

    async def run_desktop_searches(self, count: int = 35):
        """Executa buscas Desktop com o padrão validado."""
        terms = [
            "configuração arch linux 2026", "nvidia drivers arch wiki",
            "hyprland status bar custom", "vulkan layers guide",
            "melhores games steam deck", "clima em cosmópolis",
            "cotação btc hoje", "notícias inteligência artificial",
            "como otimizar xeon v2", "kernel linux-zen performance"
        ]
        search_list = random.sample(terms * (count // len(terms) + 1), count)
        # Garante que o motor saiba que é Desktop
        await self.engine.perform_search(search_list, is_mobile=False)

    async def run_mobile_searches(self, count: int = 25):
        """Executa buscas Mobile emulando o Moto G52 de forma silenciosa."""
        mobile_ua = "Mozilla/5.0 (Linux; Android 16; Moto G52) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        
        # CORREÇÃO CRÍTICA: Passar is_mobile=True para ativar hardware de celular no Playwright
        logger.info("Configurando ambiente MOBILE Soberano...")
        await self.engine.shutdown()
        await self.engine.initialize(headless=True, user_agent=mobile_ua, is_mobile=True)
        
        terms = ["restaurantes próximos", "preço gasolina hoje", "jogos mobile", "clima amanhã", "notícias esportes"]
        search_list = random.sample(terms * (count // len(terms) + 1), count)
        
        await self.engine.perform_search(search_list, is_mobile=True)
