import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_points_history():
    filename = "points_log.csv"
    if not os.path.exists(filename):
        print("⚠️  Log de pontos não encontrado. Rode o bot primeiro.")
        return

    try:
        # Lê o CSV considerando a nova estrutura: Data, Total, Ganhos
        df = pd.read_csv(filename, header=None, names=["Date", "TotalPoints", "SessionEarned"])
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date")

        # Configura o gráfico para salvar em arquivo (Headless)
        plt.figure(figsize=(12, 6))
        
        # Gráfico do Saldo Total
        plt.subplot(1, 2, 1)
        plt.plot(df["Date"], df["TotalPoints"], marker="o", color="blue", label="Saldo Total")
        plt.title("Evolução do Saldo Total")
        plt.xlabel("Data")
        plt.ylabel("Pontos")
        plt.grid(True)
        plt.xticks(rotation=45)

        # Gráfico dos Ganhos por Sessão
        plt.subplot(1, 2, 2)
        plt.bar(df["Date"], df["SessionEarned"], color="green", label="Ganhos")
        plt.title("Ganhos por Sessão")
        plt.xlabel("Data")
        plt.ylabel("Pontos Ganhos")
        plt.grid(True)
        plt.xticks(rotation=45)

        plt.tight_layout()
        
        output_file = "points_history_graph.png"
        plt.savefig(output_file)
        print(f"📊 Gráfico gerado com sucesso: {output_file}")

    except Exception as e:
        print(f"❌ Erro ao gerar gráfico: {e}")

if __name__ == "__main__":
    plot_points_history()
