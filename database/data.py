import pandas as pd
#obtem o arquivo csv a partir de uma url
url = 'https://raw.githubusercontent.com/DaniloSovano/Sistema_de_Varejo/refs/heads/main/database/base_de_varejo.csv'

#lẽ o arquivo utilizando pandas
data = pd.read_csv(url)

#converte todas as virgulas por pontos
data = data.replace(',', '.', regex=True)

#transforma as colunas em valores numericos
data['VV'] = pd.to_numeric(data['VV'], errors='coerce')
data['VC'] = pd.to_numeric(data['VC'], errors='coerce')

#cria uma copia do dataframe para não afetar o original
data = data.copy()


