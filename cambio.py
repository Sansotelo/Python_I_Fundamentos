from os import system
system ("cls")



print("&"*80)
print('CAMBIO DOLLAR'.center(80))
print('&'*80)
print("%"*80)
print("By Sandro Sotelo Bautista".center(80))
print("%"*80)

try:

    preciodolar = float(input("informe el precio en dolares USA:").replace(",","."))
    print("\nConverter para:")
    print("\t1 - Perú nuevos soles:")
    print("\t2 - Bolivia pesos bolivianos:")
    print("\t3 - Paraguai guaranies:")
    ele = input("Eleger:")
    if ele == "1":
        print (f"{preciodolar} dolares em Nuevos Soles é {(preciodolar*3.76):.2f}")
    elif ele =="2":
        print (f"{preciodolar} dolares em pesos bolivianos é {(preciodolar*6.91):.2f}")
    elif ele == "3":
        print (f"{preciodolar} dolares em guaranies é {(preciodolar*7160.70):.2f}")
    else:
        print("eleicao invalida")

except:
    print("erro de procesamento")