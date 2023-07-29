from model.programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Serie {{nome: {self.nome}, ano: {self.ano}, temporadas: {self.temporadas}, likes: {self.likes}}} "
    


