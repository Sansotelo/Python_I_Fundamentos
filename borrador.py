print("*"*80)
print("By Sandro Sotelo".center(80))
print("#"*80)

print("-"*80)
print("Python 2023".center(80))



def Hello (apelido):
    return f"Bemvindo, {apelido}"
print(Hello(input("Qual é seu apelido?")))

def study (escola):
    return f"Vc estuda na , {escola}"
print(study(input("Onde vc estuda?")))

def professiao (oficio):
    return f"Seu oficio é, {oficio}"
print(professiao(input("Qual sua professiao")))

def data (nasci):
    return f"Seu aniversario é: {nasci}"
print(data(input("Quando é seu aniversaio?")))