import csv
import time
from datetime import datetime

def get_current_points(page):
    """Apenas extrai os pontos da tela sem logar no CSV."""
    try:
        if "rewards.bing.com" not in page.url:
            page.goto('https://rewards.bing.com/', wait_until="domcontentloaded", timeout=60000)
        
        time.sleep(5) 

        points = page.evaluate("""() => {
            try {
                let counter = document.querySelector('mee-rewards-counter-animation span[aria-label]');
                if (counter) return counter.getAttribute('aria-label');
                let headerPoints = document.querySelector('#meControlSiginHeader');
                if (headerPoints) return headerPoints.innerText;
                let dailyPoints = document.querySelector('#mee-card-group-points');
                if (dailyPoints) return dailyPoints.innerText;
                return "0";
            } catch(e) { return "0"; }
        }""")

        points_cleaned = "".join(filter(str.isdigit, str(points)))
        return int(points_cleaned) if points_cleaned else 0
    except:
        return 0

def log_points(page, session_earned=None):
    """Extrai os pontos e salva no histórico CSV."""
    filename = "points_log.csv"
    today = datetime.now().strftime("%Y-%m-%d")
    current_total = get_current_points(page)
    
    try:
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            # Colunas: Data, Total, Ganhos na Sessão
            writer.writerow([today, current_total, session_earned if session_earned is not None else 0])
            
        print(f"📊 Saldo Total: {current_total} | Ganho hoje: {session_earned}")
        return current_total
    except Exception as e:
        print(f"❌ Falha ao logar pontos: {e}")
        return current_total
