# Adaptador REST
import inject
import json
from flask import Blueprint, jsonify, Response, request, render_template, g
from src.domain.actions.friendship.friendships import Friendships
from src.domain.interfaces.friendship.friendship import Friendship

@inject.autoparams()
def friendships(friendships: Friendships) -> Blueprint:
    friendships_blueprint = Blueprint('friendships', __name__)

    @friendships_blueprint.route('/api/friendship/<id>', methods=['GET'])
    def get_friendships(id) -> Response:
        response = friendships.getFriendships(id)
        return jsonify({
            'friendships': response
        })

    @friendships_blueprint.route('/api/friendship', methods=['POST'])
    def post_friendship() -> Response:
        """ 
            Pega o conteudo do body do request, deve vir no type json
        """
        request_data = request.get_json()
        if (request_data is not None) and (type(request_data) is not dict):
            request_data = json.loads(request_data)

        Friendship_obj: Friendship = None
        try:
            Friendship_obj = Friendship(**request_data)
        except TypeError as err:
            return Response(str(err), status=400, mimetype='text/plain')
        response = friendships.postFriendships(Friendship_obj)

        return jsonify({
            'friendships': response
        })
        
    @friendships_blueprint.route('/api/friendship/<user_id>/<friend_id>', methods=['DELETE'])
    def delete_friendship(user_id, friend_id) -> Response:
        response = friendships.deleteFriendships(user_id,friend_id)
        return jsonify({
            'friendships': response
        })
        
    return friendships_blueprint


