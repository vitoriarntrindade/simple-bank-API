from typing import List

from sqlalchemy import (Integer,
                        Column, String, DateTime,
                        ForeignKey, Table, Date)
from datetime import datetime, date
from models.model_base import ModelBase
from sqlalchemy.orm import relationship, Mapped
from models.account import Account
from models.address import Address

accounts_client = Table('accounts_client',
                        ModelBase.metadata,
                        Column('id_client', Integer, ForeignKey('clients.id')),
                        Column('id_account', Integer, ForeignKey('accounts.id')))


class Client(ModelBase):
    __tablename__: str = "clients"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    created_at: datetime = Column(DateTime, default=datetime.now, index=True)

    name: str = Column(String(45), unique=True, nullable=False)
    birthday: date = Column(Date, nullable=False)
    cpf: str = Column(String(45), unique=True, nullable=False)

    address_id: int = Column(Integer, ForeignKey('address.id'))
    address: Mapped[Address] = relationship('Address', lazy='joined')

    accounts: Mapped[List[Account]] = relationship(
        'Account',
        secondary=accounts_client,
        backref='account',
        lazy='joined'
    )

    def dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "birthday": self.birthday.strftime('%d/%m/%Y'),
            "cpf": self.cpf
        }