from db import DB
import pandas as pd
import os

db = DB(host="localhost", port=5432, database="postgres", user="postgres", password="postgres")

for file in os.listdir("2_silver_validated/"):
    name, ext = os.path.splitext(file)
    #if ext == ".parquet":
    #    table_name = name
    #    df = pd.read_parquet(f"2_silver_validated/{file}")
        
    #    db.create_table(table_name, df)
    #    db.insert_data(table_name, df)

    df = pd.read_parquet(f"2_silver_validated/{file}")

    db.create_table(file.replace(".parquet", ""), df)
    db.insert_data(file.replace(".parquet", ""), df)
