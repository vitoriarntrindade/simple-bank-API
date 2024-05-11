from models.address import Address
from models.client import Client
from conf.db_session import create_session
from typing import List


def create_address(data, client: Client) -> Address:
    with create_session() as session:
        address = Address()
        address.street_name = data["street_name"]
        address.number = data["number"]
        address.neighborhood = data["neighborhood"]
        address.state = data["state"]

        session.add(address)
        session.commit()

        client.address_id = address.id

        session.add(client)
        session.commit()

        return address


def get_address_by_id(id) -> Address:
    with create_session() as session:
        address: Address = session.query(Address).filter(Address.id == id).one_or_none()

        return address


def get_all_address():
    with create_session() as session:
        address: List[Address] = session.query(Address).filter().all()
        if not address:
            return []

        return address


def patch_address_by_id(id, data):
    with create_session() as session:
        address: Address = session.query(Address).filter(Address.id == id).one_or_none()
        if not address:
            return

        if "street_name" in data:
            address.street_name = data["street_name"]
        if "number" in data:
            address.number = data["number"]
        if "neighborhood" in data:
            address.neighborhood = data["neighborhood"]
        if "state" in data:
            address.state = data["state"]

        session.commit()

        return address
