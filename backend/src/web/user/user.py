# Adaptador REST
import inject
import json
from flask import Blueprint, jsonify, Response, request, render_template
from src.domain.actions.user.users import Users
from src.domain.interfaces.pedido.pedido import Pedido

@inject.autoparams()
def user(users: Users) -> Blueprint:
    user_blueprint = Blueprint('user', __name__)

    @user_blueprint.route('/api/get_users', methods=['GET'])
    def get_user() -> Response:
        response = users.getUsers()
        return jsonify({
            'users': response
        })
    
    return user_blueprint