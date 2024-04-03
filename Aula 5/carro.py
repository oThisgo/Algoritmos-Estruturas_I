from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, ano, cat, portas):
        super().__init__(marca, ano, cat)
        self.portas = portas

    def __str__(self):
        return super().__str__() + f"\nPortas: {str(self.portas)}"

    def imprimir(self):
        print("-----Carro-----")
        super().imprimir()
        print(self)
