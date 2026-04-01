import asyncio
import csv
import os
from datetime import datetime
from playwright.async_api import Page
from src.utils.logger import logger

class StatsAutomation:
    """Módulo especializado em extração de saldo e métricas de farm."""
    
    def __init__(self, engine):
        self.engine = engine
        self.log_file = "/home/viniciusphdu/WORKSPACE_CORE/Advanced-Rewards-Bot/config/points_log.csv"

    async def get_current_points(self) -> int:
        """Extrai o saldo atual de pontos do Microsoft Rewards."""
        logger.info("Iniciando consulta de saldo soberano...")
        
        if not self.engine.context:
            await self.engine.initialize(headless=True)
            
        page: Page = await self.engine.context.new_page()
        try:
            await page.goto("https://rewards.bing.com/", wait_until="networkidle")
            
            # Localizar o elemento de pontos (seletor clássico do Rewards)
            points_text = await page.inner_text("mee-rewards-counter-status-card >> .pointsValue")
            points = int(points_text.replace(".", "").replace(",", ""))
            
            logger.info(f"Saldo atual detectado: {points} pts")
            self._save_to_log(points)
            return points
            
        except Exception as e:
            logger.error(f"Erro ao consultar saldo: {str(e)}")
            return 0
        finally:
            await page.close()

    def _save_to_log(self, points: int):
        """Salva o saldo no histórico CSV para geração de gráficos."""
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        file_exists = os.path.isfile(self.log_file)
        
        with open(self.log_file, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Data", "Pontos"])
            writer.writerow([date_str, points])
        logger.debug("Histórico de pontos atualizado no CSV.")

    def generate_graph(self):
        """Dispara o gerador de gráficos externo."""
        logger.info("Gerando gráfico de evolução de pontos...")
        graph_script = "/home/viniciusphdu/WORKSPACE_CORE/Advanced-Rewards-Bot/graph_points.py"
        if os.path.exists(graph_script):
            os.system(f"python {graph_script}")
            logger.info("Gráfico atualizado: points_history_graph.png")
        else:
            logger.warning("Script de gráfico não encontrado.")
