import os
import pandas as pd
import psycopg2

class DB:
    def __init__(self, host, port, database, user, password):
            self.database=database,
            self.user=user,
            self.password=password,
            self.host=host,
            self.port=port

            self.conn = psycopg2.connect(
                host=self.database,
                port=self.database,
                database=self.database,
                user=self.database,
                password=self.database
            )
    
    def create_table(self, table_name, df):
        cols = ', '.join([f"{col} TEXT" for col in df.columns])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols});"
        
        with self.conn.cursor() as cursor:
            cursor.execute(create_table_query)
            self.conn.commit()
    
    def insert_data(self, table_name, df):
        cols = ', '.join(df.columns)
        values_placeholder = ', '.join(['%s'] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} ({cols}) VALUES ({values_placeholder});"
        
        with self.conn.cursor() as cursor:
            for _, row in df.iterrows():
                cursor.execute(insert_query, tuple(row))
            self.conn.commit()
