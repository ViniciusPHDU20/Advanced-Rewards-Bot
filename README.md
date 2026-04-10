# ⚡ Advanced-Rewards-Bot: Autonomous Multi-Account Farming Suite

**Advanced-Rewards-Bot** is a high-performance, resilient automation suite designed for multi-account management and farming. It utilizes a **Ghost Engine** architecture to emulate human-like behavior, effectively bypassing modern anti-bot detections while maintaining 24/7 operational stability.

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-yellow.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Engine-Playwright-brightgreen.svg)](https://playwright.dev/)

## 🚀 Strategic Features

- **Ghost Engine Architecture**: Specialized spoofing of browser fingerprints, hardware identifiers, and mobile device headers (e.g., Moto G52 emulation).
- **Autonomous Decision Making**: Intelligent navigation patterns and randomized delays to simulate natural user interaction.
- **Multi-Account Proxy Support**: Seamless rotation of credentials and proxies to ensure account isolation and security.
- **Real-Time Visual Analytics**: Integrated telemetry dashboard (`control_panel.py`) and point tracking graphs (`graph_points.py`).
- **Forensic Verification**: Automated spoofing verification (`verify_app_spoof.py`) to ensure the environment remains undetectable.

## 🧰 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Core Automation** | Playwright (Python) |
| **Telemetry & UI** | Flask / Matplotlib |
| **Data Management** | JSON / CSV / SQLite |
| **Spoofing Engine** | Custom User-Agent & Header Injectors |

## 🛠 Deployment & Usage

### Prerequisites

- Python 3.10+
- Playwright browsers installed:
  ```bash
  playwright install chromium
  ```

### Quick Start

1. Clone the suite:
   ```bash
   git clone https://github.com/ViniciusPHDU20/Advanced-Rewards-Bot.git
   cd Advanced-Rewards-Bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute the farm:
   ```bash
   ./run_farm.sh
   ```

## 📊 Monitoring

The bot generates real-time logs and visual reports:
- **`farm_progress.log`**: Detailed operational history.
- **`points_history_graph.png`**: Visual representation of farming efficiency.
- **`control_panel.py`**: Start this for a centralized management interface.

## 🛡️ Ethics & Disclaimer

This tool is developed for educational and research purposes only. The authors are not responsible for any account bans or misuse of the software. Use responsibly and within the terms of service of the target platforms.

---
*Developed by **ViniciusPHDU20***
