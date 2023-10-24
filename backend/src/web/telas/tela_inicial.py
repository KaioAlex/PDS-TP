from flask import Blueprint, jsonify, Response, request, render_template

def telas() -> Blueprint:
    telas_blueprint = Blueprint('telas', __name__)

    @telas_blueprint.route('/')
    def tela_inicial():
        return render_template('index.html')

    return telas_blueprint