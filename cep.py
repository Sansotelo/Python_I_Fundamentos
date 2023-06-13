from os import system
import requests
import json

requisicao = requests.get("https://cep.awesomeapi.com.br/json/cep")

buscacep = requisicao.json()

print("Endereco:" + buscacep["state"])

   
