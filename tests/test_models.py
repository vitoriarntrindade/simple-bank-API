from datetime import datetime
import requests
from models.__all_models import *
import pytest
from sqlalchemy.orm import Session
from conf.db_session import create_engine, create_tables, create_session
from repositories.client_repository import parse_birthday


@pytest.fixture(scope='module')
def test_engine():
    engine = create_engine(testing=True)
    create_tables()
    yield engine


@pytest.fixture(scope='module')
def test_session(test_engine) -> Session:
    session = create_session()

    yield session
    session.close()


@pytest.fixture
def base_url():
    return 'http://localhost:5000'


def test_parser_birthday():
    expected_date = datetime.strptime('21/10/1998', '%d/%m/%Y').date()

    parsed_date = parse_birthday('21/10/1998')

    assert parsed_date == expected_date


def test_create_client(test_session: Session, base_url):
    url = f"{base_url}/clients"
    new_client_data = {'name': 'Charlie', 'cpf': '99011166680', 'birthday': '21/10/1998'}

    response = requests.post(url, json=new_client_data)
    added_client = test_session.query(Client).filter_by(name=new_client_data['name']).first()
    test_session.commit()

    assert response.status_code == 201
    assert added_client.name == "Charlie"


def test_update_client(test_session: Session, base_url):
    url = f"{base_url}/clients/1"

    data = {'name': 'Teste', 'cpf': '11122233344'}

    response = requests.patch(url, json=data)

    client_update = test_session.query(Client).filter_by(id=1).first()

    assert client_update.cpf == '11122233344'
    assert response.status_code == 200

