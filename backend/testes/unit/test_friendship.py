# import pytest
# from unittest.mock import MagicMock
# from src.domain.actions.friendship.friendships import Friendships, FriendshipError
# from src.domain.interfaces.transaction.transaction import Transaction

# @pytest.fixture
# def mock_transaction_interface():
#     return MagicMock()

# def test_post_transaction_high_value(mock_transaction_interface):
#     friendship = Friendships(transactioninterface=mock_transaction_interface)

#     high_value_transaction = Transaction(value="20000")

#     with pytest.raises(ValorTransacaoAltoError, match="valor de transacao muito alto") as err:
#         transactions.postTransaction(high_value_transaction)

#     assert str(err.value) == "valor de transacao muito alto"

# def test_post_transaction_user_high_value(mock_transaction_interface):
#     transactions = Transactions(transactioninterface=mock_transaction_interface)

#     high_value_transaction = Transaction(value="20000")

#     with pytest.raises(ValorTransacaoAltoError, match="valor de transacao muito alto") as err:
#         transactions.makeUsersTransfer(high_value_transaction)

#     assert str(err.value) == "valor de transacao muito alto"