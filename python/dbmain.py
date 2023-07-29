import mysql.connector
from mysql.connector import Error
import pandas as pd
#from config.configuracao import Configuracao
from config.server_connection import ServerConnection 
from model.filme import Filme
from service.filmern import FilmeRN

filmeRN = FilmeRN()

operacao_cupido = Filme("Operação Cupido",1998,128)
filmeRN.cadastrar(filme=operacao_cupido)

#corra = Filme("c",1998,128)
#filmeRN.cadastrar(filme=corra)

'''
create_server = ServerConnection("localhost", "root", "","3306","playlists_withoutdocker")
connection = create_server.create_server_connection()


cursor = connection.cursor()
cursor.execute('Select * FROM filmes')
filmes = cursor.fetchall()
connection.close()

print(f"filmes {filmes}")



connection = ServerConnection("localhost", "root", "","3306","playlists_withoutdocker").create_server_connection()

tabela_documentario = """
CREATE TABLE documentario(
    idDocumentario int not null AUTO_INCREMENT,
    nome varchar(200) not null,
    duracao int not null,
    ano int not null,
    PRIMARY KEY(idDocumentario)
);
 """

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

execute_query(connection, tabela_documentario) 


'''