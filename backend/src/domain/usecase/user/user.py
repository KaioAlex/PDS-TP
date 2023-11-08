from typing import List

from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.user.user import User
from src.domain.interfaces.user.userInterface import UserInterface

class UserUseCase(UserInterface):
    def __init__(self, database: DatabaseActions):
        self.databaseAction = database

    def getUser(self, id) -> User: 
        return self.databaseAction.getUser(id)

    def getUserByUsername(self, username) -> User:   
        return self.databaseAction.getUserByUsername(username)

    def getLogin(self, username, password) -> User:   
        return self.databaseAction.getLogin(username, password)

    def getUsersList(self) -> List[User]:
        return self.databaseAction.getUsersList()

    def postUser(self, user: User) -> List[User]: 
        return self.databaseAction.postUser(user)

    def updateUserTransfer(self, user: User) -> str:
        return self.databaseAction.updateUserTransfer(user)