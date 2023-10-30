import inject
from abc import ABC, abstractmethod
from typing import List
from src.configuration import get_cursor
from src.configuration import get_conn

from src.domain.interfaces.transaction.transaction import Transaction

class TransactionInterface(ABC):
    def getTransactions(self, id) -> List[Transaction]:
        cursor = get_cursor()
        query = f"SELECT transactions.*, users.name AS dest_name FROM bdSplitWallet.transactions LEFT JOIN bdSplitWallet.users ON transactions.id_dest = users.id WHERE transactions.id_src = {id} OR transactions.id_dest = {id}"
        
        cursor.execute(query)
        transactions = cursor.fetchall()
        
        cursor.close()
        
        return transactions
    
    def postTransaction(self, tran: Transaction):
        conn = get_conn()
        cursor = get_cursor()
        
        query = f"INSERT INTO bdSplitWallet.transactions (id_src, id_dest, value, date, flag) VALUES ({tran.id_src}, {tran.id_dest}, {tran.value}, '{tran.date}', {tran.flag});"

        # Faz o post no banco
        cursor.execute(query)
        conn.commit()
                        
        cursor.close()

        return "transations inserted with sucess"