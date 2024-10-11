from .base import *
import os

SQLALCHEMY_DATABASE_URI = os.getenv('TEST_POSTGRESS_CONNECTION_STRING')
TESTING = True
