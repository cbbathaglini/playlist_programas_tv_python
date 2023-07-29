from mysql.connector import Error
class FilmeBD:
    def __init__(self):
        pass

    def cadastrar(self,filme, connection):
        try:

            cursor = connection.cursor()
            query = 'INSERT INTO filmes (nome, duracao, ano) VALUES ('+filme.nome+','+str(filme.duracao)+','+str(filme.ano)+')'
            

            '''
            arrayBind = []
            arrayBind = [['s',filme.nome]]
            arrayBind = [['i',filme.duracao]]
            arrayBind = [['i',filme.ano]]
            print(f"arraybind: {arrayBind}")
            '''

            cursor.execute(query)
            connection.commit()
            
            print(f"Filme {filme} - cadastrado com sucesso!")
            return filme
        except Error as err:
            print(f"Error: '{err}'")