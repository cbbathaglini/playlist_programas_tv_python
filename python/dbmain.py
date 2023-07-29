import mysql.connector
from mysql.connector import Error
import pandas as pd
#from config.configuracao import Configuracao
from config.server_connection import ServerConnection 
from model.filme import Filme
from service.filmern import FilmeRN


operacao_cupido = Filme("Operação Cupido",1998,128)
FilmeRN().cadastrar(filme=operacao_cupido)

