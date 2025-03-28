import mysql.connector
import os
from dotenv import load_dotenv

# Carregar o .env
load_dotenv()

#conexão com o banco de dados
def db_connect():
    '''Tenta realizar conexão com o banco de dados'''
    try:
        conn= mysql.connector.connect(
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT")),
        user='u610207868_di0nar4p',
        password='159753Pl@y',
        db=os.getenv("DATABASE")
        )
    except Exception as error:
        raise error
    else:
        return conn
db_connect()
