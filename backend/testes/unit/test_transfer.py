import pytest
from unittest.mock import MagicMock
from src.domain.actions.transaction.transactions import Transactions
from src.domain.interfaces.transaction.transaction import Transaction

@pytest.fixture
def mock_transaction_interface():
    return MagicMock()

def test_post_transaction_high_value(mock_transaction_interface):
    transactions = Transactions(transactioninterface=mock_transaction_interface)

    high_value_transaction = Transaction(id_src=1, id_dest=2, value="20000", date="2023-01-16", flag = 1, name_dest="caio")

    with pytest.raises(ValueError, match="valor de transacao muito alto") as err:
        transactions.postTransaction(high_value_transaction)

    assert str(err.value) == "valor de transacao muito alto"

def test_post_transaction_user_high_value(mock_transaction_interface):
    transactions = Transactions(transactioninterface=mock_transaction_interface)

    high_value_transaction = Transaction(id_src=1, id_dest=2, value="20000", date="2023-01-16", flag = 1, name_dest="caio")

    with pytest.raises(ValueError, match="valor de transacao muito alto") as err:
        transactions.makeUsersTransfer(high_value_transaction)

    assert str(err.value) == "valor de transacao muito alto"
