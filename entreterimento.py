class Entreterimento:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    def remover_like(self):
        self.__likes -= 1

    def mostrar_likes(self):
        return self.likes