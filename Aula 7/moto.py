from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, ano, cilindradas):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas

    def ligar(self, chave):
        if chave == "1234":
            print('Moto Ligada')
        else:
            print('Não foi possível ligar a moto')

    def imprimir(self):
        print('\nMOTO')
        super().imprimir()
        print("Cilindradas: ", self.cilindradas)
