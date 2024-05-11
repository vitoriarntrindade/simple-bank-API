from random import randint, random
from typing import List
from conf.db_session import create_session
from models.account import Account
from models.client import Client


def get_all_accounts():
    with create_session() as session:
        accounts: List[Account] = session.query(Account).filter().all()
        if not accounts:
            return []

        return accounts


def get_account_by_id(id):
    with create_session() as session:
        account: Account = session.query(Account).filter_by(id=id).one_or_none()
        if not account:
            return

        return account


def get_account_by_client_id(client: Client) -> Account:
    for account in client.accounts:
        return account


def create_account(client: Client):
    get_account_number = generate_account_number()
    account_number_is_valid = check_if_account_number_exist(account_number=get_account_number)

    if not account_number_is_valid:
        return

    agency_number: str = "001"
    account_number: str = get_account_number
    withdrawl_value_limit: int = 500
    account_balance: int = 0
    withdrawl_quantity_limit: int = 3

    with create_session() as session:
        account = Account()
        account.agency_number = agency_number
        account.account_number = account_number
        account.withdrawl_quantity_limit = withdrawl_quantity_limit
        account.account_balance = account_balance
        account.withdrawl_value_limit = withdrawl_value_limit

        client.accounts.append(account)
        session.add(account)
        session.add(client)
        session.commit()

    return account


def generate_account_number():
    five_digits = randint(10000, 99999)
    three_digits = randint(10, 99)

    return f'{five_digits}-{three_digits}'


def check_if_account_number_exist(account_number: str) -> bool:
    account = get_account_by_account_number(account_number=account_number)

    if not account:
        return True

    return False


def get_account_by_account_number(account_number):
    with create_session() as session:
        account: Account = session.query(Account).filter(Account.account_number == account_number).one_or_none()

        return account


def get_accounts_by_balance_and_operation(balance, operation):
    with create_session() as session:
        if operation == 'gt':
            accounts: List[Account] = session.query(Account).filter(Account.account_balance > balance).all()
        if operation == 'lt':
            accounts: List[Account] = session.query(Account).filter(Account.account_balance < balance).all()

        return accounts