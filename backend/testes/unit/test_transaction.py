import pytest

from src.domain.interfaces.transaction.transaction import Transaction
from src.domain.interfaces.transaction.transactionInterface import TransactionInterface
from src.domain.usecase.transaction.transaction import TransactionUseCase

@pytest.fixture
def transaction() -> Transaction:
    # Create a transaction instance
    transaction = Transaction(id_src=1, id_dest=2, value="100", date="2023-01-16", flag = 1, name_dest="caio")
        
    return transaction

class TestTransaction:
    def test_create_transaction(self, transaction: Transaction):
        assert transaction.id_src == 1
        assert transaction.id_dest == 2
        assert transaction.value == "100"
        assert transaction.date == "2023-01-16"

