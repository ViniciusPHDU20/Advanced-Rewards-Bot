import asyncio
import sys
import os
from src.core.engine import RewardsEngine
from src.automation.searches import SearchAutomation
from src.automation.stats import StatsAutomation
from src.utils.logger import logger

def print_banner():
    """Exibe o banner soberano do projeto no terminal."""
    print("\033[95m")
    print(" █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ ")
    print("██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗")
    print("███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║")
    print("██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║")
    print("██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝")
    print("╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ")
    print("      REWARDS BOT - SOBERANO EDITION v1.6 | JESUS COMMAND")
    print("\033[0m")

async def interactive_menu():
    """Menu CLI interativo e completo."""
    config = {"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    engine = RewardsEngine(config)
    automation = SearchAutomation(engine)
    stats = StatsAutomation(engine)

    while True:
        os.system('clear')
        print_banner()
        print("\033[94m[1]\033[0m Farm Completo (Daily + Desktop + Mobile)")
        print("\033[94m[2]\033[0m Apenas Buscas DESKTOP")
        print("\033[94m[3]\033[0m Apenas Buscas MOBILE (Moto G52)")
        print("\033[94m[4]\033[0m Consultar Saldo e Gerar Gráfico")
        print("\033[94m[5]\033[0m Login Manual / Validar Sessão")
        print("\033[91m[0]\033[0m Sair do Sistema")
        print("\n" + "═"*60)
        
        choice = input("\033[95mSelecione a operação soberana: \033[0m")

        if choice == "1":
            await engine.initialize(headless=False)
            await automation.run_desktop_searches(35)
            await automation.run_mobile_searches(25)
            await stats.get_current_points()
            stats.generate_graph()
            await engine.save_session()
            input("\nFarm e Gráfico concluídos. Enter para voltar...")
        elif choice == "2":
            await engine.initialize(headless=False)
            await automation.run_desktop_searches(35)
            await engine.save_session()
            input("\nBuscas Desktop concluídas. Enter para voltar...")
        elif choice == "3":
            await engine.initialize(headless=False)
            await automation.run_mobile_searches(25)
            await engine.save_session()
            input("\nBuscas Mobile concluídas. Enter para voltar...")
        elif choice == "4":
            await engine.initialize(headless=True)
            pts = await stats.get_current_points()
            stats.generate_graph()
            print(f"\n\033[92mSUCESSO: Saldo atualizado para {pts} pts!\033[0m")
            input("\nPressione Enter para voltar...")
        elif choice == "5":
            print("\033[93mAbrindo navegador para login manual...\033[0m")
            await engine.initialize(headless=False)
            print("Após logar, feche a janela do navegador para salvar a sessão.")
            await asyncio.sleep(60) 
            await engine.save_session()
        elif choice == "0":
            break
        
        if engine.browser:
            await engine.shutdown()

if __name__ == "__main__":
    try:
        asyncio.run(interactive_menu())
    except KeyboardInterrupt:
        sys.exit(0)
