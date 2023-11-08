from typing import List
import inject

from src.domain.interfaces.database.database import DatabaseInterface
from src.domain.interfaces.user.user import User
from src.domain.interfaces.card.card import Card
from src.domain.interfaces.transaction.transaction import Transaction
from src.domain.interfaces.friendship.friendship import Friendship

class DatabaseActions:
    # User
    @inject.autoparams()
    def getUser(self, id, database: DatabaseInterface) -> User:
        return database.get_user(self, id)

    @inject.autoparams()
    def getUserByUsername(self, username, database: DatabaseInterface) -> User:
        return database.get_user_by_username(self, username)

    @inject.autoparams()
    def getLogin(self, username, password, database: DatabaseInterface) -> List[User]:
        return database.get_login(self, username, password)

    @inject.autoparams()
    def getUsersList(self, database: DatabaseInterface) -> List[User]:
        return database.get_users_list(self)
        
    @inject.autoparams()
    def postUser(self, user: User, database: DatabaseInterface) -> List[User]: 
        return database.post_user(self, user)

    @inject.autoparams()
    def updateUserTransfer(self, user: User, database: DatabaseInterface) -> str: 
        return database.update_user_transfer(self, user)

    # Card
    @inject.autoparams()
    def getCard(self, id_card, database: DatabaseInterface) -> Card:
        return database.get_card(self, id_card)

    @inject.autoparams()
    def getCardsList(self, id_user, database: DatabaseInterface) -> List[Card]:
        return database.get_cards_list(self, id_user)
        
    @inject.autoparams()
    def postCard(self, card: Card, database: DatabaseInterface) -> Card: 
        return database.post_card(self, card)

    @inject.autoparams()
    def deleteCard(self, id, database: DatabaseInterface) -> str: 
        return database.delete_card(self, id)

    # Transaction
    @inject.autoparams()
    def getTransactions(self, id, database: DatabaseInterface) -> List[Transaction]:
        return database.get_transactions(self, id)

    @inject.autoparams()
    def postTransaction(self, tran:Transaction, database: DatabaseInterface) -> Transaction:
        return database.post_transaction(self, tran)
        
    @inject.autoparams()
    def makeUsersTransfer(self, tran:Transaction, database: DatabaseInterface) -> str:
        return database.make_users_transfer(self, tran)

    @inject.autoparams()
    def addBalance(self, username:str, value:float, database: DatabaseInterface) -> str:
        return database.add_balance(self, username, value)

    # Friendship
    @inject.autoparams()
    def getFriendshipsList(self, userId:int, database: DatabaseInterface) -> List[Friendship]:
        return database.get_friendships_list(self, userId)

    @inject.autoparams()
    def postFriendship(self, friendship: Friendship, database: DatabaseInterface) -> List[Friendship]:
        return database.post_friendship(self, friendship)

    @inject.autoparams()
    def deleteFriendship(self, user_id: int, friend_id: int, database: DatabaseInterface) -> str:
        return database.delete_friendship(self, user_id, friend_id)