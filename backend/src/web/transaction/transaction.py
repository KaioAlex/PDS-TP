# Adaptador REST
import inject
import json
from flask import Blueprint, jsonify, Response, request, render_template, g
from src.domain.actions.transaction.transactions import Transactions
from src.domain.interfaces.transaction.transaction import Transaction

@inject.autoparams()
def transactions(transactions: Transactions) -> Blueprint:
    transactions_blueprint = Blueprint('transactions', __name__)
    return transactions_blueprint