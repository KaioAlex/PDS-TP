import pytest
from unittest.mock import MagicMock
from src.domain.actions.friendship.friendships import Friendships
from src.domain.interfaces.friendship.friendship import Friendship

@pytest.fixture
def mock_friendship_interface():
    return MagicMock()

def test_post_friendship_value(mock_friendship_interface):
    friendship = Friendships(friendshipinterface=mock_friendship_interface)

    friendship_value_test = Friendship(user_id1 = 0, user_id2 = -1)

    with pytest.raises(ValueError, match="valor invalido") as err:
        friendship.postFriendship(friendship_value_test)

    assert str(err.value) == "valor invalido"

def test_delete_friendship_value(mock_friendship_interface):
    friendship = Friendships(friendshipinterface=mock_friendship_interface)

    friendship_value_test = Friendship(user_id1 = 1, user_id2 = -1)

    with pytest.raises(ValueError, match="valor invalido") as err:
        friendship.deleteFriendships(friendship_value_test.user_id1, friendship_value_test.user_id2)

    assert str(err.value) == "valor invalido"
