from typing import List
import inject
from src.domain.interfaces.friendship.friendship import Friendship
from src.domain.interfaces.friendship.friendshipInterface import FriendshipInterface


class Friendships:
    @inject.autoparams()
    def __init__(self, friendshipinterface: FriendshipInterface):
        self.__friendshipinterface = friendshipinterface

    def getFriendshipsList(self, id: int) :
        return self.__friendshipinterface.getFriendshipsList(id)
    
    def postFriendship(self, friendship: Friendship) -> List[Friendship]:
        if friendship.user_id1 < 0 or friendship.user_id2 < 0:
            
            raise ValueError("valor invalido")
        return self.__friendshipinterface.postFriendship(friendship)
    
    def deleteFriendships(self, user_id: int,friend_id: int) -> str:
        if user_id < 0 or friend_id < 0:
            
            raise ValueError("valor invalido")
        return self.__friendshipinterface.deleteFriendship(user_id, friend_id)
        

