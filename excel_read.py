#pandas 
#openpyxl

import pandas as pd
from datetime import datetime

#Definir caminho excel
dados_excel = pd.read_excel("planilha.xlsx")

# Conversão da coluna Aniversário para o tipo datetime
dados_excel["Aniversário"] = pd.to_datetime(dados_excel["Aniversário"], format="%d/%m/%Y")

# Obter a data atual
data_atual = datetime.now()

# Comparar com hj
dados_filtrados = dados_excel["Aniversário"].dt.month == data_atual.month
dados_filtrados = dados_excel["Aniversário"].dt.day == data_atual.day

#dados_filtrados = dados_excel["Aniversário"] == "21/09/2004"
print ("Dados Filtrados:\n", dados_excel[dados_filtrados])

#dados_excel.to_csv("saída.txt", index=False, header=True, sep="|")
#print (dados_excel)
