# Adaptador REST
import inject
import json
from flask import Blueprint, jsonify, Response, request, render_template
from src.domain.actions.card.cards import Cards
from src.domain.interfaces.card.card import Card

@inject.autoparams()
def card(cards: Cards) -> Blueprint:
    card_blueprint = Blueprint('card', __name__)
    print('Here')

    @card_blueprint.route('/api/user/login/<id>', methods=['POST'])
    def post_login(id) -> Response:
        response = users.getUser(id)

        if response:
            return jsonify({
                'users': response
            })
        else:
            return jsonify({
                'users': "Not found"
            })

    @card_blueprint.route('/api/card/<id>', methods=['GET'])
    def get_card(id) -> Response:
        response = users.getUser(id)

        return jsonify({
            'user': response
        })

    @card_blueprint.route('/api/cards', methods=['GET'])
    def get_cards() -> Response:
        response = users.getUsers()
        return jsonify({
            'users': response
        })

    @card_blueprint.route('/api/card', methods=['POST'])
    def post_card():
        request_data = request.get_json()
        if (request_data is not None) and (type(request_data) is not dict):
            request_data = json.loads(request_data)

        card_obj: Card = None
        try:
            card_obj = Card(**request_data)
        except TypeError as err:
            return Response(str(err), status=400, mimetype='text/plain')
        response = cards.postCards(card_obj)

        return jsonify({
            'cards': None
        })
    
    return card_blueprint