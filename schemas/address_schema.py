class AddressSchemaBase:
    def __init__(self, street_name: str = None, number: int = None,
                 neighborhood: str = None, state: str = None, client_id: int = None):
        self.street_name = street_name
        self.number = number
        self.neighborhood = neighborhood
        self.state = state
        self.client_id = client_id

    def validate(self):
        if self.street_name is not None and not isinstance(self.street_name, str):
            return {"description": "The field street name must be in string", "error_code": 400}

        if self.neighborhood is not None and not isinstance(self.neighborhood, str):
            return {"description": "The field neighborhood must be in string", "error_code": 400}

        if self.state is not None and not isinstance(self.state, str):
            return {"description": "The field state must be in string", "error_code": 400}

        if self.number is not None and not isinstance(self.number, int):
            return {"description": "The field number must be in integer number", "error_code": 400}

        if self.client_id is not None and not isinstance(self.client_id, int):
            return {"description": "The field client_id must be in integer number", "error_code": 400}


class PostAddressSchema(AddressSchemaBase):
    def __init__(self, street_name: str = None, number: int = None,
                 neighborhood: str = None, state: str = None, client_id: int = None):
        super().__init__(street_name=street_name, number=number, neighborhood=neighborhood,
                         state=state, client_id=client_id)

    def validate(self):
        if not self.street_name:
            return {"description": "Field street_name is required", "error_code": 400}
        if not self.number:
            return {"description": "Field number is required", "error_code": 400}
        if not self.neighborhood:
            return {"description": "Field neighborhood is required", "error_code": 400}
        if not self.state:
            return {"description": "Field state is required", "error_code": 400}
        if not self.client_id:
            return {"description": "Field client_id is required", "error_code": 400}

        ret = super().validate()
        if ret:
            return ret


class PatchAddressSchema(AddressSchemaBase):
    def __init__(self, street_name: str = None, number: int = None,
                 neighborhood: str = None, state: str = None, client_id: int = None):
        super().__init__(street_name=street_name, number=number, neighborhood=neighborhood,
                         state=state, client_id=client_id)

    def validate(self):
        ret = super().validate()
        if ret:
            return ret