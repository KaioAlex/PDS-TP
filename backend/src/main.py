from flask import Flask
from src.configuration import configure_inject
from src.configuration import connect_to_db
from src.web.pedido.pedido import pedidos

from src.web.friendship.friendship import friendships
from src.web.user.user import user
from src.web.card.card import card

app = Flask(__name__)

configure_inject(app)
app.register_blueprint(pedidos())
app.register_blueprint(user())
app.register_blueprint(card())
app.register_blueprint(friendships())


connect_to_db()
