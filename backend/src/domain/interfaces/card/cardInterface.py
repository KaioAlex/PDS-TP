from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.card.card import Card

class CardInterface(ABC):
    @abstractmethod
    def getCard(self, id_card) -> Card:   
        pass

    @abstractmethod
    def getCardList(self, id_user) -> List[Card]:   
        pass

    @abstractmethod
    def postCard(self, card: Card) -> List[Card]:
        pass

    @abstractmethod
    def deleteCard(self, id: int):
        pass
