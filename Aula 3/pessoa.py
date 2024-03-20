from cidade import Cidade
class Pessoa:

    def __init__(self, nome, idade = 18, cidade = Cidade("Pindamonhangaba")):
        self.id = None
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
    
    def __str__(self):
        texto = "Nome: " + self.nome
        texto += "\nIdade: " + str(self.idade)
        return texto
        