class Aluno:
    def __init__(self, cod, nome, matricula):
        self.cod = cod
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"""
        Código: {self.cod} 
        Nome: {self.nome}
        Matrícula: {self.matricula}
        """

    def Imprimir(self):
        print(str(self))

class AlunoEM(Aluno):
    def __init__(self, cod, nome, matricula, ano):
        super().__init__(cod, nome, matricula)
        self.ano = ano

    def __str__(self):
        return super().__str__() + f"Ano: {self.ano}" 

    def Imprimir(self):
        print(str(self))

class AlunoG(Aluno):
    def __init__(self, cod, nome, matricula, semestre):
        super().__init__(cod, nome, matricula)
        self.semestre = semestre

    def __str__(self):
        return super().__str__() + f"Semestre: {self.semestre}" 

    def Imprimir(self):
        print(str(self))
