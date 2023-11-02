import inject
from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.friendship.friendship import Friendship

class FriendshipInterface(ABC):
    @abstractmethod
    def getFriendshipsList(self, userId: int) -> List[Friendship]:
        pass
    
    @abstractmethod
    def postFriendship(self, friendship: Friendship) -> List[Friendship]:
        pass
    
    @abstractmethod
    def deleteFriendship(self, user_id: int, friend_id: int) -> str:
        pass