vendedores = {
    "Joao": 1500,
    "Marlon": 5000,
    "Ana": 5500,
    "Andre": 650,
    "Maria": 7000}

meta = 3000
bateram_meta = [vendedor
                for vendedor in vendedores
                if vendedores[vendedor]>meta]
print(bateram_meta)