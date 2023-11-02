from typing import List

from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.transaction.transaction import Transaction
from src.domain.interfaces.transaction.transactionInterface import TransactionInterface

class TransactionUseCase(TransactionInterface):
    def __init__(self, database: DatabaseActions):
        self.databaseAction = database

    def getTransactions(self, id) -> List[Transaction]: 
        return self.databaseAction.getTransactions(id)

    def postTransaction(self, tran:Transaction) -> Transaction:   
        return self.databaseAction.postTransaction(tran)

    def makeUsersTransfer(self, tran:Transaction) -> str:   
        return self.databaseAction.makeUsersTransfer(tran)

    def addBalance(self, username:str, value:float) -> str:
        return self.databaseAction.addBalance(username, value)