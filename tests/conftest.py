import pytest
from sqlalchemy.orm import Session
from conf.db_session import create_engine, create_tables, create_session


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