import inject
from abc import ABC, abstractmethod
from typing import List
from src.configuration import get_cursor
from src.configuration import get_conn

from src.domain.interfaces.friendship.friendship import Friendship

class FriendshipInterface(ABC):
    def getFriendshipsList(self) -> List[Friendship]:
        pass
    
    def post_friendship(self, friendship: Friendship):
        conn = get_conn()
        cursor = get_cursor()

        # Faz o post no banco
        cursor.execute(''' INSERT INTO friendship (user_id1, user_id2) VALUES(%s,%s)''',(friendship.user_id1, friendship.user_id2))
        conn.commit()
        
        cursor.close()

        return 
