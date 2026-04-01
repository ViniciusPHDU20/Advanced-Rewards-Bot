import random

# Lista massiva de tópicos reais para evitar repetição
TOPICS = [
    "melhores filmes de ficção científica 2026", "como cultivar manjericão em apartamento",
    "previsão do tempo para o fim de semana", "receita de strogonoff de frango simples",
    "resultado do jogo de ontem", "últimas notícias sobre inteligência artificial",
    "vagas de emprego home office tecnologia", "lançamentos de jogos ps5 2026",
    "como configurar hyprland no arch linux", "melhores extensões vscode para python",
    "história da revolução industrial resumo", "distância da terra até marte",
    "o que é computação quântica", "melhores praias do brasil para viajar em maio",
    "como economizar bateria no android 16", "notícias sobre o mercado financeiro hoje",
    "quem ganhou o oscar de melhor filme", "dicas de segurança digital para celular",
    "como fazer backup do whatsapp no pc", "evolução do kernel linux nos últimos anos",
    "melhores teclados mecânicos custo benefício", "como aprender inglês sozinho de graça",
    "curiosidades sobre o antigo egito", "quanto custa um tesla no brasil",
    "principais tendências de moda inverno 2026", "como funciona um motor elétrico",
    "melhores séries da netflix para maratonar", "exercícios para fazer em casa iniciante",
    "significado dos sonhos com viagem", "como instalar docker no linux pass a passo"
]

TEMPLATES = [
    "{}", "notícias sobre {}", "como fazer {}", "melhores {}", 
    "guia completo de {}", "preço de {} hoje", "história de {}"
]

def generate_smart_query(base_topic=None):
    # Escolhe um tópico aleatório da lista massiva
    topic = random.choice(TOPICS)
    # Às vezes adiciona um template para variar
    if random.random() > 0.5:
        return random.choice(TEMPLATES).format(topic)
    return topic
