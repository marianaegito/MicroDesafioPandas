Análise de Gols do Brasil na Copa de 2022 

Este projeto realiza uma análise simples dos gols do Brasil nas partidas da Copa do Mundo de 2022 usando Python, pandas e matplotlib. Ele permite visualizar o desempenho do time, calcular médias e identificar partidas acima da média de gols.

Requisitos

Python 3.x

Bibliotecas Python:

pip install pandas matplotlib

Arquivo CSV brasil_copa2022.csv com pelo menos as colunas:

gols_brasil — número de gols marcados pelo Brasil em cada partida

adversario — nome do time adversário

Descrição do Script

O arquivo analise_copa.py realiza as seguintes operações:

1️⃣ Importação de bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

pandas: manipulação e análise de dados.

matplotlib.pyplot: criação de gráficos para visualização.

2️⃣ Carregar os dados do CSV
dados = pd.read_csv("brasil_copa2022.csv")
print(dados)

Lê o arquivo CSV e transforma em um DataFrame.

Exibe os dados carregados para conferência.

3️⃣ Calcular a média de gols do Brasil
media = dados["gols_brasil"].mean()
print("Média de gols:", media)

Calcula a média de gols por partida.

Essa informação será usada para análise e gráficos.

4️⃣ Gráfico de linha dos gols por partida
plt.plot(dados["gols_brasil"], marker='o')
plt.axhline(media, color='red', linestyle='--', label='Média')
plt.title("Gols do Brasil por partida")
plt.xlabel("Partida")
plt.ylabel("Gols")
plt.legend()
plt.show()

Gráfico de linha mostrando a evolução dos gols.

Linha vermelha indica a média de gols.

Ideal para observar partidas acima ou abaixo da média.

Exemplo de gráfico de linha:

5️⃣ Identificar partidas acima da média
acima_media = dados[dados["gols_brasil"] > media]
print("Partidas acima da média:", len(acima_media))

Filtra partidas onde o Brasil marcou mais que a média.

Exibe o número dessas partidas.

6️⃣ Gráfico de barras por adversário
plt.bar(dados["adversario"], dados["gols_brasil"], color='green')
plt.title("Gols do Brasil por adversário")
plt.xlabel("Adversário")
plt.ylabel("Gols")
plt.show()

Visualiza quantos gols o Brasil marcou contra cada adversário.

Facilita comparar partidas de forma rápida.

Exemplo de gráfico de barras:

Como Executar

No terminal, na pasta do projeto:

python analise_copa.py

O script irá:

Mostrar os dados do CSV.

Calcular e exibir a média de gols.

Gerar gráficos de linha e barras.

Informar quantas partidas ficaram acima da média de gols.

Objetivos do Projeto

Aprender a usar pandas e matplotlib para análise de dados.

Visualizar resultados de forma clara e intuitiva.

Criar gráficos simples e informativos para estudos de desempenho esportivo.
