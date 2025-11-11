import os
import pandas as pd
import psycopg2

class DB:
    def __init__(self, host, port, database, user, password):
            self.host=host
            self.port=port
            self.database=database
            self.user=user
            self.password=password

            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
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
            for idx, row in df.iterrows():
                cursor.execute(insert_query, tuple(row))
            self.conn.commit()

if __name__ == "__main__":
    db = DB(host='localhost', port=5432, database='postgres', user='postgres', password='postgres')
    
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': ['25', '30', '35'],
        'city': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    
    table_name = 'people'
    
    db.create_table(table_name, df)
    db.insert_data(table_name, df)
