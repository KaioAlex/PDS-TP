import inject
from abc import ABC, abstractmethod
from typing import List
from src.configuration import get_cursor
from src.configuration import get_conn

from src.domain.interfaces.transaction.transaction import Transaction

class TransactionInterface(ABC):
    def getTransactions(self):
        pass