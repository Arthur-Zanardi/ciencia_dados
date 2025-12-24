import pandas as pd

import json



# um dataFrame nada mais é que uma tabela retangular.
# uma linha em dado id (primary key), é um sample qualquer.

# CSV
data_csv = pd.read_csv("./src/logs2024.csv",sep=';',encoding='latin1')

# JSON

# 1. Carrega o arquivo usando a biblioteca padrão do Python (mais segura)
with open("./src/2024logs.json", "r", encoding='utf-8') as f:
    dados_brutos = json.load(f)

data_json = pd.DataFrame(dados_brutos)
print(data_json.head())

# TXT


# DataBase toda partida
#print(data_frame_csv.head())
#   data_frame_csv.info()

print(data_csv.shape)
print(f"O data_frame_csv possui {data_csv.shape[0]} linhas/itens e {data_csv.shape[1]} colunas/atributos")
print(f"O data_frame_json possui {data_json.shape[0]} linhas/itens e {data_json.shape[1]} colunas/atributos")

