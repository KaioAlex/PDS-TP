from typing import List
import inject
from src.domain.interfaces.database.database import DatabaseInterface

class DatabaseActions:

    @inject.autoparams()
    def get_next_id(self, database: DatabaseInterface) -> int:
        return database.get_next_id(self)
