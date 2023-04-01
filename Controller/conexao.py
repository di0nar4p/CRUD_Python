import mysql.connector
from getpass import getpass


#conexão com o banco de dados
def db_connect():
    try:
        conn= mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        passwd= getpass('Digite a senha do banco: '),
        db='escola'
        )
    except Exception as error:
        raise error('Deu ruim')
    else:
        return conn


