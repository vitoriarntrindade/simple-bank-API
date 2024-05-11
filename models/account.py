from unicodedata import decimal
from decimal import Decimal
from sqlalchemy import (BigInteger, Integer,
                        Column, DateTime,
                        DECIMAL, String)
from datetime import datetime
from models.model_base import ModelBase


class Account(ModelBase):
    __tablename__: str = "accounts"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    created_at: datetime = Column(DateTime, default=datetime.now, index=True)

    agency_number: str = Column(String(45), nullable=False)
    account_number: str = Column(String(45), unique=True, nullable=False)
    withdrawl_value_limit: int = Column(Integer, nullable=False)
    account_balance: int = Column(Integer, nullable=False)
    withdrawl_quantity_limit: int = Column(Integer, nullable=False)

    def dto(self):
        return {
            "id": self.id,
            "agency_number": self.agency_number,
            "account_number": self.account_number,
            "withdrawl_value_limit": self.withdrawl_value_limit,
            "account_balance": self.account_balance,
            "withdrawl_quantity_limit": self.withdrawl_quantity_limit
        }

