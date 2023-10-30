from random import random
from typing import List

from src.domain.interfaces.database.database import DatabaseInterface

from src.domain.interfaces.user.user import User
from src.domain.interfaces.user.userInterface import UserInterface

from src.domain.interfaces.card.card import Card
from src.domain.interfaces.card.cardInterface import CardInterface

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
        cursor = get_conn().cursor()

        # Execute a consulta na tabela "users"
        query = f"SELECT * FROM bdSplitWallet.users WHERE id = {id};"
        cursor.execute(query)

        # Recupere os resultados da consulta
        user = cursor.fetchone()

        cursor.close()

        if user == '':
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
        cursor = get_conn().cursor()

        # Faz o post no banco
        cursor.execute(''' INSERT INTO users (id, name, username, email, birth, balance, score) VALUES(%s,%s,%s,%s,%s,%s,%s)''',(user.id, user.name, user.username, user.email, user.birth, user.balance, user.score))
        conn.commit()

        # Execute a consulta na tabela "users"
        # cursor.execute("SELECT * FROM bdSplitWallet.users;")
        
        # Recupere os resultados da consulta
        # users = cursor.fetchall()

        cursor.close()

        return f"Done"

    def get_card(self, id_card) -> Card:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        cursor.execute(f"SELECT * FROM bdSplitWallet.cards WHERE id = {id_card};")

        # Recupere os resultados da consulta
        card = cursor.fetchone()

        cursor.close()

        if card == '':
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

        if cards == '':
            return None

        else:
            return cards

    def post_card(self, card: Card) -> List[Card]:
        conn = get_conn()
        cursor = get_cursor()

        # Faz o post no banco
        cursor.execute(''' INSERT INTO cards (id, id_user, username, num_card, card_validity, security_code) VALUES(%s,%s,%s,%s,%s,%s)''',(card.id, card.id_user, card.username, card.num_card, card.card_validity, card.security_code))
        conn.commit()

        # Execute a consulta na tabela "users"
        # cursor.execute("SELECT * FROM bdSplitWallet.users;")
        
        # Recupere os resultados da consulta
        # users = cursor.fetchall()

        cursor.close()

        return
    
    def delete_card(self, id):
        conn = get_conn()
        cursor = get_cursor()

        # Faz o delete no banco
        query = f"DELETE FROM cards WHERE id = {id};"
        cursor.execute(query)
        conn.commit()
        
        cursor.close()

        return "message: card deleted with sucess"
