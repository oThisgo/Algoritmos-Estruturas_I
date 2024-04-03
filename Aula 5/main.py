from categoria import Categoria
from veiculo import Veiculo
from carro import Carro
from moto import Moto

cat1 = Categoria()
cat2 = Categoria("Esportiva")

v1 = Veiculo()
v1.imprimir

c1 = Carro("Jeep", 2021, Categoria("SUV"), 4)
c1.imprimir()

m1 = Moto("Honda", 2020, cat2, 250)
m1.imprimir()