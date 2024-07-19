from models.client import Client
from conf.db_session import create_session
from typing import List
from datetime import datetime


def get_all_clients() -> List[Client]:
    with create_session() as session:
        clients: List[Client] = session.query(Client).filter().all()

        return clients


def get_client_by_id(id):
    with create_session() as session:
        client: Client = session.query(Client).filter_by(id=id).one_or_none()
        if not client:
            return None
        return client


def check_if_data_is_duplicate(name, cpf):
    with create_session() as session:
        clients: List[Client] = session.query(Client).filter().all()

    for client in clients:
        if name.lower() == client.name.lower() or cpf == client.cpf:
            return False
    return True


def create_client(data):
    with create_session() as session:
        client: Client = Client()

        client.name = data["name"]
        client.birthday = parse_birthday(data["birthday"])
        client.cpf = data["cpf"]

        session.add(client)
        session.commit()

        return client


def update_client_by_id(id, data):
    with create_session() as session:
        client = session.query(Client).filter_by(id=id).one_or_none()
        if not client:
            return

        if "name" in data:
            client.name = str(data["name"])
        if "birthday" in data:
            client.birthday = data["birthday"]
        if "cpf" in data:
            client.cpf = data["cpf"]

        session.commit()

    return client


def get_age_by_birthday(birthday):
    current_year = datetime.now().year
    birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
    birthday_year = birthday_date.year

    age = current_year - birthday_year
    return age


def parse_birthday(birthday):
    birthday_date = datetime.strptime(birthday, '%d/%m/%Y').date()

    return birthday_date


def get_client_by_age(age, operation):

    date_ref = datetime.now().date().replace(year=datetime.now().date().year - int(age))
    with create_session() as session:
        if operation == 'gt':
            clients = session.query(Client).filter(Client.birthday < date_ref).all()
            return clients
