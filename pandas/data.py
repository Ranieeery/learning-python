import pandas as pd

# Series: São arrays unidimensionais que podem ser rotulados, ou seja, podemos dar um nome para cada posição do array.
s = pd.Series(["Fusca", "Gol", "Palio", "Uno", "Celta"], name="Carros")
print(s)

# Dataframe: São estruturas bidimensionais de dados, semelhantes a uma planilha.
df = pd.DataFrame({"Nome": ["Fusca", "Gol", "Palio", "Uno", "Celta"],
                   "Marca": ["Volkswagen", "Volkswagen", "Fiat", "Fiat", "Chevrolet"],
                   "Ano": [1980, 2012, 2014, 2010, 2015],
                   "Quilometragem": [150000, 40000, 30000, 50000, 35000]
                   })
print(df)

# Criando um dataframe a partir de um arquivo CSV
# df = pd.read_csv("./db.csv", sep=";")

