from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.user.user import User
from src.configuration import get_cursor
from src.configuration import get_conn

class UserInterface():
    @abstractmethod
    def getUser(self, id) -> User:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        query = f"SELECT * FROM bdSplitWallet.users WHERE id = {id};"
        cursor.execute(query)

        # Recupere os resultados da consulta
        user = cursor.fetchone()

        cursor.close()

        return user

    @abstractmethod
    def getUsersList(self) -> List[User]:   
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
    def post_user(self, user: User) -> List[User]:
        conn = get_conn()
        cursor = get_cursor()

        # Faz o post no banco
        cursor.execute(''' INSERT INTO users (id, name, username, email, birth, balance, score) VALUES(%s,%s,%s,%s,%s,%s,%s)''',(user.id, user.name, user.username, user.email, user.birth, user.balance, user.score))
        conn.commit()

        # Execute a consulta na tabela "users"
        cursor.execute("SELECT * FROM bdSplitWallet.users;")
        
        # Recupere os resultados da consulta
        users = cursor.fetchall()

        cursor.close()

        return users
