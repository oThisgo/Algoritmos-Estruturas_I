carro = {
    "Modelo" : "Renegade",
    "Ano" : 2021
}

carro2 = {"Modelo" : "Doblo", "Ano" : 2010}

print(carro)

for chave, valor in carro2.items():
    print(chave, " - ", valor)

for chave in carro.keys():
    print(chave, " - ", carro[chave])

frota = carro, carro2

print(frota)

carro2["Modelo"] = "Civic"

print(frota)
