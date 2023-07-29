from model.programa import Programa

class Filme(Programa):
    def __init__(self,nome, ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f"Filme {{nome: {self.nome}, ano: {self.ano}, duracao: {self.duracao}, likes: {self.likes}}} "


