import pytest

from src.domain.interfaces.card.card import Card
from src.domain.interfaces.card.cardInterface import CardInterface

from datetime import date

@pytest.fixture
def card() -> Card:
	return Card(2, "J2024", "1111111111111111", "2028-01-16", 123, 15)

class TestCard:
    def test_create_card(self, card: Card):
        assert card.id_user == 2
        assert card.username == "J2024"
        assert card.num_card == "1111111111111111"
        assert card.card_validity == "2028-01-16"

    def test_size_num_card(self, card: Card):
        assert len(card.num_card) == 16

    def test_validity(self, card: Card):
        year = card.card_validity.split("-")[0]
        year_current = date.today().strftime("%Y")

        assert int(year) > int(year_current)
