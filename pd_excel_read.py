import pandas as pd
from datetime import datetime

# Converter coluna aniversário p/ datetime
def converter_niver(dados_excel):
    try:
        dados_excel["Aniversário"] = pd.to_datetime(dados_excel["Aniversário"], format="%d/%m/%Y")
        print("Coluna 'Aniversário' convertida com sucesso.")
    except Exception as e:
        print(f"Erro ao converter a coluna 'Aniversário': {e}")

# Filtrar aniversariantes na data atual
def filtrar_niver(dados_excel, data_atual):
    try:
        # Filtro mes e dia
        dados_filtrados = dados_excel[(dados_excel["Aniversário"].dt.month == data_atual.month) & 
                                      (dados_excel["Aniversário"].dt.day == data_atual.day)]
        return dados_filtrados
    except Exception as e:
        print(f"Erro ao filtrar por aniversariantes: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

# Main
def main():
    try:
        dados_excel = pd.read_excel("planilha.xlsx")
        if dados_excel.empty:
            print("Planilha está vazia ou não foi carregada corretamente.")
            return
    except Exception as e:
        print(f"Erro ao carregar a planilha: {e}")
        return
    
    converter_niver(dados_excel)
    
    data_atual = datetime.now()
    aniversariantes = filtrar_niver(dados_excel, data_atual)
    
    # Mensagem caso nao haja aniversariantes
    if not aniversariantes.empty:
        print("Aniversariantes do dia: \n", aniversariantes)
        # logica pra enviar email (incluir depois) 
    else:
        print("Nenhum aniversariante hoje!") 

if __name__ == "__main__":
    main()
