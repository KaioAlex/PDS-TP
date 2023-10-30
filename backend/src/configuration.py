import inject
from flask import Flask
from src.adapters.database.mongo import MongoAdapter
from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.database.database import DatabaseInterface
from src.bd_config import db_config
import mysql.connector

def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(DatabaseInterface, MongoAdapter)

    inject.configure(config)

#conection with db
conn = None

def connect_to_db():
    global conn
    try:
        conn = mysql.connector.connect(**db_config)
        print("bd connected with sucess\n")
    except mysql.connector.Error as err:
        print(f"Erro de conexão com o banco de dados: {err}")
        
def get_cursor():
    return conn.cursor()

def get_conn():
    return conn
