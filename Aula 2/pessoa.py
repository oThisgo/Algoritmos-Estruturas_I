class Pessoa:

    def __init__(self, nome, idade=18):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        texto = "Nome: " + self.nome
        texto += "\nIdade: " + str(self.idade)
        return texto
        