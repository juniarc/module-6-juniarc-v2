import pytest

from config.setting import create_app, db
from models.animals import Animals
from models.enclosures import Enclosures
from models.employees import Employees
from models.visitors import Visitors

@pytest.fixture(scope='module')
def app():
    app = create_app("config.testing")

    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='function', autouse=True)
def test_db(app):
    db.create_all()

    yield db

    db.session.rollback()
    db.session.remove()
    db.drop_all()

@pytest.fixture
def appjson():
    return {'Content-Type' : 'application/json'}

@pytest.fixture
def add_sample_animals():
    sample_animals = [
        Animals(id=1, enclosure_id=1, name="Ujang", species="Cat", age=1, gender="Male", special_req="None"),
        Animals(id=2, enclosure_id=2, name="Onyet", species="Cat", age=1, gender="Female", special_req="None")
    ]

    db.session.bulk_save_objects(sample_animals)
    db.session.commit()

    yield sample_animals

    db.session.query(Animals).delete()
    db.session.commit()

@pytest.fixture
def add_sample_enclosures():
    sample_enclosures = [
        Enclosures(id=1, name="Kandang 1", location="Zona 1"),
        Enclosures(id=2, name="Kandang 2", location="Zona 1"),
    ]

    db.session.bulk_save_objects(sample_enclosures)
    db.session.commit()

    yield sample_enclosures

    db.session.query(Animals).delete()
    db.session.commit()

    db.session.query(Enclosures).delete()
    db.session.commit()

@pytest.fixture
def add_sample_visitors():
    sample_visitors = [
        Visitors(id=1, ticket_type="Child", event_type="Weekend day", date="31-10-2024 14:30:00", feedback="Positive"),
        Visitors(id=2, ticket_type="Adult", event_type="Normal day", date="31-10-2024 14:30:00", feedback="Positive")
    ]

    db.session.bulk_save_objects(sample_visitors)
    db.session.commit()

    yield sample_visitors

    db.session.query(Visitors).delete()
    db.session.commit()

@pytest.fixture
def add_sample_employees():
    sample_employees = [
        Employees(id=1, end_schedule="31-10-2024 14:30:00", name="Halim", role="Casheer", start_schedule="30-10-2024 14:30:00"),
        Employees(id=2, end_schedule="31-10-2024 14:30:00", name="Mahmud", role="Casheer", start_schedule="30-10-2024 14:30:00")
    ]

    db.session.bulk_save_objects(sample_employees)
    db.session.commit()

    yield sample_employees

    db.session.query(Employees).delete()
    db.session.commit()