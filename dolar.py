from os import system
import requests
import json

requisicao = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")

cotacao = requisicao.json()

print("moeda:"+ cotacao["USD"]["name"])
print("data:" + cotacao["USD"]["create_date"])
print("Valor Atual: R$" + cotacao["USD"]["bid"])
preco = float(cotacao["USD"]["bid"])







