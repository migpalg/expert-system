export PYTHON_PATH="$PYTHON_PATH:$(pwd)/expert"
export FLASK_APP=expert
export FLASK_ENV=development
pipenv run flask run
