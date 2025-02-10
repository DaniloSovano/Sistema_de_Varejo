import pandas as pd

url = 'https://raw.githubusercontent.com/DaniloSovano/Sistema_de_Varejo/refs/heads/main/base_de_varejo.csv'
data = pd.read_csv(url)

data = data.replace(',', '.', regex=True)

data['VV'] = pd.to_numeric(data['VV'], errors='coerce')
data['VC'] = pd.to_numeric(data['VC'], errors='coerce')

data = data.copy()