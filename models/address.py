from sqlalchemy import Integer, Column, String, DateTime
from datetime import datetime
from models.model_base import ModelBase


class Address(ModelBase):
    __tablename__: str = "address"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    created_at: datetime = Column(DateTime, default=datetime.now, index=True)

    street_name: str = Column(String(45), nullable=False)
    number: int = Column(Integer, nullable=False)
    neighborhood: str = Column(String(200), nullable=False)
    state: str = Column(String(45), nullable=False)

    def dto(self):
        return {
            "id": self.id,
            "street_name": self.street_name,
            "number": self.number,
            "neighborhood": self.neighborhood,
            "state": self.state
        }
