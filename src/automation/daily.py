import asyncio
import random
from src.core.engine import RewardsEngine
from src.utils.logger import logger

class DailyAutomation:
    """Módulo especializado em resolver desafios diários (Daily Set)."""
    
    def __init__(self, engine: RewardsEngine):
        self.engine = engine

    async def solve_daily_set(self):
        """Identifica e resolve os cards de atividades diárias."""
        page = self.engine.page
        if not page: return

        try:
            logger.info("🛠️  Processando Daily Set Soberano...")
            await page.goto('https://rewards.bing.com/', wait_until="domcontentloaded")
            await asyncio.sleep(5)

            cards = page.locator("mee-card")
            count = await cards.count()
            
            for i in range(count):
                try:
                    card = cards.nth(i)
                    # Ignora cards concluídos ou sem links
                    if await card.locator(".mee-icon-CheckMark").count() > 0:
                        continue 
                    
                    link = card.locator("a").first
                    if await link.count() == 0: continue

                    title = await card.locator("h3").inner_text()
                    logger.info(f"➡️ Atividade: {title}")
                    
                    async with page.expect_popup() as popup_info:
                        await link.click()
                    
                    new_page = await popup_info.value
                    await new_page.wait_for_load_state("domcontentloaded")
                    
                    await self._process_activity_page(new_page)
                    await new_page.close()
                    
                    await asyncio.sleep(random.uniform(5, 8))
                    
                except Exception:
                    continue
                    
            logger.info("Daily Set finalizado.")
        except Exception as e:
            logger.error(f"Falha no Daily Set: {e}")

    async def _process_activity_page(self, page):
        """Interage com a página do desafio (Quiz/Enquete)."""
        await asyncio.sleep(8) 
        
        selectors = [
            ".btOption", "#btoption", ".rqOption", ".rq_option", 
            ".b_cards", ".options", ".it_voted"
        ]
        
        # Tenta responder até 15 questões (para Quizes longos)
        for _ in range(15): 
            found = False
            for sel in selectors:
                options = page.locator(sel)
                opt_count = await options.count()
                if opt_count > 0:
                    for i in range(opt_count):
                        opt = options.nth(i)
                        try:
                            if await opt.is_visible():
                                await opt.click(timeout=3000, force=True)
                                await asyncio.sleep(random.uniform(3, 5))
                                found = True
                                break
                        except: continue
                    if found: break
            if not found: break
                
        await asyncio.sleep(5)
