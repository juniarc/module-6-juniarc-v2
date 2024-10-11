from .base import *
import os

SQLALCHEMY_DATABASE_URI = os.getenv('POSTGRESS_CONNECTION_STRING')
