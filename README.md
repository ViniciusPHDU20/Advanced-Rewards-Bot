# Advanced Rewards Bot (Soberano Edition)

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/ViniciusPHDU20/Advanced-Rewards-Bot/graphs/commit-activity)

## 📌 Visão Geral

O **Advanced Rewards Bot** é uma engine de automação de alto desempenho projetada para a plataforma Microsoft Rewards. Construída com foco em **fator de evasão de detecção (EDF)** e **estabilidade de execução**, a ferramenta utiliza uma arquitetura híbrida de **Playwright** para orquestração de sessões e **Ghost Engine** para emulação nativa de entrada de hardware (HID) no Linux/Wayland.

O projeto foi arquitetado sob princípios **SOLID**, permitindo a integração de interfaces gráficas customizadas e a expansão de módulos de busca sem a necessidade de alteração no núcleo do sistema.

## 🚀 Principais Funcionalidades

- **Multi-Plataforma (Emulação):** Suporte nativo para emulação de dispositivos mobile (ex: Moto G52) com injeção de User-Agent e viewport dinâmico.
- **Ghost Engine (Bypass Nível 2):** Utiliza `wtype` e `hyprctl` para simular entradas de teclado e mouse reais no Hyprland, evitando detecções sintéticas do WebRTC.
- **Arquitetura Baseada em Hooks:** Pronto para integração com GUIs (Qt, Rust/Iced, Go/Fyne) via barramento de eventos.
- **Gerenciamento de Sessão Persistente:** Clonagem e restauração automática de perfis de navegação para evitar re-logins constantes.
- **Sistema de Log Enterprise:** Logs rotativos e estruturados em JSON para auditoria técnica.

## 🏗️ Arquitetura do Sistema

```bash
Advanced-Rewards-Bot/
├── src/
│   ├── api/            # Interfaces e barramento de eventos para GUI
│   ├── automation/     # Lógica específica de busca e farm
│   ├── core/           # Motor principal (Playwright Engine)
│   ├── utils/          # Helpers, Loggers e Config-Manager
│   └── main.py         # Ponto de entrada (Entrypoint)
├── config/             # Arquivos de configuração (YAML/ENV)
├── docs/               # Documentação técnica estendida
└── tests/              # Suíte de testes unitários e integração
```

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.10+
- Playwright (`pip install playwright`)
- Wtype (para Linux/Wayland)

### Configuração
1. Clone o repositório:
   ```bash
   git clone https://github.com/ViniciusPHDU20/Advanced-Rewards-Bot.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```
3. Configure as credenciais no diretório `config/settings.yaml`.

## 📈 Roadmap de Desenvolvimento

- [x] Motor de Automação Core (v1.0)
- [x] Integração Ghost Engine (Bypass)
- [ ] Implementação de GUI Nativa (Em progresso)
- [ ] Suporte a Multi-Contas Sincronizadas

## 🤝 Contribuição

Contribuições são bem-vindas! Para garantir a qualidade do código, siga as diretrizes em `CONTRIBUTING.md`.

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---
*Desenvolvido com foco em soberania tecnológica e automação de elite.*
