import inject
from abc import ABC, abstractmethod
from typing import List
from src.configuration import get_cursor
from src.configuration import get_conn

from src.domain.interfaces.friendship.friendship import Friendship

class FriendshipInterface(ABC):
    def getFriendshipsList(self, userId):
        cursor = get_cursor()
        query = f"SELECT friend_id, GROUP_CONCAT(name SEPARATOR ', ') AS friend_names FROM (SELECT DISTINCT CASE WHEN user_id1 = {userId} THEN user_id2 ELSE user_id1 END AS friend_id FROM bdSplitWallet.friendship WHERE user_id1 = {userId} OR user_id2 = {userId}) AS subquery LEFT JOIN bdSplitWallet.users ON subquery.friend_id = bdSplitWallet.users.id GROUP BY friend_id;"
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

        return friendship
    
    def deleteFriendship(self, user_id: int, friend_id: int):
        conn = get_conn()
        cursor = get_cursor()

        # Faz o delete no banco
        query = f"DELETE FROM friendship WHERE (user_id1 = {user_id} AND user_id2 = {friend_id}) OR (user_id1 = {friend_id} AND user_id2 = {user_id});"
        cursor.execute(query)
        conn.commit()
        
        cursor.close()

        return "message: user deleted with sucess"

