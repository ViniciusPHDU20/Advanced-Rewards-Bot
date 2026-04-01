import requests

def send_discord_notification(email, message):
    """Envia notificação se o Webhook estiver configurado."""
    webhook_url = "yourdiscordhookURLhere"
    
    # Se não configurado, ignora silenciosamente
    if "yourdiscordhookURL" in webhook_url:
        return
        
    try:
        data = {
            "username": "Rewards Engine Bot",
            "content": f"**[{email}]**\n{message}"
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("🔔 Notificação enviada ao Discord.")
    except Exception as e:
        # Silencia erros de rede ou configuração
        pass
