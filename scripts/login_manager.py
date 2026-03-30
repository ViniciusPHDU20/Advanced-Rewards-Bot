import time

def login(page, email, password):
    try:
        print(f"🌐 Verificando sessão para: {email}...")
        page.goto('https://rewards.bing.com/', wait_until="networkidle")

        # Se a URL contém 'dashboard' ou não estamos na tela de login, estamos logados!
        if "login.live.com" not in page.url:
            print(f"✅ Sessão ativa detectada via Perfil Clonado!")
            return True

        print("⌨️ Sessão expirada. Tentando re-login automático...")
        page.fill('input[name="loginfmt"]', email)
        page.click('input[type="submit"]')
        
        # Como o JESUS está dormindo, se pedir aprovação agora vai falhar.
        # Mas o perfil clonado deve evitar isso 99% das vezes.
        print("⚠️ [AUTÔNOMO] Aguardando 30s por possível auto-redirecionamento...")
        time.sleep(30)
        
        if "rewards.bing.com" in page.url:
            return True
            
        print("❌ Login falhou no modo autônomo (Requer aprovação manual).")
        return False

    except Exception as e:
        print(f"❌ Erro no Login Autônomo: {e}")
        return False
