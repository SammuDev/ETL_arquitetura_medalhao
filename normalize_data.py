import os
import pandas as pd

input_dir = '1_bronze_raw'  # vamos ler os arquivos da pasta bronze (csv e json)
output_dir = '2_silver_validated'  # vamos salvar como arquivo .parquet

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    input_file = os.path.join(input_dir, filename)
    file, ext = os.path.splitext(filename)
    output_file = os.path.join(output_dir, f"{file}.parquet")
    
    if ext.lower() == '.csv':
        df = pd.read_csv(input_file)
    elif ext.lower() == '.json':
        try:
            df = pd.read_json(input_file)
        except ValueError:
            df = pd.read_json(input_file, lines=True)
    else:
        print(f"Formato de arquivo não suportado: {filename}!")
        continue  # pular arquivos que não são csv ou json
    
    # Normalização: converter nomes de colunas para minúsculas e substituir espaços por underscores
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    df.to_parquet(output_file, index=False)
