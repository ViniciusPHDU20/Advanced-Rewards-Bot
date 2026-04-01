import time
import random
from datetime import datetime

class RewardSession:
    def __init__(self, page, email):
        self.page = page
        self.email = email
        self.start_points = 0
        self.end_points = 0
        self.session_start_time = datetime.now()
        self.activities_log = []

    def get_points(self, retry=3):
        """Captura os pontos reais com verificação de carregamento."""
        for attempt in range(retry):
            try:
                # Garante que estamos na dashboard
                if "rewards.bing.com" not in self.page.url:
                    self.page.goto('https://rewards.bing.com/', wait_until="domcontentloaded", timeout=60000)
                
                # Espera o contador animar e estabilizar
                self.page.wait_for_selector('mee-rewards-counter-animation span[aria-label]', timeout=15000)
                time.sleep(3) 

                points_text = self.page.evaluate("""() => {
                    const counter = document.querySelector('mee-rewards-counter-animation span[aria-label]');
                    return counter ? counter.getAttribute('aria-label') : "0";
                }""")

                # Extrai apenas números (ex: "5.430 pontos" -> 5430)
                points_cleaned = "".join(filter(str.isdigit, str(points_text)))
                if points_cleaned and int(points_cleaned) > 0:
                    return int(points_cleaned)
                
                time.sleep(2) # Pequeno delay antes da próxima tentativa
            except Exception as e:
                print(f"⚠️ Tentativa {attempt+1} de ler pontos falhou: {e}")
                time.sleep(2)
        
        return 0

    def start_session(self):
        self.start_points = self.get_points()
        print(f"💰 Saldo Inicial ({self.email}): {self.start_points} pts")

    def end_session(self):
        self.end_points = self.get_points()
        earned = self.end_points - self.start_points
        print(f"🏁 Saldo Final: {self.end_points} pts | Ganho na sessão: +{earned} pts")
        return earned

    def log_activity(self, name, status, points=0):
        self.activities_log.append({
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "activity": name,
            "status": status,
            "points_earned": points
        })
