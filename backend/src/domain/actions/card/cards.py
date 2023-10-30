from typing import List
import inject
from src.domain.interfaces.card.card import Card
from src.domain.interfaces.card.cardInterface import CardInterface

class Cards:
    @inject.autoparams()
    def __init__(self, cardinterface: CardInterface):
        self.__cardinterface = cardinterface

    def getCard(self, id) -> Card:
        return self.__cardinterface.getCard(id)

    def getCards(self) -> List[Card]:
        return self.__cardinterface.getCardsList()
    
    def postCards(self, card: Card) -> List[Card]:
        return self.__cardinterface.post_card(card)

