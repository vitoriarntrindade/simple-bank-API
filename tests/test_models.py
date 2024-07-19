from datetime import datetime
from typing import List

import requests
from models.__all_models import *
from repositories.client_repository import parse_birthday


def test_parser_birthday():
    expected_date = datetime.strptime('21/10/1998', '%d/%m/%Y').date()

    parsed_date = parse_birthday('21/10/1998')

    assert parsed_date == expected_date


def test_create_client(test_session, base_url):
    url = f"{base_url}/clients"
    new_client_data = {'name': 'Charlie', 'cpf': '99011166680', 'birthday': '21/10/1998'}

    response = requests.post(url, json=new_client_data)
    added_client = test_session.query(Client).filter_by(name=new_client_data['name']).first()
    test_session.commit()

    assert response.status_code == 201
    assert added_client.name == "Charlie"


def test_update_client(test_session, base_url):
    url = f"{base_url}/clients/1"

    data = {'name': 'Teste', 'cpf': '11122233344'}

    response = requests.patch(url, json=data)

    client_update = test_session.query(Client).filter_by(id=1).first()

    assert client_update.cpf == '11122233344'
    assert response.status_code == 200


def test_get_all_clients_returns_list(base_url):
    url = f"{base_url}/clients"
    response = requests.get(base_url)

    assert response.status_code == 200


def test_create_address(test_session, base_url):
    url = f"{base_url}/address"

    data = {
        "street_name": "Hassib Mofarrej",
        "neighborhood": "Vila Leopoldina",
        "state": "São Paulo",
        "client_id": 1,
        "number": 500
    }

    response = requests.post(url, json=data)
    address = test_session.query(Address).filter_by(id=1).first()

    assert response.status_code == 201
    assert address.street_name == "Hassib Mofarrej"


def test_create_account(test_session, base_url):
    url = f"{base_url}/accounts"

    data = {"id_client": 1}
    response = requests.post(url, data)

    account = test_session.query(Account).filter_by(id=1).first()

    assert response.status_code == 201
    assert account.id == 1
