# Adaptador REST
import inject
import json
from flask import Blueprint, jsonify, Response, request, render_template
from src.domain.actions.card.cards import Cards
from src.domain.interfaces.card.card import Card

@inject.autoparams()
def card(cards: Cards) -> Blueprint:
    card_blueprint = Blueprint('card', __name__)

    @card_blueprint.route('/api/card/<id_card>', methods=['GET'])
    def get_card(id_card) -> Response:
        response = cards.getCard(id_card)

        return jsonify({
            'card': response
        })

    @card_blueprint.route('/api/cards/<id_user>', methods=['GET'])
    def get_card_list(id_user) -> Response:
        response = cards.getCardList(id_user)

        return jsonify({
            'cards': response
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
        
    @card_blueprint.route('/api/card/<id>', methods=['DELETE'])
    def delete_card(id) -> Response:
        response = cards.deleteCard(id)
        return jsonify({
            'cards': response
        })
    
    return card_blueprint