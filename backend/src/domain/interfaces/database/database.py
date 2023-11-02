from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.user.user import User
from src.domain.interfaces.card.card import Card

class DatabaseInterface(ABC):
    # User
    @abstractmethod
    def get_user(self, id) -> User:
        pass

    @abstractmethod
    def get_user_by_username(self, username) -> User:
        pass

    @abstractmethod
    def get_login(self, username, password) -> List[User]:
        pass

    @abstractmethod
    def get_users_list(self) -> List[User]:
        pass

    @abstractmethod
    def post_user(self, user: User) -> List[User]:   
        pass

    @abstractmethod
    def update_user_transfer(self, user) -> str:
        pass

    # Card
    @abstractmethod
    def get_card(self, id) -> Card:
        pass

    @abstractmethod
    def get_card_list(self) -> List[Card]:
        pass

    @abstractmethod
    def post_card(self, card: Card) -> Card:   
        pass

    @abstractmethod
    def delete_card(self, id) -> str:   
        pass