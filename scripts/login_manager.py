import time

def login(page, email, password):
    try:
        print(f"🌐 Verificando sessão para: {email}...")
        page.goto('https://rewards.bing.com/', wait_until="domcontentloaded", timeout=60000)
        time.sleep(5)

        # Se já estivermos no dashboard, sucesso imediato
        if "login.live.com" not in page.url:
            print(f"✅ Sessão ativa detectada!")
            return True

        print("⌨️ Sessão expirada. Inserindo e-mail para aprovação...")
        # Seletor robusto para o campo de login
        email_input = page.locator('input[type="email"], input[name="loginfmt"]').first
        email_input.wait_for(state="visible", timeout=30000)
        email_input.fill(email)
        
        page.locator('input[type="submit"], #idSIButton9').click()
        
        print(f"🔔 [AÇÃO REQUERIDA] Aprove o login para {email} no celular!")
        print("⏳ O bot vai aguardar 90 segundos...")
        
        # Espera o redirecionamento pós-aprovação
        try:
            page.wait_for_url("**/rewards.bing.com/**", timeout=90000)
            print("✅ Login aprovado manualmente!")
            return True
        except:
            if "rewards.bing.com" in page.url:
                return True
            print("❌ Tempo esgotado para aprovação.")
            return False

    except Exception as e:
        print(f"❌ Erro no Login: {e}")
        return False
