import requests
import pandas as pd

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
users_list = []

for cep in cep_list:
    new_cep = get_user(cep.replace("-", ""))
    users_list.append(new_cep)
    print(new_cep)

users_df = pd.DataFrame(users_list)
users_df.to_csv("bronze_raw/users_info.csv", index=False)
