import requests
import pandas as pd

user_list = []

def get_user(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    user_info = response.json()

    return user_info

users_path = "bronze_raw/users.csv"
users = pd.read_csv(users_path)

cep_list = users["cep"].tolist()

print(cep_list)

"""
_users = pd.DataFrame(users)
print(df_users.head())
"""
