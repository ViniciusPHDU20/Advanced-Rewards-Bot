# JESUS Rewards Bot 🚀

Automação avançada e furtiva para Microsoft Rewards no Arch Linux. Este projeto utiliza Playwright para emular comportamentos humanos e realizar buscas automáticas (Desktop + Mobile) sem a necessidade de intervenção manual ou aprovação de login (via clonagem de sessão ativa).

## 🛠️ Tecnologias
- **Python 3.11+**
- **Playwright** (Motor de automação nativo)
- **Falsificação de User-Agent** (PC + Moto G52)
- **Bypass de Sessão** (Clonagem de Perfil do Edge)

## 🚀 Como Usar
1. Logue na sua conta Microsoft no Edge oficial.
2. Clone este repositório.
3. Configure o e-mail em `config/accounts.json` (A senha não é necessária se a sessão estiver ativa).
4. Rode o lançador:
   ```bash
   ./run_farm.sh
   ```

## 🛡️ Segurança
O script possui mecanismos de **Anti-Fingerprinting** para evitar detecções e utiliza atrasos variáveis entre cada busca para simular navegação real.

---
*Developed by ViniciusPHDU20*
