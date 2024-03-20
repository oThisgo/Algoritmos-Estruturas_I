from categoria import Categoria
class Produto:
    def __init__(self, nome, preco, qtd, cat = Categoria()):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.cat = cat