import pytest
from typing import List

from src.adapters.database.mysql import MysqlAdapter
from src.domain.interfaces.user.user import User

@pytest.fixture
def database() -> MysqlAdapter:
	return MysqlAdapter()

@pytest.fixture
def user() -> User:
	# Aqui será feito um post na base de dados mesmo para podermos testar
	user_obj = User(**{"name": "teste", "username": "t2024", "password": "123", "email": "c@proton.me", "birth": "2020-01-16", "balance": "50.00", "score": 0})
	fetched_post = MysqlAdapter().post_user(user_obj)

	return fetched_post

class TestMysqlAdapter:
	# Get the last user inserted (inserido na função acima)
	def test_get_user(self, database: MysqlAdapter, user: User):
		fetched_users = database.get_users_list()
	
		assert fetched_users[len(fetched_users)-1][1] == user.name

""" 	def test_post_user(self, database: MysqlAdapter, user: User):
		user_obj = User(**{"name": "caio", "username": "k2024", "password": "123", "email": "c@proton.me", "birth": "2020-01-16", "balance": "50.00", "score": 0})
		fetched_post = database.post_user(user_obj)

		# Pega só o ultimo user e compara, pois a base de dados é fixo
		assert fetched_post[len(fetched_post)-1] == user[len(user)-1]
 """
	# def test_get_next_id(self, database: MysqlAdapter):
	# 	fetched_id = database.get_next_id()
	# 	assert isinstance(fetched_id, int)