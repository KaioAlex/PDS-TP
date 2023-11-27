from typing import List
import inject

from src.domain.interfaces.transaction.transaction import Transaction
from src.domain.interfaces.transaction.transactionInterface import TransactionInterface

class ValorTransacaoAltoError(BaseException):
    pass

class Transactions:
    @inject.autoparams()
    def __init__(self, transactioninterface: TransactionInterface):
        self.__transactioninterface = transactioninterface

    def getTransactions(self, id:int) -> List[Transaction]: 
        return self.__transactioninterface.getTransactions(id)

    def postTransaction(self, tran:Transaction) -> Transaction: 
        if float(tran.value) > 10000:
            raise ValorTransacaoAltoError("valor de transacao muito alto")  
        return self.__transactioninterface.postTransaction(tran)

    def makeUsersTransfer(self, tran:Transaction) -> str:   
        if float(tran.value) > 10000:
            raise ValorTransacaoAltoError("valor de transacao muito alto")
        return self.__transactioninterface.makeUsersTransfer(tran)

    def addBalance(self, username:str, value:float) -> str:
        return self.__transactioninterface.addBalance(username, value)