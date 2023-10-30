from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.card.card import Card
from src.configuration import get_cursor
from src.configuration import get_conn

class CardInterface():
    @abstractmethod
    def getCard(self, id) -> Card:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        query = f"SELECT * FROM bdSplitWallet.cards WHERE id_user = {id};"
        cursor.execute(query)

        # Recupere os resultados da consulta
        cards = cursor.fetchall()

        cursor.close()

        if cards == '':
            return None

        else:
            return cards

    @abstractmethod
    def getCardList(self) -> List[Card]:   
        cursor = get_cursor()

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

    @abstractmethod
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
    
    def deleteCard(self, id: int):
        conn = get_conn()
        cursor = get_cursor()

        # Faz o delete no banco
        query = f"DELETE FROM cards WHERE id = {id};"
        cursor.execute(query)
        conn.commit()
        
        cursor.close()

        return "message: card deleted with sucess"
