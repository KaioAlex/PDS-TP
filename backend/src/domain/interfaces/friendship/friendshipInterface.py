import inject
from abc import ABC, abstractmethod
from typing import List
from src.configuration import get_cursor
from src.configuration import get_conn

from src.domain.interfaces.friendship.friendship import Friendship

class FriendshipInterface(ABC):
    def getFriendshipsList(self, userId) -> List[int]:
        cursor = get_cursor()
        query =  f"SELECT DISTINCT CASE WHEN user_id1 = {userId} THEN user_id2 ELSE user_id1 END AS friend_id FROM bdSplitWallet.friendship WHERE user_id1 = {userId} OR user_id2 = {userId};"
        cursor.execute(query)
        friends = cursor.fetchall()
        
        cursor.close()
        
        return friends
    
    def post_friendship(self, friendship: Friendship):
        conn = get_conn()
        cursor = get_cursor()

        # Faz o post no banco
        cursor.execute(''' INSERT INTO friendship (user_id1, user_id2) VALUES(%s,%s)''',(friendship.user_id1, friendship.user_id2))
        conn.commit()
        
        cursor.close()

        return 
