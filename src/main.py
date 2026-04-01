import asyncio
import sys
from src.core.engine import RewardsEngine
from src.utils.logger import logger

async def main():
    """Ponto de entrada principal da engine de automação."""
    
    # Configuração simulada (Em produção, viria de um arquivo YAML/Config)
    config = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "mobile_mode": False
    }

    engine = RewardsEngine(config)

    # Exemplo de Hook (Bridge para uma futura GUI)
    def gui_bridge(event, data):
        """Função simuladora de recebimento de eventos pela interface gráfica."""
        # Se você estivesse usando uma GUI, aqui você atualizaria a tela.
        pass

    engine.add_hook(gui_bridge)

    try:
        await engine.initialize(headless=True)
        
        # Simulação de buscas reais (keywords poderiam vir de uma API)
        keywords = ["Tecnologia Soberana", "Arch Linux Performance", "Engenharia de Elite"]
        await engine.perform_search(keywords)
        
    except KeyboardInterrupt:
        logger.warning("Interrupção manual detectada pelo usuário.")
    except Exception as e:
        logger.error(f"Falha crítica na execução do bot: {str(e)}", exc_info=True)
    finally:
        await engine.shutdown()
        logger.info("Processo finalizado com integridade.")

if __name__ == "__main__":
    # Garantir que o loop de eventos asyncio seja fechado corretamente
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
