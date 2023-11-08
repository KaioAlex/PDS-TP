import inject
from flask import Flask

from src.adapters.database.mysql import MysqlAdapter

from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.database.database import DatabaseInterface

from src.domain.interfaces.user.userInterface import UserInterface
from src.domain.usecase.user.user import UserUseCase

from src.domain.interfaces.card.cardInterface import CardInterface
from src.domain.usecase.card.card import CardUseCase

from src.domain.interfaces.transaction.transactionInterface import TransactionInterface
from src.domain.usecase.transaction.transaction import TransactionUseCase

from src.domain.interfaces.friendship.friendshipInterface import FriendshipInterface
from src.domain.usecase.friendship.friendship import FriendshipUseCase


from src.bd_config import db_config
import mysql.connector

def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(DatabaseInterface, MysqlAdapter)
        binder.bind(UserInterface, UserUseCase(DatabaseActions()))
        binder.bind(CardInterface, CardUseCase(DatabaseActions()))
        binder.bind(TransactionInterface, TransactionUseCase(DatabaseActions()))
        binder.bind(FriendshipInterface, FriendshipUseCase(DatabaseActions()))

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
