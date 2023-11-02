from random import random
from typing import List

from src.domain.interfaces.database.database import DatabaseInterface

from src.domain.interfaces.user.user import User
from src.domain.actions.user.users import Users
from src.domain.interfaces.user.userInterface import UserInterface

from src.domain.interfaces.card.card import Card
from src.domain.interfaces.card.cardInterface import CardInterface

from src.domain.interfaces.transaction.transaction import Transaction
from src.domain.interfaces.transaction.transactionInterface import TransactionInterface

from src.bd_config import db_config
# from src.configuration import connect_to_db
import mysql.connector

conn = mysql.connector.connect(**db_config)
# print("bd connected with sucess\n")

def get_cursor():
    return conn.cursor()

def get_conn():
    return conn

class MysqlAdapter(DatabaseInterface):
    def get_user(self, id) -> User:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        query = f"SELECT * FROM bdSplitWallet.users WHERE id = {id};"
        cursor.execute(query)

        # Recupere os resultados da consulta
        user = cursor.fetchone()

        cursor.close()

        if user is None:
            return None
        else:
            response = User(id=user[0], name=user[1], username=user[2], email=user[3], birth=user[4], balance=user[5], score=user[6], password=user[7])

            return response

    def get_user_by_username(self, username) -> User:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        query = f"SELECT * FROM bdSplitWallet.users WHERE username = '{username}';"
        print("\n\n\n", query)
        cursor.execute(query)

        # Recupere os resultados da consulta
        user = cursor.fetchone()

        cursor.close()

        if user is None:
            return None

        else:
            response = User(id=user[0], name=user[1], username=user[2], email=user[3], birth=user[4], balance=user[5], score=user[6], password=user[7])

            return response

    def get_login(self, username, password) -> User:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        query = f"SELECT * FROM bdSplitWallet.users WHERE username = '{username}' AND password = '{password}';"
        cursor.execute(query)

        # Recupere os resultados da consulta
        user = cursor.fetchone()

        cursor.close()

        if user is None:
            return None

        else:
            return user

    def get_users_list(self) -> List[User]:
        cursor = get_conn().cursor()

        # Execute a consulta na tabela "users"
        query = "SELECT * FROM bdSplitWallet.users;"
        cursor.execute(query)

        # Recupere os resultados da consulta
        users = cursor.fetchall()

        # Faça algo com os resultados, como imprimir na tela
        for user in users:
            print(user)

        cursor.close()

        return users

    def post_user(self, user: User) -> List[User]: 
        conn = get_conn()
        cursor = get_cursor()
        query =  f"INSERT INTO bdSplitWallet.users (name, username, email, birth, balance, score, password) VALUES('{user.name}','{user.username}','{user.email}','{user.birth}','{user.balance}','{user.score}','{user.password}');"

        # Faz o post no banco
        cursor.execute(query)
        
        conn.commit()

        cursor.close()
        
        user = self.getUserByUsername(user.username)

        return user

    def update_user_transfer(self, user: User) -> str:
        conn = get_conn()
        cursor = get_cursor()
        query = f"UPDATE bdSplitWallet.users SET balance = {user.balance}, score = {user.score}  WHERE id = {user.id};"

        # Faz o post no banco
        cursor.execute(query)
        conn.commit()

        cursor.close()

        return "transfer done"

    def get_card(self, id_card) -> Card:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        cursor.execute(f"SELECT * FROM bdSplitWallet.cards WHERE id = {id_card};")

        # Recupere os resultados da consulta
        card = cursor.fetchone()

        cursor.close()

        if card is None:
            return None

        else:
            return card

    def get_cards_list(self, id_user) -> List[Card]:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        cursor.execute(f"SELECT * FROM bdSplitWallet.cards WHERE id_user = {id_user};")

        # Recupere os resultados da consulta
        cards = cursor.fetchall()

        cursor.close()

        if cards is None:
            return None

        else:
            return cards

    def post_card(self, card: Card) -> Card:
        conn = get_conn()
        cursor = get_cursor()

        # Faz o post no banco
        query =  f"INSERT INTO bdSplitWallet.cards (id_user, username, num_card, card_validity, security_code) VALUES('{card.id_user}','{card.username}','{card.num_card}','{card.card_validity}','{card.security_code}');"
        cursor.execute(query)
        conn.commit()

        cursor.close()

        return card
    
    def delete_card(self, id) -> str:
        conn = get_conn()
        cursor = get_cursor()

        # Faz o delete no banco
        query = f"DELETE FROM cards WHERE id = {id};"
        cursor.execute(query)
        conn.commit()
        
        cursor.close()

        return "message: card deleted with sucess"

    def get_transactions(self, id) -> List[Transaction]:
        cursor = get_cursor()
        query = f"SELECT transactions.*, users.name AS dest_name FROM bdSplitWallet.transactions LEFT JOIN bdSplitWallet.users ON transactions.id_dest = users.id WHERE transactions.id_src = {id} OR transactions.id_dest = {id}"
        
        cursor.execute(query)
        transactions = cursor.fetchall()
        
        cursor.close()
        
        return transactions
    
    def post_transaction(self, tran: Transaction) -> Transaction:
        conn = get_conn()
        cursor = get_cursor()
        
        query = f"INSERT INTO bdSplitWallet.transactions (id_src, id_dest, value, date, flag) VALUES ({tran.id_src}, {tran.id_dest}, {tran.value}, '{tran.date}', {tran.flag});"

        # Faz o post no banco
        cursor.execute(query)
        conn.commit()
                        
        cursor.close()
        
        self.makeUsersTransfer(tran)

        return tran
    
    def make_users_transfer(self, tran:Transaction) -> str:
        users_instance = Users() 
        user_src = users_instance.getUser(tran.id_src)
        user_dest = users_instance.getUser(tran.id_dest)
        
        user_dest.balance += float(tran.value)
        user_dest.score += int(tran.value)
        user_src.score += int(tran.value)
        user_src.balance -= float(tran.value)
        
        response = users_instance.updateUserTransfer(user_dest)
        response = users_instance.updateUserTransfer(user_src)
        
        print(response)
        
    def add_balance(self, username, value) -> str:
        users_instance = Users()
        user = users_instance.getUserByUsername(username)
        
        user.balance += float(value)
        
        response = users_instance.updateUserTransfer(user)
        
        return response    