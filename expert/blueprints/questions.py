import json
from flask import Blueprint, request
from uuid import uuid4

questions = Blueprint('questions', __name__, url_prefix='/questions')


@questions.route('', methods=['GET', 'POST'])
def get_questions():
    with open('data/initial_config.json') as f:
        data = json.load(f)
        return {
            'count': len(data['questions']),
            'data': data['questions']
        }


@questions.route('/create', methods=['POST'])
def create_question():
    return {
        'message': 'question created',
        'question_id': uuid4()
    }
