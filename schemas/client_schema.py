from typing import Dict
import re


class ClientSchemaBase:
    def __init__(self, name: str = None, cpf: str = None, birthday: str = None):
        self.name = name
        self.cpf = cpf
        self.birthday = birthday

    def validate_birthday(self):
        regex = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$"
        if not re.match(regex, self.birthday):
            return False
        return True

    def validate(self):
        if self.name is not None and self.name.isdigit():
            return {"description": "The name field does not allow numbers", "error_code": 400}

        if self.cpf is not None and not isinstance(self.cpf, str):
            return {"description": "CPF must be a string", "error_code": 400}

        if self.birthday is not None:
            birth_is_valid = self.validate_birthday()
            if not birth_is_valid:
                return {"description": "Birthday must be in the format: 00/00/0000", "error_code": 400}


class PostClientSchema(ClientSchemaBase):
    def __init__(self, name: str = None, cpf: str = None, birthday: str = None):
        super().__init__(name, cpf, birthday)
        self.name = name
        self.cpf = cpf
        self.birthday = birthday

    def validate(self) -> Dict:
        if not self.name:
            return {"description": "Field Name is required", "error_code": 400}
        if not self.cpf:
            return {"description": "Field cpf is required", "error_code": 400}
        if not self.birthday:
            return {"description": "Field birthday is required", "error_code": 400}

        ret = super().validate()
        if ret:
            return ret


class PatchClientSchema(ClientSchemaBase):
    def __init__(self, name: str = None, cpf: str = None, birthday: str = None):
        self.name = name
        self.cpf = cpf
        self.birthday = birthday

    def validate(self):
        ret = super().validate()
        if ret:
            return ret
