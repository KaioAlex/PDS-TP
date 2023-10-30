from typing import List
import inject
from src.domain.interfaces.transaction.transaction import Transaction
from src.domain.interfaces.transaction.transactionInterface import TransactionInterface

class Transactions:
    @inject.autoparams()
    def __init__(self, transactionnterface: TransactionInterface):
        self.__traninterface = transactionnterface

    def getTransactions(self, id: int) -> List[Transaction]:
        return self.__traninterface.getTransactions(id)
    
    def postTransactions(self, transaction: Transaction):
        return self.__traninterface.postTransaction(transaction)