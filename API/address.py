import json
from flask import request, make_response
from flask_restful import Resource
from repositories.address_repository import create_address, get_all_address, get_address_by_id, patch_address_by_id
from repositories.client_repository import get_client_by_id
from schemas.address_schema import PostAddressSchema, PatchAddressSchema


class AddressList(Resource):
    def post(self):
        data = json.loads(request.data)

        address_schema = PostAddressSchema(**data)
        is_not_valid = address_schema.validate()

        if is_not_valid:
            return make_response({"description": is_not_valid.get('description')}, is_not_valid.get('error_code'))

        client = get_client_by_id(id=data.get('client_id', None))
        if not client:
            return make_response({"description": f'Client ID {data.get("client_id")} was not found'}, 404)

        create_address(data=data, client=client)

        return make_response({}, 201)

    def get(self):
        address_models = get_all_address()

        return [address.dto() for address in address_models]


class Address(Resource):
    def get(self, id):
        address = get_address_by_id(id)
        if not address:
            return make_response({"description": f"Address ID {id} was not found"}, 404)

        return make_response(address.dto(), 200)

    def patch(self, id):
        data = json.loads(request.data)

        patch_address_schema = PatchAddressSchema(**data)
        is_not_valid = patch_address_schema.validate()

        if is_not_valid:
            return make_response({"description": is_not_valid.get('description')}, is_not_valid.get('error_code'))

        address = patch_address_by_id(id, data)
        if not address:
            return make_response({"description": f"Address ID {id} was not found"}, 404)

        return make_response(address.dto(), 200)

