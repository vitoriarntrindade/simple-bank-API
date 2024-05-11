import json
from flask import request, make_response, render_template
from flask_restful import Resource
from repositories.account_repository import (create_account, get_account_by_id,
                                             get_all_accounts, get_account_by_client_id, get_account_by_account_number,
                                             get_accounts_by_balance_and_operation)
from repositories.client_repository import get_client_by_id
from schemas.account_schema import AccountSchemaBase, AccountTransaction,PostAccountSchema
from utils.service import make_transaction, withdrawl, deposit, check_account_balance, check_withdrawl_value_limit, \
    check_withdrawl_quantity_limit


class Account(Resource):
    def get(self, id):
        account = get_account_by_id(id)
        if not account:
            return make_response({"description": f'Account ID {id} was not found'}, 404)

        return make_response(account.dto(), 200)


class AccountsList(Resource):
    def post(self):
        data = json.loads(request.data)

        post_client_schema = PostAccountSchema(**data)
        is_not_valid = post_client_schema.validate()

        if is_not_valid:
            return make_response({"description": is_not_valid.get('description')}, is_not_valid.get('error_code'))

        client = get_client_by_id(data.get("client_id"))
        if not client:
            return make_response({"description": f'Client ID {data.get("client_id")} was not found'}, 404)

        create_account(client=client)

        return make_response({}, 201)

    def get(self):
        balance = request.args.get('balance', None)
        operation = request.args.get('operation', None)
        if balance and operation:
            accounts_by_balance = get_accounts_by_balance_and_operation(balance, operation)
            return [account.dto() for account in accounts_by_balance]

        account_models = get_all_accounts()

        return [account.dto() for account in account_models]


class AccountByClient(Resource):
    def get(self, id):
        client = get_client_by_id(id)
        if not client:
            return make_response({"description": f"Client ID {id} was not found"}, 404)

        account = get_account_by_client_id(client=client)
        if not account:
            return make_response({"description": "No accounts to show"}, 404)

        return make_response(account.dto(), 200)


class AccountsDeposit(Resource):
    def post(self):
        data = json.loads(request.data)

        account_schema = AccountSchemaBase(**data)
        is_not_valid = account_schema.validate()

        if is_not_valid:
            return make_response({"description": is_not_valid.get('description')}, is_not_valid.get('error_code'))

        account = get_account_by_account_number(data.get("account_number"))
        if not account:
            return make_response({"description": "Account was not found"}, 404)

        deposit(account=account, deposit_amount=data.get("amount"))

        return make_response({}, 200)


class AccountsTransaction(Resource):
    def post(self):

        data = json.loads(request.data)

        account_transaction = AccountTransaction(**data)
        is_not_valid = account_transaction.validate()

        if is_not_valid:
            return make_response({"description": is_not_valid.get('description')}, is_not_valid.get('error_code'))

        amount = data.get('amount')
        origin_account = get_account_by_account_number(data.get('origin_account_number'))
        if not origin_account:
            return make_response({"description": "Origin account was not fount"}, 404)

        destination_account = get_account_by_account_number(data.get('destination_account_number'))
        if not destination_account:
            return make_response({"description": "Destination account was not found"}, 404)

        transaction = make_transaction(origin_account=origin_account, destination_account=destination_account, amount=amount)
        if transaction:
            return make_response({"description": "success"}, 200)
        else:
            return make_response({"description": "Insufficient balance to carry out this operation"}, 400)


class AccountsWithdrawl(Resource):
    def post(self):
        data = json.loads(request.data)

        account = get_account_by_account_number(data.get("account_number"))
        if not account:
            return make_response({"description": f'Account {data["account_number"]} was not found'}, 404)

        ret_balance = check_account_balance(account=account, value=data['amount'])
        if not ret_balance:
            return make_response({"description": "Insufficient balance to carry out this operation"}, 400)

        ret_withdrawl_value_limit = check_withdrawl_value_limit(account=account, value=data['amount'])
        if not ret_withdrawl_value_limit:
            return make_response({"description": "Amount exceeded limit allowed per withdrawl"}, 400)

        ret_withdrawl_quantity_limit = check_withdrawl_quantity_limit(account=account)
        if not ret_withdrawl_quantity_limit:
            return make_response({"description": "You have reached the withdrawl journal limit"}, 400)

        withdrawl(account, data.get("amount"))

        return make_response({"description": "success"}, 200)

