import os
import pandas as pd
import numpy as np

def limpar_dados_imoveis(caminho_raw):
    """Lê a base bruta de imóveis em Petrópolis, remove duplicatas, trata outliers por IQR e padroniza bairros"""
    df = pd.read_csv(caminho_raw)
    
    # 1. Remoção de duplicados
    df_clean = df.drop_duplicates(subset=['bairro', 'area_m2', 'preco_venda', 'quartos'])
    
    # 2. Criação da variável de valor por m2
    df_clean['preco_m2'] = df_clean['preco_venda'] / df_clean['area_m2']
    
    # 3. Filtro de Outliers via IQR
    Q1 = df_clean['preco_m2'].quantile(0.25)
    Q3 = df_clean['preco_m2'].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    df_filtrado = df_clean[(df_clean['preco_m2'] >= limite_inferior) & (df_clean['preco_m2'] <= limite_superior)]
    
    os.makedirs('data/processed', exist_ok=True)
    caminho_saida = 'data/processed/imoveis_petropolis_clean.csv'
    df_filtrado.to_csv(caminho_saida, index=False)
    print(f"Base higienizada salva em: {caminho_saida}")
    return df_filtrado

if __name__ == '__main__':
    limpar_dados_imoveis('data/raw/imoveis_petropolis_raw.csv')
