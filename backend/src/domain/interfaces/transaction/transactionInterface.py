import inject
from abc import ABC, abstractmethod
from typing import List
from src.configuration import get_cursor
from src.configuration import get_conn

from src.domain.interfaces.transaction.transaction import Transaction
from src.domain.actions.user.users import Users

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
        
        self.makeUsersTransfer(tran)

        return tran
    
    def makeUsersTransfer(self, tran:Transaction):
        users_instance = Users() 
        user_src = users_instance.getUser(tran.id_src)
        user_dest = users_instance.getUser(tran.id_dest)
        
        user_dest.balance += tran.value
        user_dest.score += int(tran.value)
        user_src.score += int(tran.value)
        user_src.balance -= tran.value
        
        response = users_instance.updateUserTransfer(user_dest)
        response = users_instance.updateUserTransfer(user_src)
        
        print(response)
        
    def addBalance(self, username, value):
        users_instance = Users()  
        user = users_instance.getUserByUsername(username)
        
        user.balance += float(value)
        
        response = users_instance.updateUserTransfer(user)
        
        return response        
        
        
    