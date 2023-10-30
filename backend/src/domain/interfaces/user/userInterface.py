import inject
from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.user.user import User
# from src.configuration import get_cursor
# from src.configuration import get_conn

class UserInterface(ABC):
    @abstractmethod
    def getUser(self, id) -> User:   
        pass

    @abstractmethod
    def getUsersList(self) -> List[User]:   
        pass

    @abstractmethod
    def postUser(self, user: User) -> List[User]:
        pass
