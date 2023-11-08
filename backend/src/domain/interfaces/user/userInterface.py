import inject
from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.user.user import User

class UserInterface(ABC):
    @abstractmethod
    def getUser(self, id) -> User:   
        pass
    
    @abstractmethod
    def getUserByUsername(self, username) -> User:   
        pass
    
    @abstractmethod
    def getLogin(self, username, password) -> User:   
        pass

    @abstractmethod
    def getUsersList(self) -> List[User]:   
        pass

    @abstractmethod
    def postUser(self, user: User) -> User:
        pass
    
    @abstractmethod
    def updateUserTransfer(self, user: User) -> str:
        pass
