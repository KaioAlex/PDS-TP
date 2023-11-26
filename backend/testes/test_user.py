import pytest
from src.domain.interfaces.user.user import User

def test_create_user():
    user = User("John", "J2024", "r2025@gmail.com", "16-01-2000", "0.0", "0", "teste1234", "255")

    assert user.id == '255'
    assert user.name == "John"
    assert user.username == "J2024"
    assert user.email == "r2025@gmail.com"

# def test_increase_balance():
#     user = User(id=1, name="John", username="john_doe", email="j2025@gmail.com")
#     initial_balance = user.balance
#     amount_to_increase = 50

#     user.increase_balance(amount_to_increase)

#     assert user.balance == initial_balance + amount_to_increase

# def test_decrease_balance():
#     user = User(id=1, name="John", username="john_doe", email="j2025@gmail.com")
#     user.balance = 100  # Set an initial balance
#     initial_balance = user.balance
#     amount_to_decrease = 30

#     user.decrease_balance(amount_to_decrease)

#     assert user.balance == initial_balance - amount_to_decrease

# def test_decrease_balance_insufficient_funds():
#     user = User(id=1, name="John", username="john_doe", email="j2025@gmail.com")
#     user.balance = 20  # Set an initial balance
#     amount_to_decrease = 30

#     with pytest.raises(ValueError, match="Insufficient funds"):
#         user.decrease_balance(amount_to_decrease)

#     # Ensure balance remains unchanged
#     assert user.balance == 20

# Add more tests for other methods in the User class if needed