import pandas as pd
import matplotlib.pyplot as plt

# carregar o csv
dados = pd.read_csv("brasil_copa2022.csv")

print("Dados carregados:")
print(dados)

# calcular média
media = dados["gols_brasil"].mean()

print("Média de gols:", media)

# gráfico de linha
plt.plot(dados["gols_brasil"], marker='o')
plt.axhline(media)
plt.title("Gols do Brasil por partida")
plt.xlabel("Partida")
plt.ylabel("Gols")
plt.show()

# partidas acima da média
acima_media = dados[dados["gols_brasil"] > media]

print("Partidas acima da média:", len(acima_media))

# gráfico de barras
plt.bar(dados["adversario"], dados["gols_brasil"])
plt.title("Gols do Brasil por adversário")
plt.xlabel("Adversário")
plt.ylabel("Gols")
plt.show()