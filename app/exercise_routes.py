from Exercise import Exercise

from flask import Blueprint, jsonify


exercises_bp = Blueprint('exercises_bp', __name__, url_prefix='/exercises/')


@exercises_bp.route('/', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    exercises_data = [{'id': exercise.id, 'name': exercise.name, 'description': exercise.description} for exercise in
                      exercises]
    return jsonify(exercises_data)
