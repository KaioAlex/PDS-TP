from typing import List
from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.friendship.friendship import Friendship
from src.domain.interfaces.friendship.friendshipInterface import FriendshipInterface

class FriendshipUseCase(FriendshipInterface): 
    def __init__(self, database: DatabaseActions):
        self.databaseAction = database

    def getFriendshipList(self) -> List[Friendship]:
        return self.databaseAction.get_friendship()

    def post_friendship(self, friendship: Friendship) -> List[Friendship]:
        if friendship.id < 3:
            friendship.id = self.databaseAction.get_next_id()
        return self.databaseAction.post_friendship(friendship)
