import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path
from typing import Optional
from sqlalchemy.future.engine import Engine
from urllib.parse import quote
from models.model_base import ModelBase

__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False, testing: bool = False):
    global __engine

    if __engine:
        return

    if sqlite or testing:
        if testing:
            conn_str = 'sqlite:///:memory:'
        else:
            arquivo_db = 'db/simplebank.sqlite'
            folder = Path(arquivo_db).parent
            folder.mkdir(parents=True, exist_ok=True)
            conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})
    else:
        conn_str = "mysql+mysqlconnector://root:%s@localhost:3306/simplebank5" % quote('teste123!@#')
        __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)


session = create_session()
