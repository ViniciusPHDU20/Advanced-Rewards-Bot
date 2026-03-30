import csv
import time
from datetime import datetime

def log_points(page):
    filename = "points_log.csv"
    today = datetime.now().strftime("%Y-%m-%d")
    
    try:
        # Garante que estamos na página certa
        if "rewards.bing.com" not in page.url:
            page.goto('https://rewards.bing.com/', wait_until="networkidle", timeout=60000)
        
        # A Microsoft usa animações para os pontos, precisamos esperar!
        time.sleep(8) 

        # 🚀 MÉTODO SOBERANO V2: Foco no componente de animação e aria-label
        points = page.evaluate("""() => {
            try {
                // 1. Tenta o span dentro do contador de animação (O mais preciso)
                let counter = document.querySelector('mee-rewards-counter-animation span[aria-label]');
                if (counter) return counter.getAttribute('aria-label');
                
                // 2. Tenta qualquer elemento com a classe de pontos do header
                let headerPoints = document.querySelector('#meControlSiginHeader');
                if (headerPoints) return headerPoints.innerText;

                // 3. Tenta o ID clássico
                let dailyPoints = document.querySelector('#mee-card-group-points');
                if (dailyPoints) return dailyPoints.innerText;

                return "0";
            } catch(e) {
                return "0";
            }
        }""")

        # Limpeza agressiva: Mantém apenas números
        points_cleaned = "".join(filter(str.isdigit, str(points)))

        # Se falhou ou deu 0, tenta um Regex final no texto visível da página
        if not points_cleaned or points_cleaned == "0":
            try:
                body_text = page.inner_text("body")
                import re
                # Procura o saldo total que geralmente aparece no topo
                match = re.search(r'(\d+[\.,]\d+|\d+)\s*(pontos|points|disponíveis|available)', body_text, re.IGNORECASE)
                if match:
                    points_cleaned = "".join(filter(str.isdigit, match.group(1)))
            except: pass

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([today, points_cleaned])
            
        print(f"📊 Saldo Total capturado: {points_cleaned}")
        return points_cleaned if points_cleaned else "0"
    except Exception as e:
        print(f"❌ Falha ao extrair saldo: {e}")
        return "Error"
