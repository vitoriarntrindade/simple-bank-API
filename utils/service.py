from models.account import Account
from conf.db_session import session


def check_account_balance(account: Account, value):
    if account.account_balance >= value:
        return True
    return False


def check_withdrawl_quantity_limit(account: Account):
    if account.withdrawl_quantity_limit > 0:
        return True

    return False


def check_withdrawl_value_limit(account: Account, value):
    if account.withdrawl_value_limit >= value:
        return True

    return False


def make_transaction(origin_account: Account, destination_account: Account, amount):
    if check_account_balance(origin_account, amount):
        origin_account.account_balance -= amount
        destination_account.account_balance += amount

        session.add(origin_account)
        session.add(destination_account)
        session.commit()
        session.close()

        return True


def withdrawl(account: Account, withdrawl_amount):
    account.account_balance -= withdrawl_amount
    account.withdrawl_quantity_limit -= 1
    session.add(account)
    session.commit()
    session.close()

    return True


def deposit(account: Account, deposit_amount):
    account.account_balance += deposit_amount

    session.add(account)
    session.commit()
    session.close()





