from typing import List
import inject

from src.domain.interfaces.database.database import DatabaseInterface
from src.domain.interfaces.user.user import User
from src.domain.interfaces.card.card import Card

class DatabaseActions:
    # User
    @inject.autoparams()
    def getUser(self, id, database: DatabaseInterface) -> User:
        return database.get_user(self, id)

    @inject.autoparams()
    def getUsersList(self, database: DatabaseInterface) -> List[User]:
        return database.get_users_list(self)
        
    @inject.autoparams()
    def postUser(self, user: User, database: DatabaseInterface) -> List[User]: 
        return database.post_user(self, user)

    # Card
    @inject.autoparams()
    def getCard(self, id_card, database: DatabaseInterface) -> Card:
        return database.get_card(self, id_card)

    @inject.autoparams()
    def getCardsList(self, id_user, database: DatabaseInterface) -> List[Card]:
        return database.get_cards_list(self, id_user)
        
    @inject.autoparams()
    def postCard(self, card: Card, database: DatabaseInterface) -> List[Card]: 
        return database.post_card(self, card)

    @inject.autoparams()
    def deleteCard(self, id, database: DatabaseInterface) -> List[Card]: 
        return database.delete_card(self, id)