from repository.filmedb import FilmeBD
from model.filme import Filme
from config.server_connection import ServerConnection 
from mysql.connector import Error
#from config.configuracao import Configuracao
from model.excecao import Excecao

class FilmeRN:
    len_max_nome_filme = 120
    duracao_maior_que_0 = 0
    ano_maior_que_1900 = 1900

    def __init__(self):
        pass

    def validar_nome(self,filme, obj_excecao):
        nome_filme = filme.nome.strip()
        if(len(nome_filme) > self.len_max_nome_filme):
            obj_excecao.adiciona_validacao("Ops! Nome do filme tem mais que 120 caracteres")
        filme.nome = nome_filme
    
    def validar_duracao(self,filme, obj_excecao):
        duracao_filme = filme.duracao
        if(duracao_filme <= self.duracao_maior_que_0):
            obj_excecao.adiciona_validacao("Ops! O filme precisa ter mais que 0 minutos de duração")
        filme.duracao = duracao_filme

    def validar_ano(self,filme, obj_excecao):
        ano_filme = filme.ano
        if(ano_filme < self.ano_maior_que_1900):
            obj_excecao.adiciona_validacao("Ops! O filme precisa ser de um ano superior a 1900")
        filme.ano_filme = ano_filme

    

    def cadastrar(self,filme):

        try:
            connection = ServerConnection().create_server_connection()
            obj_excecao = Excecao()

            self.validar_nome(filme,obj_excecao)
            self.validar_ano(filme,obj_excecao)
            self.validar_duracao(filme,obj_excecao)
            
            obj_excecao.lancar_Validacoes()

            filmeBD = FilmeBD()
            filmeBD.cadastrar(connection=connection,filme=filme)
            connection.close()
        except Error as err:
            print(f"Error: '{err}'")
