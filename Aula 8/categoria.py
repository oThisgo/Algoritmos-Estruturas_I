class Categoria:
    def __init__(self, id = 1, nome = 'Tecnologia'):
        self.id = id
        self.nome = nome

    def __str__(self):
        return self.nome