from flask import Flask
from src.configuration import configure_inject
from src.web.pedido.pedido import pedidos
from src.web.telas.tela_inicial import telas

app = Flask(__name__)
configure_inject(app)
app.register_blueprint(pedidos())
app.register_blueprint(telas())
