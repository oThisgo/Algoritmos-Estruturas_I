from categoria import Categoria

class Veiculo:

    def __init__(self, marca = 'Fiat', ano = '2014', cat = Categoria('SUV')):
        self.id = id
        self.marca = marca
        self.ano = ano
        self.cat = cat

    def __str__(self):
        text = f"""
        Veículo

        Marca: {self.marca}
        Ano: {self.ano}
        Categoria: {self.cat.nome}"""

        return text

    def imprimir(self):
        print(self)