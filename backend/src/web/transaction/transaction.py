# Adaptador REST
import inject
import json
from flask import Blueprint, jsonify, Response, request, render_template, g
from src.domain.actions.transaction.transactions import Transactions
from src.domain.interfaces.transaction.transaction import Transaction

@inject.autoparams()
def transactions(transactions: Transactions) -> Blueprint:
    transactions_blueprint = Blueprint('transactions', __name__)
    
    @transactions_blueprint.route('/api/transaction/<id>', methods=['GET'])
    def getTransactions(id) -> Response:
        response = transactions.getTransactions(id)
        return jsonify({
            'transactions': response
        })
        
    
    @transactions_blueprint.route('/api/transaction/balance', methods=['POST'])
    def addBalance() -> Response:
        
        request_data = request.get_json()
        if (request_data is not None) and (type(request_data) is not dict):
            request_data = json.loads(request_data)
            
        response = transactions.addBalance(request_data['username'], request_data['value'])
        return jsonify({
            'transactions': response
        })
        

    @transactions_blueprint.route('/api/transaction', methods=['POST'])
    def post_transactions() -> Response:
        """ 
            Pega o conteudo do body do request, deve vir no type json
        """
        request_data = request.get_json()
        if (request_data is not None) and (type(request_data) is not dict):
            request_data = json.loads(request_data)

        Transaction_obj: Transaction = None
        try:
            Transaction_obj = Transaction(**request_data)
        except TypeError as err:
            return Response(str(err), status=400, mimetype='text/plain')
        response = transactions.postTransactions(Transaction_obj)
        
        return jsonify({
            'response': response
        })
        
    return transactions_blueprint
        