from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config_db import config_db


# Création d'un instance de l'application Flask
app = Flask(__name__)

# Initialisation de la DB
config_db(app)
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
