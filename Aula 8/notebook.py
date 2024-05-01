from produto import Produto
from categoria import Categoria

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, bateria):
        super().__init__(modelo, cor, preco)
        self.__bateria = bateria
    
    @property
    def bateria(self):
        return self.__bateria

    @bateria.setter
    def bateria(self, tempo):
        self.__bateria = tempo

    def cadastrar(self):
        self.categoria = Categoria(2, 'Notebook')

    def getInformacoes(self):
        return "\nNOTEBOOK\n" + super().getInformacoes() + "\n            Tempo de Bateria: " + str(self.__bateria) + "h"

    