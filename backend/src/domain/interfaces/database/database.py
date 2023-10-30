from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.user.user import User
from src.domain.interfaces.card.card import Card

class DatabaseInterface(ABC):
    @abstractmethod
    def get_user(self, id) -> User:
        pass

    @abstractmethod
    def get_users_list(self) -> List[User]:
        pass

    @abstractmethod
    def post_user(self, user: User) -> List[User]:   
        pass

    @abstractmethod
    def get_card(self, id) -> User:
        pass

    @abstractmethod
    def get_card_list(self) -> List[User]:
        pass

    @abstractmethod
    def post_card(self, card: Card) -> List[Card]:   
        pass

    @abstractmethod
    def delete_card(self, id) -> str:   
        pass