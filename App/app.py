from flask import Flask
from flask_restful import Api
from API.clients import Client, ListClients
from API.address import AddressList, Address
from API.accounts import Account, AccountsList, AccountByClient, AccountsDeposit, AccountsTransaction, AccountsWithdrawl

app = Flask(__name__)
api = Api(app=app)


api.add_resource(Client, "/clients/<int:id>")
api.add_resource(ListClients, "/clients/")
api.add_resource(Address, "/address/<int:id>")
api.add_resource(AddressList, "/address/")
api.add_resource(Account, "/accounts/<int:id>")
api.add_resource(AccountsList, "/accounts/")
api.add_resource(AccountByClient, "/accounts/clients/<int:id>")
api.add_resource(AccountsDeposit, "/accounts/deposit")
api.add_resource(AccountsTransaction, "/accounts/transaction")
api.add_resource(AccountsWithdrawl, "/accounts/withdrawl")









if __name__ == '__main__':
    app.run()