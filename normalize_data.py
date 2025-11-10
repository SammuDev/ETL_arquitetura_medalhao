import os
import pandas as pd

class NormalizedData:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def normalize(self):
        for file in os.listdir(self.input_dir):
            input_file = os.path.join(self.input_dir, file)
            output_file = os.path.join(self.output_dir, f"{file}.parquet")
            file, ext = os.path.splitext(file)
            
            if ext.lower() == '.csv':
                df = pd.read_csv(input_file)
            elif ext.lower() == '.json':
                try:
                    df = pd.read_json(input_file)
                except ValueError:
                    df = pd.read_json(input_file, lines=True)
            else:
                print(f"Formato de arquivo não suportado: {file}!")
                continue
            
            df.columns = [col.lower().replace(' ', '_') for col in df.columns]
            
            df.to_parquet(output_file, index=False)

if __name__ == "__main__":
    normalizer = NormalizedData(input_dir='1_bronze_raw', output_dir='2_silver_validated')
    normalizer.normalize()
