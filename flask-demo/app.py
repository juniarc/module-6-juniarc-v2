from flask import Flask

from routes.animals.animals import animals_bp
from routes.employees.employees import employee_bp

app = Flask(__name__)

app.register_blueprint(animals_bp, url_prefix='/animals')
app.register_blueprint(employee_bp, url_prefix='/employees')

@app.route('/')
def home():
    return '<h1>Welcome to Animals and Employees API</h1><p>Add path /animals to access Animals data, Add path /employees to access Employees data</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)