lado1 = input("Informe o primeiro lado: ")
lado2 = input("Informe o segundo lado: ")

# Verificar se valores são numéricos
print("Lado 1 é numérico?", lado1.isnumeric())
print("Lado 2 é numérico?", lado2.isnumeric())

area = float(lado1) * float(lado2)

print(f"A área é {area}")

