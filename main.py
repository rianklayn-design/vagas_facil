import pandas as pd 

# 1. carrega a planilha para dentro de uma estrutura chamada dataframe (df)
#se o seu arquivo for .csv, mude para: pd.read_csv("dados.csv")

df = pd.read_csv("vagas_facil.csv")

#print(df)

print(df.info()) #mostra informaçoes sobre a dataframe, como numero de linhas,colunas e tipos de dados 

#print(df.head()) #mostra as primeiras linhas do dataframe 


#df.describe() # mostra estatisticas descritivas das colunas numericas do dataframe 

print(df.describe())  # mostra estatistica descritivas das colunas numericas do datframe 

print(df.drop_duplicates()) # remove linhas duplicadas do dataframe e exibe o resultado 