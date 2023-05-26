import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def config_db(app):
    # Récupération des variables d'environnement
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    # Création de la chaine de caractère de connexion sql
    db_info = 'mysql+pymysql://' + db_user + ':' + db_password + '@' + db_host + ':' + db_port + '/' + db_name
    print(db_info)

    # Configuration des paramètres de connexion de la DB
    app.config["SQLALCHEMY_DATABASE_URI"] = db_info
