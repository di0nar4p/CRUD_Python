import mysql.connector
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


load_dotenv()

#conexão com o banco de dados
def db_connect():
    '''Conexão com SQLAlchemy'''
    pwd = '159753Play'
    host = 'srv1659.hstgr.io'
    engine = create_engine(f"mysql+pymysql://u610207868_di0nar4p:{pwd}@{host}:3306/u610207868_glauco")

    Session = sessionmaker(bind=engine)
    session = Session()
    return session
    
