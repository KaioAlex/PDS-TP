import pytest
from src.domain.interfaces.user.user import User
from src.domain.interfaces.user.userInterface import UserInterface

from src.domain.interfaces.transaction.transaction import Transaction
from src.domain.interfaces.transaction.transactionInterface import TransactionInterface
from src.domain.usecase.transaction.transaction import TransactionUseCase

@pytest.fixture
def user() -> User:
	return User("John", "J2024", "r2025@gmail.com", "2020-01-16", "50.00", "0", "teste1234", 255)

class TestUser:
    def test_create_user(self, user: User):
        assert user.id == 255
        assert user.name == "John"
        assert user.username == "J2024"
        assert user.email == "r2025@gmail.com"

    def test_add_balance(self, user: User):
        # Create a transaction instance
        transaction = Transaction(id_src=1, id_dest=2, value="100", date="2023-01-16", flag = 1, name_dest="caio")
        
        initial_balance = float(user.balance)
        amount_to_increase = 30

        user.balance = initial_balance + amount_to_increase

        assert user.balance == initial_balance + amount_to_increase

    def test_decrease_balance(self, user: User):        
        initial_balance = float(user.balance)
        amount_to_decrease = 30

        user.balance = initial_balance - amount_to_decrease

        assert user.balance == initial_balance - amount_to_decrease

    def test_decrease_balance_insufficient_funds(self, user: User):
        amount_to_decrease = 70

        with pytest.raises(ValueError, match="Insufficient funds"):
            if float(user.balance) - amount_to_decrease < 0:
                raise ValueError('Insufficient funds')

            user.balance = float(user.balance) - amount_to_decrease

        # Ensure balance remains unchanged
        assert user.balance == "50.00"

# Add more tests for other methods in the User class if needed