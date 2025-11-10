import requests
import pandas as pd

user_list = []

def get_user(cep):
    try:
        endpoint = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(endpoint)
        user_info = response.json()

        return user_info
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

users_path = "bronze_raw/users.csv"
users = pd.read_csv(users_path)

cep_list = users["cep"].tolist()

for cep in cep_list:
    new_cep = get_user(cep.replace("-", ""))
    print(new_cep)
