from produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, fonte):
        super().__init__(modelo, cor, preco, categoria)
        self._fonte = fonte
    
    @property
    def fonte(self):
        return self._fonte

    @fonte.setter
    def bateria(self, potencia):
        self._fonte = potencia

    def getInformacoes(self):
        return "DESKTOP\n" + super().getInformacoes() + "Fonte: " + self._fonte
