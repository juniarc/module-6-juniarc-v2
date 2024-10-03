from flask import Flask

from routes.animals.animals import animals_bp
from routes.employees.employees import employee_bp

app = Flask(__name__)

app.register_blueprint(animals_bp, url_prefix='/animals')
app.register_blueprint(employee_bp, url_prefix='/employees')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)