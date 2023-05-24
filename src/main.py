from flask import Flask
from bp_exercices import bp_exercises

app = Flask(__name__)
app.register_blueprint(bp_exercises, url_prefix="/exercises/")

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')