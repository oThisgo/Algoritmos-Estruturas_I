precos = [4, 10, 5]

def aumentarPreco(valor):
    return valor * 1.1

novosPrecos = map(aumentarPreco, precos) 

print(list(novosPrecos))

valores = ((10, 20), [30, 40], [50], [60, 70, 80])

#def somar(x):
    #return x[0] + x[1]

#print(list(map(somar, valores)))

def somarValores(x):
    soma = 0
    for v in x:
        soma += v
    return soma

print(list(map(somarValores, valores)))