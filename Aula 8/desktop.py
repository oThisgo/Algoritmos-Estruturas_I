from produto import Produto
from categoria import Categoria

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, fonte):
        super().__init__(modelo, cor, preco)
        self._fonte = fonte
    
    @property
    def fonte(self):
        return self._fonte

    @fonte.setter
    def bateria(self, potencia):
        self._fonte = potencia

    def cadastrar(self):
        self.categoria = Categoria(3, 'Desktop')

    def getInformacoes(self):
        return "\nDESKTOP\n" + super().getInformacoes() + "\n            Fonte: " + str(self._fonte) + "W"
        
    