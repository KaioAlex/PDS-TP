from random import random
from typing import List
from src.domain.interfaces.database.database import DatabaseInterface

pedidos_db = [
    {'id': 0, 'title': 'Pastel'},
    {'id': 1, 'title': 'Pizza'},
    {'id': 2, 'title': 'Sushi'},
]

class MongoAdapter(DatabaseInterface):

    def get_next_id(self) -> int:
        # retorna id randomico interiro
        return int(random() * 100)
