import requests

def get_cep(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    cep_info = response.json()

    return cep_info

cep_info = get_cep("49043349")

cep_list = ["49043349", "01001000", "20040002"]

for i in cep_list:
    print(get_cep(i))
