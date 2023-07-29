class Filme:
    def __init__(self,nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao

    def imprime(self):
        print(f"Filme {{nome:{self.nome}, ano:{self.ano}, duracao:{self.duracao} }} ")

vingadores = Filme("Vingadores - Guerra Infinita",2022,160)
print(vingadores.nome)
