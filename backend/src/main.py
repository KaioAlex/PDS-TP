from flask import Flask
from src.configuration import configure_inject
from src.configuration import connect_to_db

from src.web.friendship.friendship import friendships
from src.web.user.user import user

app = Flask(__name__)
#mysql.init_app(app)
configure_inject(app)
app.register_blueprint(user())
app.register_blueprint(friendships())

#app.register_blueprint(telas())

connect_to_db()
