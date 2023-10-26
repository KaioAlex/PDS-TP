from flask import Flask
from src.configuration import configure_inject
from src.configuration import connect_to_db
from src.web.pedido.pedido import pedidos
#from src.web.telas.tela_inicial import telas

#from src.web.telas.tela_inicial import mysql

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Root@2023'
app.config['MYSQL_DATABASE_DB'] = 'test'
#mysql.init_app(app)

configure_inject(app)
app.register_blueprint(pedidos())
#app.register_blueprint(telas())

connect_to_db()
