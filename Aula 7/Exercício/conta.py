from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, nome, agencia, criacao):
        self.nome = nome
        self.agencia = agencia
        self.criacao = criacao

    @abstractmethod
    def cadastrar