class Cidade:
    def __init__(self, nome = 'Santa Cruz do Sul'):
        self.id = None
        self.nome = nome

    def __str__(self):
        return "Cidade: " + self.nome