import requests

def get_cep(cep):
    endpoint = f"viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    cep_info = response.json()

get_cep("01001000")
