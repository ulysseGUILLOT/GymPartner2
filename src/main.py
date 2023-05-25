import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bp_exercices import bp_exercises

# Récupération des variables d'environnement
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# Création de la chaine de caractère de connexion sql
db_info = 'mysql+pymysql://' + db_user + ':' + db_password + '@' + db_host + ':' + db_port + '/' + db_name

# Création d'un instance de l'application Flask
app = Flask(__name__)
app.register_blueprint(bp_exercises, url_prefix="/exercises/")

# Configuration des paramètres de connexion de la DB
app.config["SQLALCHEMY_DATABASE_URI"] = db_info

# Initialisation de la DB
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')