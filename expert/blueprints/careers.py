import json
from flask import Blueprint

careers = Blueprint('careers', __name__, url_prefix='/careers')

@careers.route('')
def get_careers():
    with open('data/initial_config.json', 'r') as file:
        data = json.load(file)
        return { 'data': data['profiles']}
