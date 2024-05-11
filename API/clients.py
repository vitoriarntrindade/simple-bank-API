import json
from flask import request, make_response
from flask_restful import Resource
from repositories.client_repository import (
    get_all_clients,
    get_client_by_id,
    create_client,
    update_client_by_id,
    check_if_data_is_duplicate,
    get_client_by_age
)
from schemas.client_schema import PostClientSchema, PatchClientSchema


class Client(Resource):
    def get(self, id):
        client_model = get_client_by_id(id)
        if not client_model:
            return make_response({"description": f"Client {id} was not found"}, 404)
        return make_response(client_model.dto(), 200)

    def patch(self, id):
        data = json.loads(request.data)

        post_client_schema = PatchClientSchema(**data)
        is_not_valid = post_client_schema.validate()

        if is_not_valid:
            return make_response({"description": is_not_valid.get('description')}, is_not_valid.get('error_code'))

        client = update_client_by_id(id=id, data=data)
        if not client:
            return make_response({"description": f'Client ID {id} was not found'}, 404)

        return make_response(client.dto(), 200)


class ListClients(Resource):
    def post(self):
        data = json.loads(request.data)

        post_client_schema = PostClientSchema(**data)
        is_not_valid = post_client_schema.validate()

        if is_not_valid:
            return make_response({"description": is_not_valid.get('description')}, is_not_valid.get('error_code'))

        if not check_if_data_is_duplicate(name=data["name"], cpf=data["cpf"]):
            return make_response({"description": "duplicated cpf or name"}, 400)

        create_client(data=data)

        return make_response({}, 201)

    def get(self):
        age = request.args.get('age')
        operation = request.args.get('operation')
        if age and operation:
            clients_by_age = get_client_by_age(age=age, operation=operation)
            return [client.dto() for client in clients_by_age]

        clients = get_all_clients()

        response = [client.dto() for client in clients]
        return make_response(response, 200)

