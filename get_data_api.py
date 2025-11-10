import requests
import pandas as pd

user_list = []

def get_user(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    user_info = response.json()

    return user_info


