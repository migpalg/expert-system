from flask import Blueprint, request
from uuid import uuid4

questions = Blueprint('questions', __name__, url_prefix='/questions')


@questions.route('', methods=['GET', 'POST'])
def get_questions():
    return {
        'count': 2,
        'questions': [
            {
                'id': uuid4(),
                'title': 'hello world!',
                'options': [
                    {
                        'value': uuid4(),
                        'text': 'Option 1',
                    },
                    {
                        'value': uuid4(),
                        'text': 'Option 2',
                    }
                ]
            },
            {
                'id': uuid4(),
                'title': 'question 2',
                'options': [
                    {
                        'value': uuid4(),
                        'text': 'Option 1'
                    },
                    {
                        'value': uuid4(),
                        'text': 'Option 2'
                    }
                ]
            }
        ]
    }


@questions.route('/create', methods=['POST'])
def create_question():
    return {
        'message': 'question created',
        'question_id': uuid4()
    }
