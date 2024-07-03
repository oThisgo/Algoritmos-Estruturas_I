carros = "Uno", "Doblo", "Renegade", "Hilux"

print(carros)
print(carros[1])
print(carros[2:-3])

def calcular(x, y):
    return x + y, x - y, x * y, x / y

print(calcular(10 , 5))

a, b, c, d = calcular(10 , 5)

print(f"""
Soma: {a}
Subtração: {b}
Multiplicação: {c}
Divisão: {d}
""")

resultados = calcular(15, 5)

for x in resultados:
    print(x)