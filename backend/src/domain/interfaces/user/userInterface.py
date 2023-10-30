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

        if user == '':
            return None

        else:
            response = User(id=user[0], name=user[1], username=user[2], email=user[3], birth=user[4], balance=user[5], score=user[6], password=user[7])

            return response
    
    def getUserByUsername(self, username) -> User:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        query = f"SELECT * FROM bdSplitWallet.users WHERE username = '{username}';"
        print("\n\n\n", query)
        cursor.execute(query)

        # Recupere os resultados da consulta
        user = cursor.fetchone()

        cursor.close()

        if user == '':
            return None

        else:
            response = User(id=user[0], name=user[1], username=user[2], email=user[3], birth=user[4], balance=user[5], score=user[6], password=user[7])

            return response
    
    def getLogin(self, username, password) -> User:   
        cursor = get_cursor()

        # Execute a consulta na tabela "users"
        query = f"SELECT * FROM bdSplitWallet.users WHERE username = '{username}' AND password = '{password}';"
        cursor.execute(query)

        # Recupere os resultados da consulta
        user = cursor.fetchone()

        cursor.close()

        if user == '':
            return None

        else:
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
    def post_user(self, user: User) -> User:
        conn = get_conn()
        cursor = get_cursor()
        query =  f"INSERT INTO bdSplitWallet.users (name, username, email, birth, balance, score, password) VALUES('{user.name}','{user.username}','{user.email}','{user.birth}','{user.balance}','{user.score}','{user.password}');"

        # Faz o post no banco
        cursor.execute(query)
        
        conn.commit()

        cursor.close()

        return user
    
    def updateUserTransfer(self, user: User) -> str:
        conn = get_conn()
        cursor = get_cursor()
        query = f"UPDATE bdSplitWallet.users SET balance = {user.balance}, score = {user.score}  WHERE id = {user.id};"

        # Faz o post no banco
        cursor.execute(query)
        
        conn.commit()

        cursor.close()
        

        return "transfer done"
