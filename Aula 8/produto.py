from abc import ABC, abstractmethod
from categoria import Categoria

class Produto(ABC):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = None

    def getInformacoes(self):
        if self.categoria == None:
            return f"""
            Modelo: {self.modelo}
            Cor: {self.cor}
            Preço: {self.preco}
            Categoria: Produto não cadastrado"""
        else:
            return f"""
            Modelo: {self.modelo}
            Cor: {self.cor}
            Preço: {self.preco}
            Categoria: {self.categoria}"""

    @abstractmethod
    def cadastrar(self):
        pass