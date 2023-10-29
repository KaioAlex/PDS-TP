from typing import List
import inject
from src.domain.interfaces.friendship.friendship import Friendship
from src.domain.interfaces.friendship.friendshipInterface import FriendshipInterface

class Friendships:
    @inject.autoparams()
    def __init__(self, friendshipinterface: FriendshipInterface):
        self.__pedinterface = friendshipinterface

    def getFriendships(self) -> List[Friendship]:
        return self.__pedinterface.getFriendshipsList()
    
    def postFriendships(self, friendship: Friendship) -> List[Friendship]:
        return self.__pedinterface.post_friendship(friendship)

