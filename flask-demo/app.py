from flask import Flask
import os
from flask_migrate import Migrate

from routes.animals.animals import animals_bp
from routes.employees.employees import employee_bp
from routes.feedings.feedings import feedings_bp
from routes.enclosures.enclosures import enclosures_bp
from routes.reports.reports import reports_bp
from routes.visitors.visitors import visitors_bp
from config.setting import db

from models.animals import Animals
from models.employees import Employees
from models.enclosures import Enclosures
from models.feedings import Feedings
from models.visitors import Visitors

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRESS_CONNECTION_STRING')

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(animals_bp, url_prefix='/animals')
app.register_blueprint(employee_bp, url_prefix='/employees')
app.register_blueprint(feedings_bp, url_prefix='/feedings')
app.register_blueprint(enclosures_bp, url_prefix='/enclosures')
app.register_blueprint(reports_bp, url_prefix='/reports')
app.register_blueprint(visitors_bp, url_prefix='/visitors')

@app.route('/')
def home():
    return '<h1>Welcome to Animals and Employees API</h1><p>Add path /animals to access Animals data, Add path /employees to access Employees data</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)