from etl.extract import extract_csv_data

data_path = 'data'
outpu_path = 'documents/all_data.csv'

df = extract_csv_data(data_path)
df.to_csv(outpu_path, index=False)
print(f'All data saved in: {outpu_path}')
