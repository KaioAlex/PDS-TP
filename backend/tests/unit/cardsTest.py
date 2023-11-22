import unittest
from unittest.mock import Mock
from src.domain.interfaces.card.card import Card
from src.domain.interfaces.card.cardInterface import CardInterface
from src.domain.actions.card.cards import Cards

class TestCards(unittest.TestCase):

    def setUp(self):
        # Configurando o mock para CardInterface
        self.card_interface_mock = Mock(spec=CardInterface)
        self.cards = Cards(cardinterface=self.card_interface_mock)

    def test_getCard(self):
        # Configurando o comportamento esperado do mock
        expected_card = Card(id=1, username="Test Card")
        self.card_interface_mock.getCard.return_value = expected_card

        # Chamando o método da classe Cards
        result = self.cards.getCard(id_card=1)

        # Verificando se o método do mock foi chamado corretamente
        self.card_interface_mock.getCard.assert_called_once_with(1)

        # Verificando se o resultado é o esperado
        self.assertEqual(result, expected_card)

    def test_getCardList(self):
        # Configurando o comportamento esperado do mock
        expected_card_list = [Card(id=1, title="Test Card 1"), Card(id=2, title="Test Card 2")]
        self.card_interface_mock.getCardList.return_value = expected_card_list

        # Chamando o método da classe Cards
        result = self.cards.getCardList(id_user=1)

        # Verificando se o método do mock foi chamado corretamente
        self.card_interface_mock.getCardList.assert_called_once_with(1)

        # Verificando se o resultado é o esperado
        self.assertEqual(result, expected_card_list)

    # def test_postCard(self):
    #     # Configurando o comportamento esperado do mock
    #     input_card = Card(title="New Card")
    #     expected_card = Card(id=1, title="New Card")
    #     self.card_interface_mock.postCard.return_value = expected_card

    #     # Chamando o método da classe Cards
    #     result = self.cards.postCard(card=input_card)

    #     # Verificando se o método do mock foi chamado corretamente
    #     self.card_interface_mock.postCard.assert_called_once_with(input_card)

    #     # Verificando se o resultado é o esperado
    #     self.assertEqual(result, expected_card)

    # def test_deleteCard(self):
    #     # Configurando o comportamento esperado do mock
    #     id_to_delete = 1
    #     self.card_interface_mock.deleteCard.return_value = "Card deleted successfully."

    #     # Chamando o método da classe Cards
    #     result = self.cards.deleteCard(id=id_to_delete)

    #     # Verificando se o método do mock foi chamado corretamente
    #     self.card_interface_mock.deleteCard.assert_called_once_with(id_to_delete)

    #     # Verificando se o resultado é o esperado
    #     self.assertEqual(result, "Card deleted successfully.")

if __name__ == '__main__':
    unittest.main()
