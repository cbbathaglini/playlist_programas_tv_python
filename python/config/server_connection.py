import mysql.connector
from mysql.connector import Error
#from configuracao import Configuracao

class ServerConnection():
    
    def __init__(self):
        arrConfigs = self.db_config()

        self._host_name = arrConfigs[0]
        self._user_name = arrConfigs[1]
        self._user_password = arrConfigs[2]
        self._port = arrConfigs[3]
        self._database = arrConfigs[4]

    def db_config(self):
            return ["localhost", "root", "","3306","playlists_withoutdocker"];
    
    def create_server_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self._host_name,
                user=self._user_name,
                passwd=self._user_password,
                port= self._port,
                database=self._database
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        return connection
    

