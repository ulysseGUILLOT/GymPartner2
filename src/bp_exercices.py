from flask import Blueprint, request, jsonify

bp_exercises = Blueprint(__name__, 'bp_exercises', url_prefix="exercises")

@bp_exercises.route("/all")
def get_all():
    return 'exercises list'