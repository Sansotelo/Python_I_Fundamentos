notas = []
media = 0.0

print("CADASTRO DE NOTAS")
qtd = int(input("Qtd de notas: "))

for i in range(qtd):
    notas.append(float(input(f'Nota {i+1}: ')))

print("CÁLCULO DA MÉDIA")

for i in notas:
    media += i

media = media / len(notas)
print(f"Média: {media:.2f}")