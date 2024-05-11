import re


class AccountSchemaBase:
    def __init__(self, account_number=None, amount=None):
        self.account_number = account_number
        self.amount = amount

    def validate_account_number(self):
        regex = r'^\d{5}-\d{2}$'

        if not re.match(regex, self.account_number):
            return False
        return True

    def validate(self):
        if not self.amount:
            return {"description": "Field amount is required", "error_code": 400}
        if not self.account_number:
            return {"description": "Field account_number is required", "error_code": 400}
        if not isinstance(self.account_number, str):
            return {"description": "Account number must be string", "error_code": 400}

        account_is_valid = self.validate_account_number()
        if not account_is_valid:
            return {"description": "Account number must be in the format:'37999-69'", "error_code": 400}

        if not isinstance(self.amount, int):
            return {"description": "The amount must be in numerical value", "error_code": 400}


class AccountTransaction(AccountSchemaBase):
    def __init__(self, origin_account_number=None, destination_account_number=None, amount=None):
        super().__init__(self)
        self.origin_account_number = origin_account_number
        self.destination_account_number = destination_account_number
        self.amount = amount

    def validate_account_number(self):
        regex = r'^\d{5}-\d{2}$'

        if not re.match(regex, self.origin_account_number) or not re.match(regex, self.destination_account_number):
            return False
        return True

    def validate(self):
        if not self.origin_account_number:
            return {"description": "Field origin_account is required", "error_code": 400}
        if not self.destination_account_number:
            return {"description": "Field destination_account is required", "error_code": 400}
        if not self.amount:
            return {"description": "Field amount is required", "error_code": 400}
        if not isinstance(self.amount, int):
            return {"description": "The amount must be in numerical value", "error_code": 400}

        if not isinstance(self.origin_account_number, str):
            return {"description": "Account number must be string", "error_code": 400}

        if not isinstance(self.destination_account_number, str):
            return {"description": "Account number must be string", "error_code": 400}

        account_is_valid = self.validate_account_number()
        if not account_is_valid:
            return {"description": "Account number must be in the format:'00000-00'", "error_code": 400}


class PostAccountSchema:
    def __init__(self, client_id=None):
        self.client_id = client_id

    def validate(self):
        if not self.client_id:
            return {"description": "Field client_id is required", "error_code": 400}
        if not isinstance(self.client_id, int):
            return {"description": "The field client_id must be in numerical value", "error_code": 400}

