from produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, bateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__bateria = bateria
    
    @property
    def bateria(self):
        return self.__bateria

    @bateria.setter
    def bateria(self, tempo):
        self.__bateria = tempo

    def getInformacoes(self):
        return "DESKTOP\n" + super().getInformacoes() + "Fonte: " + self.__bateria
