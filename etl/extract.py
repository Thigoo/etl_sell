import os
import pandas as pd

def extract_csv_data(folder: str) -> pd.DataFrame:
    if not os.path.exists(folder):
        raise FileNotFoundError(f'Folder {folder} was not searched')
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    if not files:
        print(f'Any SCV files was found in: {folder}')
    dataframes = []

    for file in files:
        file_path = os.path.join(folder, file)
        try:
            df = pd.read_csv(file_path)
            dataframes.append(df)
        except Exception as e:
            print(f'Error reading {file}: {e}')
        
    return pd.concat(dataframes, ignore_index=True)
