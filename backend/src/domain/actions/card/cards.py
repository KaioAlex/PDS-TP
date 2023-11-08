from typing import List
import inject
from src.domain.interfaces.card.card import Card
from src.domain.interfaces.card.cardInterface import CardInterface

class Cards:
    @inject.autoparams()
    def __init__(self, cardinterface: CardInterface):
        self.__cardinterface = cardinterface

    def getCard(self, id_card) -> Card:
        return self.__cardinterface.getCard(id_card)

    def getCardList(self, id_user) -> List[Card]:
        return self.__cardinterface.getCardList(id_user)
           
    def postCard(self, card: Card) -> Card:
        return self.__cardinterface.postCard(card)
    
    def deleteCard(self, id: int) -> str:
        return self.__cardinterface.deleteCard(id)

