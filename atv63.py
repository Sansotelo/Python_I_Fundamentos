from os import system
system("cls")

numero = 0
somapar = 0
for i in range(1,11):

    numero = int(input(f"Digite os {i} numeros aleatorios:"))
    if numero %2 ==0:
        somapar += numero
        print(f"Somatoria dos número pares é:{somapar}")

            