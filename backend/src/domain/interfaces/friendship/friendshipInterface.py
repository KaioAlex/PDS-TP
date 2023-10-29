import inject
from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.friendship.friendship import Friendship

class FriendshipInterface(ABC):
    def getFriendshipsList(self) -> List[Friendship]:
        pass

    def post_friendship(self, friendship: Friendship) -> List[Friendship]:
        pass
