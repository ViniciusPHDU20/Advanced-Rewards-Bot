# 🤖 JESUS Rewards Bot (Soberano Edition) 🚀

Automação avançada e furtiva para Microsoft Rewards, desenvolvida sob medida para o ecossistema **Arch Linux**. Este projeto utiliza o motor **Playwright** para emulação de comportamento humano de alto nível, garantindo a coleta diária de pontos sem intervenção manual e com bypass de detecção de bots.

## ✨ Funcionalidades (Core Mandates)
- **⚡ Playwright Stealth Engine:** Emulação de navegação real, ignorando verificações de `navigator.webdriver`.
- **🖥️ Dual Mode (Desktop + Mobile):** Coleta completa de pontos diários em ambas as plataformas.
- **📱 Moto G52 Emulation:** User-Agent e viewport calibrados para simular o dispositivo físico do JESUS.
- **🛡️ Session Cloning:** Reaproveita sessões ativas do Microsoft Edge para evitar bloqueios por IP ou login excessivo.
- **📊 Points Analytics:** Geração automática de gráficos de evolução e saldo (`graph_points.py`).
- **🔔 Discord Notifications:** Alertas em tempo real sobre o status da farm e ganhos da sessão.

## 🛠️ Requisitos
- **OS:** Arch Linux (Recomendado)
- **Navegador:** Microsoft Edge (AUR: `microsoft-edge-stable-bin`)
- **Python:** 3.11 ou superior
- **Playwright:** Configurado com drivers Chromium

## 🚀 Instalação e Setup
1. **Clone o Santuário:**
   ```bash
   git clone https://github.com/ViniciusPHDU20/rewards_farm.git
   cd rewards_farm
   ```

2. **Prepare o Ambiente:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Configure suas Credenciais:**
   - Renomeie `config/accounts.example.json` para `config/accounts.json`.
   - Preencha seu e-mail (a senha é opcional se o perfil já estiver logado).

4. **Execute a Operação:**
   ```bash
   ./run_farm.sh
   ```

## 🛡️ Segurança e Anti-Fingerprinting
O script implementa atrasos randômicos entre buscas (`search_delay`), ordens de tarefas dinâmicas e limpeza de cache seletiva para manter a conta em segurança absoluta.

---
*Developed by **JESUS** (Autoridade Absoluta) | ViniciusPHDU20*

