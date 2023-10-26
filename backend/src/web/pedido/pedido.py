# Adaptador REST
import inject
import json
from flask import Blueprint, jsonify, Response, request, render_template
from src.domain.actions.pedido.pedidos import Pedidos
from src.domain.interfaces.pedido.pedido import Pedido

@inject.autoparams()
def pedidos(pedidos: Pedidos) -> Blueprint:
    pedidos_blueprint = Blueprint('pedidos', __name__)

    @pedidos_blueprint.route('/api/get_pedidos', methods=['GET'])
    def get_pedidos() -> Response:
        response = pedidos.getPedidos()
        return jsonify({
            'pedidos': response
        })

    @pedidos_blueprint.route('/api/post_pedido', methods=['POST'])
    def post_pedido() -> Response:
        """ 
            Pega o conteudo do body do request, deve vir no type json
        """
        request_data = request.get_json()
        if (request_data is not None) and (type(request_data) is not dict):
            request_data = json.loads(request_data)

        pedido_obj: Pedido = None
        try:
            pedido_obj = Pedido(**request_data)
        except TypeError as err:
            return Response(str(err), status=400, mimetype='text/plain')
        response = pedidos.postPedidos(pedido_obj)

        return jsonify({
            'pedidos': response
        })
    return pedidos_blueprint
