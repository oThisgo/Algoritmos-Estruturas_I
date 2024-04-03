from veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, marca, ano, cat, cilindradas):
        super().__init__(marca, ano, cat)
        self.cilindradas = cilindradas

    def __str__(self):
        text = f"""
        Moto

        Marca: {self.marca}
        Ano: {self.ano}
        Categoria: {self.cat.nome}
        Cilindradas: {self.cilindradas}"""

        return text

    def imprimir(self):
        print(self)