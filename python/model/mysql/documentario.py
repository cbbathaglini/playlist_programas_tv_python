from model.programa import Programa
class Documentario(Programa):
    def __init__(self, nome, ano,duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    