from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
import os

db = SQLAlchemy()

engine = create_engine(os.getenv('POSTGRESS_CONNECTION_STRING'))
