# 🤖 Advanced Rewards Automation Engine (Pro Edition) 🚀

Advanced and stealthy automation for Microsoft Rewards, specifically optimized for **Arch Linux** and Linux-based environments. This project leverages the **Playwright** engine to emulate high-level human behavior, ensuring daily point collection without manual intervention and with advanced bot detection bypass.

## ✨ Core Features
- **⚡ Playwright Stealth Engine:** Real navigation emulation, bypassing `navigator.webdriver` checks.
- **🖥️ Dual Mode (Desktop + Mobile):** Complete daily point collection across both platforms.
- **📱 Device Emulation:** Calibrated User-Agents and viewports for seamless mobile simulation.
- **🛡️ Session Management:** Efficient session handling to minimize IP-based blocks or excessive logins.
- **📊 Points Analytics:** Automated evolution tracking and balance reporting (`graph_points.py`).
- **🔔 Notification Integration:** Real-time alerts via Discord regarding farm status and session earnings.

## 🛠️ Requirements
- **OS:** Linux (Arch Linux recommended)
- **Browser:** Microsoft Edge or Chromium-based
- **Python:** 3.11+
- **Playwright:** Configured with Chromium drivers

## 🚀 Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ViniciusPHDU20/rewards_farm.git
   cd rewards_farm
   ```

2. **Prepare the Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Configure Credentials:**
   - Rename `config/accounts.example.json` to `config/accounts.json`.
   - Fill in your email (password is optional if the profile is already logged in).

4. **Run the Engine:**
   ```bash
   ./run_farm.sh
   ```

## 🛡️ Security and Anti-Fingerprinting
The script implements randomized delays between searches (`search_delay`), dynamic task ordering, and selective cache clearing to maintain account security.

---
*Developed by **ViniciusPHDU20** | Professional Automation Solutions*
