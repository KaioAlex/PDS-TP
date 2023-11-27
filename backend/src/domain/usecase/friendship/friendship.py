from typing import List

from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.friendship.friendship import Friendship
from src.domain.interfaces.friendship.friendshipInterface import FriendshipInterface



class FriendshipUseCase(FriendshipInterface): 
    def __init__(self, database: DatabaseActions):
        self.databaseAction = database

    def getFriendshipsList(self, userId) -> List[Friendship]:
        return self.databaseAction.getFriendshipsList(userId)

    def postFriendship(self, friendship: Friendship) -> List[Friendship]:
        return self.databaseAction.postFriendship(friendship)

    def deleteFriendship(self, user_id: int, friend_id: int) -> str:
        return self.databaseAction.deleteFriendship(user_id, friend_id)