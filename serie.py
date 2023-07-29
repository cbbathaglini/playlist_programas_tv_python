class Serie:
    def __init__(self,nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
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

    def imprime(self):
        print(f"Serie {{nome:{self.nome}, ano:{self.ano}, temporadas:{self.temporadas}, likes: {self.likes} }} ")
    


friends = Serie("Friends",1999,12)
friends.nome = "friends"
friends.dar_like()
friends.dar_like()
friends.imprime()