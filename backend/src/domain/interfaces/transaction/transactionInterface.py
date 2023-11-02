import inject
from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.transaction.transaction import Transaction
#from src.domain.actions.user.users import Users

class TransactionInterface(ABC):
    @abstractmethod
    def getTransactions(self, id) -> List[Transaction]:
        pass
    
    @abstractmethod
    def postTransaction(self, tran: Transaction) -> Transaction:
        pass
    
    @abstractmethod
    def makeUsersTransfer(self, tran:Transaction) -> str:
        pass

    @abstractmethod  
    def addBalance(self, username, value) -> str:
        pass
