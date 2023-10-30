from typing import List
import inject
from src.domain.interfaces.database.database import DatabaseInterface
from src.domain.interfaces.user.user import User

class DatabaseActions:
    @inject.autoparams()
    def get_user(self, id, database: DatabaseInterface) -> User:
        return database.get_user(self, id)

    @inject.autoparams()
    def get_users_list(self, database: DatabaseInterface) -> List[User]:
        return database.get_users_list(self)
        
    @inject.autoparams()
    def post_user(self, user: User, database: DatabaseInterface) -> List[User]: 
        return database.post_user(self, user)
