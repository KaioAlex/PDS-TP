from abc import ABC, abstractmethod
from typing import List

class DatabaseInterface(ABC):
    @abstractmethod
    def get_next_id(self) -> int:
        pass
