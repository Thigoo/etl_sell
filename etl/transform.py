import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df['Quantidade Vendida'] = pd.to_numeric(df['Quantidade Vendida'], errors='coerce')
    df['Valor Unitário'] = pd.to_numeric(df['Valor Unitário'])

    df['Total da Venda'] = df['Quantidade Vendida'] * df['Valor Unitário']

    # delete rows with missing in data keys columns
    df = df.dropna(subset=['Data da Venda', 'Produto', 'Quantidade Vendida', 'Valor Unitário'])

    df['Data da Venda'] = pd.to_datetime(df['Data da Venda'], errors='coerce')
    df.dropna(subset=['Data da Venda'])

    print('Data transformed')
    return df
    