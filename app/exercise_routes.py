from Exercise import Exercise

from flask import Blueprint, jsonify

exercises_bp = Blueprint('exercises_bp', __name__, url_prefix='/exercises/')


@exercises_bp.route('/', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    exercises_data = [{'id': exercise.id, 'name': exercise.name, 'description': exercise.description} for exercise in
                      exercises]
    return jsonify(exercises_data)


@exercises_bp.route('/<int:exercise_id>', methods=['GET'])
def get_exercise(exercise_id):
    exercise = Exercise.query.get(exercise_id)

    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404

    exercise_data = {
        'id': exercise.id,
        'name': exercise.name,
        'description': exercise.description
    }

    return jsonify(exercise_data)
