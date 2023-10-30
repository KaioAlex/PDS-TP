# Adaptador REST
import inject
import json
from flask import Blueprint, jsonify, Response, request, render_template
from src.domain.actions.user.users import Users
from src.domain.interfaces.user.user import User

@inject.autoparams()
def user(users: Users) -> Blueprint:
    user_blueprint = Blueprint('user', __name__)

    @user_blueprint.route('/api/user/login/<username>/<password>', methods=['GET'])
    def get_login(username, password) -> Response:
        response = users.getLogin(username, password)

        if response:
            return jsonify({
                'users': response
            })
        else:
            return jsonify({
                'users': "Not found"
            })

    @user_blueprint.route('/api/user/<id>', methods=['GET'])
    def get_user(id) -> Response:
        response = users.getUser(id)

        return jsonify({
            'user': response
        })
    
    @user_blueprint.route('/api/user/username/<username>', methods=['GET'])
    def get_user_by_name(username) -> Response:
        response = users.getUserByUsername(username)

        return jsonify({
            'user': response
        })

    @user_blueprint.route('/api/user', methods=['GET'])
    def get_users() -> Response:
        response = users.getUsers()
        return jsonify({
            'users': response
        })

    @user_blueprint.route('/api/user', methods=['POST'])
    def post_user():
        request_data = request.get_json()
        if (request_data is not None) and (type(request_data) is not dict):
            request_data = json.loads(request_data)

        user_obj: User = None
        try:
            user_obj = User(**request_data)
        except TypeError as err:
            return Response(str(err), status=400, mimetype='text/plain')
        response = users.postUsers(user_obj)

        return jsonify({
            'users': response
        })
    
    return user_blueprint