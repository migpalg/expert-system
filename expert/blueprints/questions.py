import json
from flask import Blueprint
from uuid import uuid4

questions = Blueprint('questions', __name__, url_prefix='/questions')


@questions.route('', methods=['GET', 'POST'])
def get_questions():
    questions = {
        'questions': [
            {
                'id': '1',
                'title': 'hello world!',
                'options': [
                    {
                        'option_id': '1.1',
                        'text': 'Option 1',
                    },
                    {
                        'option_id': '1.2',
                        'text': 'Option 2',
                    }
                ]
            },
            {
                'id': '2',
                'title': 'question 2',
                'options': [
                    {
                        'option_id': '2.1',
                        'text': 'Option 1'
                    },
                    {
                        'option_id': '2.2',
                        'text': 'Option 2'
                    }
                ]
            }
        ]
    }

    return json.dumps(questions, separators=(',', ':'))


@questions.route('/create', methods=['POST'])
def create_question():
    return {
        'message': 'question created'
    }
