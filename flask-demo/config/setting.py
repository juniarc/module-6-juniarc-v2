from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(settings_conf=None):
    load_dotenv()

    app = Flask(__name__)
    os.environ.setdefault('FLASK_SETTING_MODULE', "config.dev")
    conf = settings_conf or os.getenv("FLASK_SETTING_MODULE")
    app.config.from_object(conf)

    from routes.animals.animals import animals_bp
    from routes.employees.employees import employee_bp
    from routes.feedings.feedings import feedings_bp
    from routes.enclosures.enclosures import enclosures_bp
    from routes.reports.reports import reports_bp
    from routes.visitors.visitors import visitors_bp

    app.register_blueprint(animals_bp, url_prefix='/animals')
    app.register_blueprint(employee_bp, url_prefix='/employees')
    app.register_blueprint(feedings_bp, url_prefix='/feedings')
    app.register_blueprint(enclosures_bp, url_prefix='/enclosures')
    app.register_blueprint(reports_bp, url_prefix='/reports')
    app.register_blueprint(visitors_bp, url_prefix='/visitors')

    db.init_app(app)
    migrate.init_app(app, db)

    ## berubah
    return app
