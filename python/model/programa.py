class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def remover_like(self):
        self._likes -= 1

    def mostrar_likes(self):
        return self.likes
    
    def __str__(self):
        return f"Programa {{Nome: {self.nome}, Ano: {self.ano}, Likes: {self.likes}}}"
