import asyncio
import random
from src.core.engine import RewardsEngine
from src.utils.logger import logger

class SearchAutomation:
    """Módulo especializado em emulação de buscas Desktop e Mobile."""
    
    def __init__(self, engine: RewardsEngine):
        self.engine = engine

    async def run_desktop_searches(self, count: int = 35):
        """Executa buscas simulando um ambiente Desktop."""
        logger.info(f"Iniciando {count} buscas DESKTOP...")
        
        terms = [
            "configuração arch linux 2026", "nvidia drivers arch wiki",
            "hyprland status bar custom", "vulkan layers guide",
            "melhores games steam deck", "clima em cosmópolis",
            "cotação btc hoje", "notícias inteligência artificial",
            "lançamentos hardware 2026", "como otimizar xeon v2"
        ]
        search_list = random.sample(terms * (count // len(terms) + 1), count)
        
        # Passar is_mobile=False para usar ML102W
        await self.engine.perform_search(search_list, is_mobile=False)
        logger.info("Ciclo DESKTOP finalizado.")

    async def run_mobile_searches(self, count: int = 25):
        """Executa buscas emulando o Moto G52 (Amoled Shadow)."""
        logger.info(f"Trocando para identidade MOBILE (Moto G52)...")
        
        mobile_ua = "Mozilla/5.0 (Linux; Android 16; Moto G52) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        
        # Reinicia o contexto com o User-Agent mobile preservando o login
        await self.engine.initialize(headless=False, user_agent=mobile_ua)
        
        terms = ["restaurantes próximos", "preço gasolina hoje", "jogos mobile free", "filmes em cartaz"]
        search_list = random.sample(terms * (count // len(terms) + 1), count)
        
        # Passar is_mobile=True para usar ML102V
        await self.engine.perform_search(search_list, is_mobile=True)
        logger.info("Ciclo MOBILE finalizado.")
