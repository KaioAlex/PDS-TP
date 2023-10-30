from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.user.user import User

class DatabaseInterface(ABC):
    @abstractmethod
    def getUser(self, id) -> User:
        pass

    @abstractmethod
    def getUsersList(self) -> List[User]:
        pass

    @abstractmethod
    def post_user(self, user: User) -> List[User]:   
        pass