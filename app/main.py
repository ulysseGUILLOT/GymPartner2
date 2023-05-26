from flask import Flask

from config_db import config_db
from config_db import db
from exercise_routes import exercises_bp

import Exercise


# Création d'un instance de l'application Flask
app = Flask(__name__)

# Declaration des blueprints
app.register_blueprint(exercises_bp, url_prefix='/exercises/')

# Initialisation de la DB
config_db(app)
db.init_app(app)

# Création des tables si elles n'existent pas encore
with app.app_context():
    db.create_all()

# Démarrage du serveur Flask
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
