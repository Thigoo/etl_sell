import sqlite3
import pandas as pd

def load_data(df: pd.DataFrame, db_path: str = 'database/sales.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_date DATE,
            product TEXT,
            amount INTEGER,
            unit_value REAL,
            total_value REAL                   
        )
    ''')

    # insert data in the table
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO sales (sale_date, product, amount, unit_value, total_value)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            str(row['Data da Venda'].date()),
            row['Produto'],
            row['Quantidade Vendida'],
            row['Valor Unitário'],
            row['Total da Venda'],
        ))
    conn.commit()
    conn.close()
    print(f'{len(df)} registers inserted in {db_path}')