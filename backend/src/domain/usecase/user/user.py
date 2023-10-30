from typing import List
from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.user.user import User
from src.domain.interfaces.user.userInterface import UserInterface

class UserUseCase(UserInterface):
    def __init__(self, database: DatabaseActions):
        self.databaseAction = database

    def getUser(self, id) -> User: 
        return self.databaseAction.getUser(id)

    def getUsersList(self) -> List[User]:
        return self.databaseAction.getUsersList()

    def postUser(self, user: User) -> List[User]: 
        return self.databaseAction.postUser(user)