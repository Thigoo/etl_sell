from etl.extract import extract_data
from etl.transform import transform_data

data_path = 'data'
output_folder = 'documents/'

df = extract_data(data_path)
df.to_csv(output_folder + 'all_data.csv', index=False)
print(f'All data saved in: {output_folder + "all_data.csv"}')

df_transformed = transform_data(df)
df_transformed.to_csv(f'{output_folder + "transformed_data.csv"}', index=False)
print(f'Transformed data saved in: {output_folder + "transformed_data.csv"}')
