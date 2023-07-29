from mysql.connector import Error
class FilmeBD:
    def __init__(self):
        pass

    def cadastrar(self,filme, connection):
        try:

            cursor = connection.cursor()
            query = 'INSERT INTO filmes (nome, duracao, ano) VALUES (%s,%s,%s)'
            arrayBind = [filme.nome,filme.duracao,filme.ano]
            cursor.execute(query,arrayBind)
            connection.commit()
            
            print(f"{filme} - cadastrado com sucesso!")
            return filme
        except Error as err:
            print(f"Error: '{err}'")