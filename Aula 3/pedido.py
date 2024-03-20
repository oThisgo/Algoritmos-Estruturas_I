from pessoa import Pessoa
class Pedido:
    def __init__(self, endereco, cliente = Pessoa()):
        self.id = None
        self.endereco = endereco
        self.produtos = []
        self.cliente = cliente

    def addProduto(self, produtos):
        self.produtos.append(produtos)