from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.user.user import User

class UserInterface(ABC):
    @abstractmethod
    def getUsersList(self) -> List[User]:
        pass

    @abstractmethod
    def post_user(self, pedido: User) -> List[User]:
        pass
