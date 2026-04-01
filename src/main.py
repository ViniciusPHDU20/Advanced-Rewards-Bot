import asyncio
import os
import sys
import random
from src.core.engine import RewardsEngine
from src.automation.searches import SearchAutomation
from src.automation.stats import StatsAutomation
from src.utils.logger import logger

def clear_screen():
    os.system('clear')

def print_banner():
    # Cores Soberanas
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    
    print(f"{PURPLE}")
    print(" █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ ")
    print("██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗")
    print("███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║")
    print("██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║")
    print("██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝")
    print("╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ")
    print(f"      {CYAN}ENGINE DE AUTOMAÇÃO DE ELITE | V4.0 SOBERANA | JESUS COMMAND{RESET}")
    print(f"      {GREEN}Status: Sistema Operacional e Blindado{RESET}")
    print("═"*70)

async def interactive_menu():
    engine = RewardsEngine({})
    automation = SearchAutomation(engine)
    stats = StatsAutomation(engine)

    while True:
        clear_screen()
        print_banner()
        print(f"\033[94m[1]\033[0m Iniciar Farm Completo {PURPLE}(Desktop + Mobile + Daily){RESET}")
        print(f"\033[94m[2]\033[0m Consultar Saldo e Evolução {PURPLE}(Gráfico){RESET}")
        print(f"\033[94m[3]\033[0m Login Manual / Validar Conta {PURPLE}(Navegador Aberto){RESET}")
        print(f"\033[94m[4]\033[0m Apenas Buscas Desktop")
        print(f"\033[94m[5]\033[0m Apenas Buscas Mobile")
        print(f"\033[91m[0]\033[0m Sair do Sistema")
        print("\n" + "═"*70)
        
        choice = input(f"\033[95mJESUS, selecione o comando: \033[0m")

        try:
            if choice == "1":
                await engine.initialize(headless=False)
                await automation.run_desktop_searches(35)
                await automation.run_mobile_searches(25)
                pts = await stats.get_current_points()
                stats.generate_graph()
                input(f"\n\033[92m[OK] Farm concluído: {pts} pts. ENTER para voltar...\033[0m")
            
            elif choice == "2":
                await engine.initialize(headless=True)
                pts = await stats.get_current_points()
                stats.generate_graph()
                print(f"\n\033[92mSaldo Sincronizado: {pts} pts\033[0m")
                input("\nENTER para voltar...")
            
            elif choice == "3":
                logger.info("Abrindo portal de autenticação...")
                await engine.initialize(headless=False)
                print("\n\033[93m[!] Logue na conta e quando terminar, feche o navegador.\033[0m")
                input("\n\033[92mPressione ENTER aqui após fechar o navegador para salvar.\033[0m")
                await engine.save_session()
            
            elif choice == "4":
                await engine.initialize(headless=False)
                await automation.run_desktop_searches(35)
                input("\nENTER para voltar...")

            elif choice == "5":
                await engine.initialize(headless=False)
                await automation.run_mobile_searches(25)
                input("\nENTER para voltar...")
            
            elif choice == "0":
                break
        
        except Exception as e:
            logger.error(f"Erro no motor: {e}")
            input("\nPressione ENTER para restaurar...")
        
        finally:
            if engine.playwright:
                await engine.shutdown()

if __name__ == "__main__":
    PURPLE = "\033[95m"
    RESET = "\033[0m"
    try:
        asyncio.run(interactive_menu())
    except KeyboardInterrupt:
        sys.exit(0)
