from cidade import Cidade
from pessoa import Pessoa

c1 = Cidade("Porto Alegre")
c2 = Cidade("Gravataí")

p1 = Pessoa("Maria")
p2 = Pessoa("João")

p2.cidade = c1

print(p1.cidade)
print(p2.cidade)

print('-'*20)
c3 = Cidade()

p3 = Pessoa("Júlia")
p4 = Pessoa("Carlos", 20)
p5 = Pessoa("Thiago", 19, c2)
