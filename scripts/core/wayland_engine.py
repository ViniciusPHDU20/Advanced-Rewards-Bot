import subprocess
import time
import random
import json
from urllib.parse import quote

class WaylandEngine:
    @staticmethod
    def get_edge_address():
        try:
            clients = subprocess.check_output(["hyprctl", "clients", "-j"]).decode("utf-8")
            data = json.loads(clients)
            for client in data:
                if "edge" in client["initialClass"].lower() or "microsoft-edge" in client["initialClass"].lower():
                    return client["address"]
        except: return None
        return None

    @staticmethod
    def focus_window(address):
        subprocess.run(["hyprctl", "dispatch", "focuswindow", f"address:{address}"])
        time.sleep(1.5)

    @staticmethod
    def type_query(query, mobile=False):
        # Parâmetros oficiais de bypass
        reward_param = "ML102W" if not mobile else "ML102V"
        search_url = f"https://www.bing.com/search?q={quote(query)}&form={reward_param}&OCID={reward_param}&PUBL=REWARDS_DASHBOARD"
        
        # Foca na barra de endereço (Ctrl+L)
        subprocess.run(["wtype", "-M", "ctrl", "l", "-m", "ctrl"])
        time.sleep(0.8)
        subprocess.run(["wtype", "-k", "BackSpace"])
        
        # Digita a URL parametrizada
        subprocess.run(["wtype", search_url])
        time.sleep(0.5)
        subprocess.run(["wtype", "-k", "Return"])

    @staticmethod
    def human_interaction():
        # Simula leitura com Scroll e pequenas pausas
        time.sleep(random.uniform(15, 25))
        for _ in range(random.randint(3, 6)):
            subprocess.run(["wtype", "-k", "Page_Down"])
            time.sleep(random.uniform(2, 5))
        for _ in range(2):
            subprocess.run(["wtype", "-k", "Page_Up"])
            time.sleep(1)
