from typing import List

from src.domain.actions.database.database import DatabaseActions

from src.domain.interfaces.card.card import Card
from src.domain.interfaces.card.cardInterface import CardInterface

class CardUseCase(CardInterface):
    def __init__(self, database: DatabaseActions):
        self.databaseAction = database

    def getCard(self, id_card) -> Card: 
        return self.databaseAction.getCard(id_card)

    def getCardList(self, id_user) -> List[Card]:
        return self.databaseAction.getCardsList(id_user)

    def postCard(self, card: Card) -> List[Card]: 
        return self.databaseAction.postCard(card)

    def deleteCard(self, id) -> str: 
        return self.databaseAction.deleteCard(id)