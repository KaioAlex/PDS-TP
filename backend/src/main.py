from flask import Flask
from flask_cors import CORS
from src.configuration import configure_inject
from src.configuration import connect_to_db

from src.web.friendship.friendship import friendships
from src.web.transaction.transaction import transactions
from src.web.user.user import user
from src.web.card.card import card

app = Flask(__name__)
cors = CORS(app)

configure_inject(app)
app.register_blueprint(user())
app.register_blueprint(card())
app.register_blueprint(friendships())
app.register_blueprint(transactions()) 


connect_to_db()
