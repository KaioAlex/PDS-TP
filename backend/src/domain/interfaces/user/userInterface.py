from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.user.user import User
from src.configuration import get_cursor

class UserInterface():
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
    def post_user(self, pedido: User) -> List[User]:
        pass
