from flask import Blueprint
from uuid import uuid4

questions = Blueprint('questions', __name__, url_prefix='/questions')


@questions.route('', methods=['GET', 'POST'])
def get_questions():
    return {
        'questions': [
            {
                'id': uuid4(),
                'title': 'hello world!',
                'options': [
                    {
                        'option_id': uuid4(),
                        'text': 'Option 1',
                    },
                    {
                        'option_id': uuid4(),
                        'text': 'Option 2'
                    }
                ]
            }
        ]
    }


@questions.route('/create', methods=['POST'])
def create_question():
    return {
        'message': 'question created'
    }
