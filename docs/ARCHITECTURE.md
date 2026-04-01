# Documentação Técnica e Arquitetura de Software

## 🏗️ Visão Geral da Arquitetura

O **Advanced-Rewards-Bot** foi desenvolvido seguindo os princípios de modularidade e separação de preocupações (Separation of Concerns). O sistema é dividido em camadas distintas para garantir que a lógica de automação permaneça independente de qualquer interface de usuário (GUI).

### 📂 Estrutura de Diretórios

- **`src/core/`**: Contém o "Cérebro" do sistema. É onde reside a lógica de baixo nível do Playwright e o controle de fluxo de automação.
- **`src/utils/`**: Utilitários transversais, como o sistema de logging e gerenciadores de configuração.
- **`src/api/`**: Camada de abstração para comunicação externa (preparada para integração com GUIs em Rust/Go/C++).
- **`src/automation/`**: Scripts específicos de comportamento (Daily Sets, Searche Types).

---

## ⚙️ Detalhamento dos Componentes

### 1. Motor de Automação (`core/engine.py`)
A classe `RewardsEngine` é o componente central. Ela gerencia o ciclo de vida do navegador Chromium.
- **`initialize()`**: Configura o contexto do navegador, injeta o User-Agent (ex: Moto G52 para mobile) e define as dimensões do viewport.
- **`perform_search()`**: Implementa um algoritmo de busca sequencial com **delays randômicos** (jitter) entre 2.5s e 5.0s, simulando o tempo de leitura humano e evitando padrões mecânicos detectáveis pela telemetria da Microsoft.
- **`shutdown()`**: Garante o fechamento limpo das instâncias do navegador para evitar vazamento de memória (Memory Leaks).

### 2. Sistema de Hooks (Event Bridge)
O bot utiliza o **Observer Pattern**. Através do método `add_hook()`, qualquer componente externo (como uma futura GUI) pode se registrar para ouvir eventos em tempo real:
- `ENGINE_READY`: Motor pronto para operação.
- `SEARCH_START`: Uma nova busca foi iniciada (envia o termo atual).
- `SEARCH_SUCCESS`: A busca foi validada com sucesso.
- `SEARCH_ERROR`: Ocorreu uma falha (envia o erro detalhado).

**Exemplo de Extensão:** Para adicionar uma GUI, basta criar uma função de callback e passá-la para `engine.add_hook(minha_funcao_gui)`.

### 3. Logger Enterprise (`utils/logger.py`)
Implementado via **Singleton Pattern**, garantindo que todas as partes do sistema escrevam no mesmo arquivo de auditoria (`logs/audit.log`).
- Utiliza **RotatingFileHandler**: O log nunca excederá 5MB, rotacionando automaticamente para economizar espaço em disco.
- Suporta níveis de severidade: `DEBUG` (detalhes técnicos), `INFO` (progresso), `WARNING` (alertas) e `ERROR` (falhas críticas).

---

## 🛡️ Lógica de Evasão e Segurança

Para atingir o **Bypass Nível 2**, o bot opera sob as seguintes premissas:
1. **User-Agent Spoofing:** Injeção de strings de identificação de hardware real.
2. **Context Isolation:** Cada execução utiliza um perfil de navegação limpo ou persistente, evitando rastros de sessões anteriores.
3. **Ghost Engine (Work in Progress):** Preparado para usar `wtype` (Wayland Input) para enviar comandos de teclado direto para o compositor do sistema, ignorando o DOM do navegador (indetectável por scripts de proteção de página).

---

## 🚀 Como Expandir o Código

1. **Adicionar Novos Tipos de Busca:** Crie um novo método em `engine.py` ou um novo arquivo em `automation/` e chame-o através do `main.py`.
2. **Implementar GUI:** O `src/api/` está reservado para classes de bridge. Se for usar **Rust**, utilize os hooks para atualizar o estado da sua aplicação via barramento de eventos.
3. **Novas Plataformas:** O viewport e o User-Agent podem ser movidos para um arquivo `config/devices.yaml` para fácil troca entre diferentes modelos de smartphone.

---
*Documento de Referência Técnica - Advanced-Rewards-Bot*
