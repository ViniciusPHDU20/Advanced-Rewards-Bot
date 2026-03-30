import os
import sys

def main_menu():
    os.system('clear')
    print("==========================================")
    print("   🚀 JESUS REWARDS BOT - CONTROL PANEL")
    print("==========================================")
    print("1) Iniciar Farming Completo (Desktop + Mobile)")
    print("2) Visualizar Log de Pontos")
    print("3) Verificar Status da Conta (Login)")
    print("4) Atualizar Playwright / Drivers")
    print("5) Sair")
    print("==========================================")
    
    choice = input("👉 Escolha uma opção: ")
    
    if choice == "1":
        os.system("./run_farm.sh")
    elif choice == "2":
        os.system("tail -n 20 points_log.csv")
        input("\nPressione Enter para voltar...")
        main_menu()
    elif choice == "3":
        os.system("source venv/bin/activate && python -c 'from playwright.sync_api import sync_playwright; from scripts.browser_manager import create_browser; from scripts.login_manager import login; p=sync_playwright().start(); c,pg=create_browser(p); login(pg,\"viniciusphdu@gmail.com\",\"pw\"); p.stop()'")
    elif choice == "5":
        sys.exit()
    else:
        main_menu()

if __name__ == "__main__":
    main_menu()
