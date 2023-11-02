from typing import List
import inject

from src.domain.interfaces.user.user import User
from src.domain.interfaces.user.userInterface import UserInterface

class Users:
    @inject.autoparams()
    def __init__(self, userinterface: UserInterface):
        self.__userinterface = userinterface

    def getUser(self, id) -> User:
        return self.__userinterface.getUser(id)
    
    def getUserByUsername(self, username) -> User:
        return self.__userinterface.getUserByUsername(username)
    
    def getLogin(self, username, password) -> User:
        return self.__userinterface.getLogin(username, password)

    def getUsers(self) -> List[User]:
        return self.__userinterface.getUsersList()
    
    def postUsers(self, user: User) -> User:
        return self.__userinterface.postUser(user)
    
    def updateUserTransfer(self, user: User) -> str:
        return self.__userinterface.updateUserTransfer(user)

