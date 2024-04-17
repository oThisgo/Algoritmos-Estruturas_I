from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, ano, portas):
        super().__init__(modelo, ano)
        self.qtdePortas = portas

    def ligar(self, chave):
        if chave == "1234":
            print('Carro Ligado')
        else:
            print('Não foi possível ligar o carro')

    def imprimir(self):
        print("CARRO\n")
        super().imprimir()
        print("Quantidade de Portas: ", self.qtdePortas)
